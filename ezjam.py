# ezjam.py
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
from community import community_profile
from modules import DB
from modules import LoadJSON
import session_handle as shand

app = Flask('EzJam')
app.secret_key = 'zoo@123456'
socketio = SocketIO(app)

app.register_blueprint(community_profile)

# 플레이어 정보 저장하는 딕셔너리
players = {}

# 타일맵(stage) 데이터를 저장하는 변수
stage_data = {}
tilesets_data = {}


# 서버 시작 시 JSON 데이터 불러오기
tilesetsData = LoadJSON.loadMapTilesetsData()
mainMapData = LoadJSON.loadMapJsonData('main')
lobbyMapData = LoadJSON.loadMapJsonData('lobby')
hiphopMapData = LoadJSON.loadMapJsonData('hiphop')
balladMapData = LoadJSON.loadMapJsonData('ballad')
rockMapData = LoadJSON.loadMapJsonData('rock')
indiMapData = LoadJSON.loadMapJsonData('indi')


@app.route('/game')
def startGame():
    if not shand.isUserLoggedIn():
        return redirect(url_for('community.login'))
    else:
        return render_template("game.html")

@socketio.on('getNickName')
def ret_nickname():
    emit('nickName', str(DB.get_nickname_with_id(shand.getUserId())))

# 메인 맵에 새로운 플레이어가 접속할 때 처리 -- > 임시
@socketio.on('main_new_player')
def handle_main_new_player(data):
    if shand.isUserLoggedIn():
        print('메인방에 캐릭터가 입장했습니다')
        player_id = str(DB.get_nickname_with_id(shand.getUserId())) # 플레이어 ID 가져오기
        session['userNickname'] = player_id  # 세션에 닉네임 저장 (웹 소켓에서 필요하지 않음)
        
        # 플레이어 정보 players 딕셔너리에 저장
        players[player_id] = {'x': data['x'], 'y': data['y'], 'sid': request.sid}
        
        emit('existing_players', players, room=request.sid)  # 현재 플레이어에게 다른 플레이어 정보 전송
        print(players)
        emit('main_map_data', {'stage': mainMapData, 'tilesets': tilesetsData}, room=request.sid) # 맵 데이터 전송
        emit('new_player', data, broadcast=True, include_self=False)  # 다른 플레이어에게 새 플레이어 정보 전송
        print(players)
    else:
        return redirect(url_for('community.login'))

# 로비 맵에 새로운 플레이어가 접속할 때 처리 -- > 임시
@socketio.on('lobby_new_player')
def handle_lobby_new_player(data):
    if shand.isUserLoggedIn():
        print('힙합방에 캐릭터가 입장했습니다')
        player_id = str(DB.get_nickname_with_id(shand.getUserId())) # 플레이어 ID 가져오기
        session['userNickname'] = player_id  # 세션에 닉네임 저장 (웹 소켓에서 필요하지 않음)
        
        # 플레이어 정보 players 딕셔너리에 저장
        players[player_id] = {'x': data['x'], 'y': data['y'], 'sid': request.sid}
        
        emit('existing_players', players, room=request.sid)  # 현재 플레이어에게 다른 플레이어 정보 전송
        print(players)
        emit('lobby_map_data', {'stage': lobbyMapData, 'tilesets': tilesetsData}, room=request.sid) # 맵 데이터 전송
        emit('new_player', data, broadcast=True, include_self=False)  # 다른 플레이어에게 새 플레이어 정보 전송
        print(players)
    else:
        return redirect(url_for('community.login'))

# 힙합 맵에 새로운 플레이어가 접속할 때 처리 -- > 임시
@socketio.on('hiphop_new_player')
def handle_hiphop_new_player(data):
    if shand.isUserLoggedIn():
        print('힙합방에 캐릭터가 입장했습니다')
        player_id = str(DB.get_nickname_with_id(shand.getUserId())) # 플레이어 ID 가져오기
        session['userNickname'] = player_id  # 세션에 닉네임 저장 (웹 소켓에서 필요하지 않음)
        
        # 플레이어 정보 players 딕셔너리에 저장
        players[player_id] = {'x': data['x'], 'y': data['y'], 'sid': request.sid}
        
        emit('existing_players', players, room=request.sid)  # 현재 플레이어에게 다른 플레이어 정보 전송
        print(players)
        emit('hiphop_map_data', {'stage': hiphopMapData, 'tilesets': tilesetsData}, room=request.sid) # 맵 데이터 전송
        emit('new_player', data, broadcast=True, include_self=False)  # 다른 플레이어에게 새 플레이어 정보 전송
        print(players)
    else:
        return redirect(url_for('community.login'))

