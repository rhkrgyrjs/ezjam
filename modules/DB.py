import pymysql
from . import SHA256
from . import RegEx

HOST = 'localhost'
USER_NAME = 'root'
USER_PASSWORD = 'zoo@123456'
DB_NAME = 'ezjam'

# 쿼리문들
LOGIN_VALIDATION_QUERY = "SELECT name, nickname FROM userinfo WHERE id=%s AND pw_hashed=%s"

# DB와 연결해 connection 객체 리턴하는 함수
def getConnection():
    try:
        return pymysql.connect(host=HOST, user=USER_NAME, passwd=USER_PASSWORD, db=DB_NAME, charset='utf8')
    except pymysql.Error as e:
        print("DB 연결에 실패했습니다.")
        print(e)
        return None

# 로그인 검증하는 함수
# 성공시 유저의 이름과 닉네임 든 리스트 리턴, 실패시 None 리턴
def loginValidation(userID, userPW):
    hashedPw = SHA256.encode(userPW)
    connection = getConnection()
    cursor = connection.cursor()
    value = (userID, hashedPw)
    cursor.execute(LOGIN_VALIDATION_QUERY, value)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if not data:
        return None
    else:
        return data

print("ti")
    