from flask import session

# 관리자의 ID 하드코딩
ADMIN_ID = 'rhkrgyrjsl'

# 유저가 로그인되어있나 확인하는 함수
def isUserLoggedIn():
    if 'userID' in session:
        return True
    else:
        return False

def getUserId():
    if isUserLoggedIn() == True:
        return str(session['userID'])
    else:
        return False

def isUserAdmin():
    if 'userID' in session and session['userID'] == ADMIN_ID:
        return True
    else:
        return False