# 락 맵에 새로운 플레이어가 접속할 때 처리 -- > 임시
@socketio.on('rock_new_player')
def handle_rock_new_player(data):
    if shand.isUserLoggedIn():
        print('힙합방에 캐릭터가 입장했습니다')
        player_id = str(DB.get_nickname_with_id(shand.getUserId())) # 플레이어 ID 가져오기
        session['userNickname'] = player_id  # 세션에 닉네임 저장 (웹 소켓에서 필요하지 않음)
        
        # 플레이어 정보 players 딕셔너리에 저장
        players[player_id] = {'x': data['x'], 'y': data['y'], 'sid': request.sid}
        
        emit('existing_players', players, room=request.sid)  # 현재 플레이어에게 다른 플레이어 정보 전송
        print(players)
        emit('rock_map_data', {'stage': rockMapData, 'tilesets': tilesetsData}, room=request.sid) # 맵 데이터 전송
        emit('new_player', data, broadcast=True, include_self=False)  # 다른 플레이어에게 새 플레이어 정보 전송
        print(players)
    else:
        return redirect(url_for('community.login'))

# 발라드 맵에 새로운 플레이어가 접속할 때 처리 -- > 임시
@socketio.on('ballad_new_player')
def handle_ballad_new_player(data):
    if shand.isUserLoggedIn():
        print('힙합방에 캐릭터가 입장했습니다')
        player_id = str(DB.get_nickname_with_id(shand.getUserId())) # 플레이어 ID 가져오기
        session['userNickname'] = player_id  # 세션에 닉네임 저장 (웹 소켓에서 필요하지 않음)
        
        # 플레이어 정보 players 딕셔너리에 저장
        players[player_id] = {'x': data['x'], 'y': data['y'], 'sid': request.sid}
        
        emit('existing_players', players, room=request.sid)  # 현재 플레이어에게 다른 플레이어 정보 전송
        print(players)
        emit('ballad_map_data', {'stage': balladMapData, 'tilesets': tilesetsData}, room=request.sid) # 맵 데이터 전송
        emit('new_player', data, broadcast=True, include_self=False)  # 다른 플레이어에게 새 플레이어 정보 전송
        print(players)
    else:
        return redirect(url_for('community.login'))

# 인디 맵에 새로운 플레이어가 접속할 때 처리 -- > 임시
@socketio.on('indi_new_player')
def handle_indi_new_player(data):
    if shand.isUserLoggedIn():
        print('힙합방에 캐릭터가 입장했습니다')
        player_id = str(DB.get_nickname_with_id(shand.getUserId())) # 플레이어 ID 가져오기
        session['userNickname'] = player_id  # 세션에 닉네임 저장 (웹 소켓에서 필요하지 않음)
        
        # 플레이어 정보 players 딕셔너리에 저장
        players[player_id] = {'x': data['x'], 'y': data['y'], 'sid': request.sid}
        
        emit('existing_players', players, room=request.sid)  # 현재 플레이어에게 다른 플레이어 정보 전송
        print(players)
        emit('indi_map_data', {'stage': indiMapData, 'tilesets': tilesetsData}, room=request.sid) # 맵 데이터 전송
        emit('new_player', data, broadcast=True, include_self=False)  # 다른 플레이어에게 새 플레이어 정보 전송
        print(players)
    else:
        return redirect(url_for('community.login'))


# 플레이어의 움직임을 처리
@socketio.on('player_moved')
def handle_player_moved(data):
    player_sid = request.sid  # 소켓 ID로 플레이어 식별
    player_id = None

    # request.sid로 플레이어 ID 찾기
    for pid, info in players.items():
        if info.get('sid') == player_sid:
            player_id = pid
            break

    if player_id:
        # 플레이어 위치 업데이트
        players[player_id] = {'x': data['x'], 'y': data['y'], 'sid': request.sid}
        emit('player_moved', data, broadcast=True, include_self=False)  # 다른 클라이언트에 위치 전송

# 플레이어가 접속을 종료했을 때 처리
@socketio.on('disconnect')
def handle_disconnect():
    for player_id, info in list(players.items()):
        if info.get('sid') == request.sid:
            del players[player_id]
            emit('remove_player', player_id, broadcast=True)
            print(f"Player {player_id} disconnected")
            break



# 이하 채팅 기능 테스트
@socketio.on('chat-send')
def chatMessageBroadcast(data):
    emit('chat-receive', data, broadcast=True, include_self=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
