// 채팅 기능 테스트
socket.on('chat-receive', function (data) {
    console.log(String(data.nickName) + ' : ' + String(data.message));
}); 

function sendChatMessage(message)
{
    socket.emit('chat-send', {nickName: playerId, message: message});
}