const socket = io();        // 소켓 통신을 위한 SocketIO 객체
let playerId;               // 플레이어의 아이디를 저장하는 변수
let gameInitialized = false;// 게임의 초기화 여부를 저장하는 변수

let game;                   // Phaser 게임 객체

let player;                 // 플레이어 Sprite를 저장
let playerIdText;           // 플레이어의 닉네임 렌더링
let otherPlayers = {};      // 같은 맵에 있는 다른 플레이어들의 좌표 저장
let otherPlayersText = {};  // 같은 맵에 있는 다른 플레이어들의 닉네임 저장
let cursors;
let currentAnimation = null;

// 내 닉네임을 서버로부터 불러오고 게임 이니셜라이징
socket.emit('getNickName');
socket.on('nickName', function(nickName) 
{
    playerId = nickName;
    console.log('받은 playerId:', playerId);

    if (!gameInitialized) {
        initializeGame();
        gameInitialized = true;
    }
});

// 게임 이니셜라이징
function initializeGame() 
{
    const config = {
        type: Phaser.AUTO,
        width: 800,
        height: 600,
        physics: {
            default: 'arcade',
            arcade: {
                gravity: { y: 0 },
                debug: true // 테스트용
            }
        },
        scene: [MainMap, LobbyMap, HipHopMap, RockMap, BalladMap, IndiMap]
    };

    game = new Phaser.Game(config);
}