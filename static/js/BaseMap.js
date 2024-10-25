// BaseMap 씬 class
// 모든 맵은 BaseMap을 상속받아 만들어짐
class BaseMap extends Phaser.Scene
{
    constructor(key) { super(key); }

    // 타일셋과 맵을 로드하는 함수
    loadTilesetAndMap(tilesetsData) 
    {
        // 타일셋 이미지를 로드
        for (let tileset in tilesetsData) 
            {
            const imagePath = '/static/maps/tiles/' + tilesetsData[tileset].image;
            console.log('Loading tileset:', imagePath);
            this.load.image(tileset, imagePath);
        }

        // 타일맵 파일 로드
        this.load.tilemapTiledJSON(this.scene.key, `/static/maps/${this.scene.key}.json`);

        // 모든 타일셋 로드가 완료되면 타일맵 생성
        this.load.once('complete', () => {
            this.createTileMap();
        });
    }

    // 플레이어 생성하는 함순
    createPlayer() 
    {
        player = this.physics.add.sprite(400, 300, 'player').setDisplaySize(25, 25);
        player.setDepth(1);
        cursors = this.input.keyboard.createCursorKeys();

        const camera = this.cameras.main;
        camera.startFollow(player);
        camera.setZoom(1.5);
        camera.setBounds(0, 0, 1600, 1200);

        playerIdText = this.add.text(player.x, player.y + 30, playerId, 
            {
                fontSize: '10px',
                fill: '#ffffff'
            }).setOrigin(0.5).setDepth(1);

        createPlayerAnimations.call(this);
    }

    // 소켓 이벤트를 셋업하는 함수
    setupSocketEvents() 
    {
        // 서버에 새로운 플레이어 정보 전송
        // 맵(씬)마다 캐릭터를 관리하기 떄문에 씬 키를 붙임
        socket.emit(`${this.scene.key}_new_player`, { playerId: playerId, x: player.x, y: player.y });

        socket.on('existing_players', (playersData) => 
        {
            for (let id in playersData) 
            {
                if (id !== playerId) 
                {
                    addPlayer(id, playersData[id].x, playersData[id].y);
                    console.log('다른 플레이어 추가' + id);
                }
            }
        });

        socket.on('new_player', (data) => { addPlayer(data.playerId, data.x, data.y); });

        socket.on('remove_player', (id) => {
            if (otherPlayers[id]) {
                otherPlayers[id].destroy();
                otherPlayersText[id].destroy(); // 텍스트도 삭제
                delete otherPlayers[id];
                delete otherPlayersText[id];
            }
        });

        socket.on('player_moved', (data) => {
            if (otherPlayers[data.playerId]) {
                otherPlayers[data.playerId].setPosition(data.x, data.y);
                otherPlayersText[data.playerId].setPosition(data.x, data.y + 30);

                // 애니메이션 재생 (움직임 정보가 있을 경우)
                if (data.moved) {
                    otherPlayers[data.playerId].anims.play(data.direction, true);
                } else {
                    otherPlayers[data.playerId].anims.stop();
                    otherPlayers[data.playerId].setFrame(0); // 첫 프레임으로 설정
                }
            }
        });
    }

    preload()
    {
        // 상속받아 만들어진 씬의 키를 기반으로 에셋을 받아옴
        console.log(`${this.scene.key} 에셋 받아오는 중...`);
        socket.on(`${this.scene.key}_map_data`, (data) => 
        {
            console.log(`Received ${this.scene.key} Map data:`, data);
            this.loadTilesetAndMap(data.tilesets);
            this.load.start();
            console.log(`${this.scene.key} 프리로드 끝`);
        });

        // 플레이어 스프라이트 로드
        this.load.spritesheet('player', '/static/images/player.png', { frameWidth: 16, frameHeight: 16 });
    }

    update()
    {
        let moved = false;
        let direction = null;

        if (cursors.left.isDown) {
            player.setVelocityX(-200);
            direction = 'left';
            moved = true;
        } else if (cursors.right.isDown) {
            player.setVelocityX(200);
            direction = 'right';
            moved = true;
        } else {
            player.setVelocityX(0); // 속도 초기화
        }

        if (cursors.up.isDown) {
            player.setVelocityY(-200);
            direction = 'up';
            moved = true;
        } else if (cursors.down.isDown) {
            player.setVelocityY(200);
            direction = 'down';
            moved = true;
        } else {
            player.setVelocityY(0); // 속도 초기화
        }

        playerIdText.setPosition(player.x, player.y + 30);

        if (direction && currentAnimation !== direction) {
            player.anims.play(direction, true);
            currentAnimation = direction;
        }

        if (!moved && currentAnimation) {
            player.anims.stop();
            player.setFrame(0);
            currentAnimation = null;
        }
        
        socket.emit('player_moved', {
            playerId: playerId,
            x: player.x,
            y: player.y,
            moved: moved,
            direction: direction
        });

    }
}