// 플레이어 애니메이션 생성 함수
function createPlayerAnimations() {
    const directions = ['down', 'right', 'left', 'up'];
    const frames = [
        { key: 'down', frames: [0, 1, 0, 2] },
        { key: 'right', frames: [3, 4, 3, 5] },
        { key: 'left', frames: [8, 7, 8, 6] },
        { key: 'up', frames: [9, 10, 9, 11] }
    ];

    frames.forEach(animation => {
        this.anims.create({
            key: animation.key,
            frames: this.anims.generateFrameNumbers('player', { frames: animation.frames }),
            frameRate: 10,
            repeat: -1
        });
    });
}

// 새로운 플레이어 추가
function addPlayer(id, x, y) {
        if (!otherPlayers[id]) {
            otherPlayers[id] = game.scene.scenes[0].physics.add.sprite(x, y, 'player').setDisplaySize(25, 25);
            otherPlayersText[id] = game.scene.scenes[0].add.text(x, y + 30, id, {
                fontSize: '10px',
                fill: '#ffffff'
            });
            otherPlayersText[id].setOrigin(0.5);  // 텍스트를 가운데 정렬
            otherPlayers[id].setDepth(1);
            otherPlayersText[id].setDepth(1);
        }
}

// 모든 플레이어 삭제하는 함수
function removeAllOtherPlayers() 
{
    // 모든 플레이어를 순회
    for (let id in otherPlayers) {
        if (otherPlayers.hasOwnProperty(id) && id !== playerId) {
            // 현재 플레이어의 id가 아닌 플레이어만 삭제
            otherPlayers[id].destroy();  // 스프라이트 삭제
            otherPlayersText[id].destroy();  // 텍스트 삭제
            delete otherPlayers[id];  // 플레이어 객체 삭제
            delete otherPlayersText[id];  // 텍스트 객체 삭제
        }
    }
}