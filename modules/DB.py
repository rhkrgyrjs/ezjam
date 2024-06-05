import pymysql
from . import SHA256
from . import RegEx

HOST = 'localhost'
USER_NAME = 'root'
USER_PASSWORD = 'zoo@123456'
DB_NAME = 'ezjam'

# 쿼리문들
LOGIN_VALIDATION_QUERY = "SELECT nickname FROM userinfo WHERE id=%s AND pw_hashed=%s"
USER_ID_CHECK_QUERY = "SELECT id FROM userinfo WHERE id=%s"
USER_NICKNAME_CHECK_QUERY = "SELECT nickname FROM userinfo WHERE nickname=%s"
USER_EMAIL_CHECK_QUERY = "SELECT email_local, email_domain FROM userinfo WHERE email_local=%s AND email_domain=%s"
USER_PHONE_CHECK_QUERY = 'SELECT phone FROM userinfo WHERE phone=%s'
SIGNUP_QUERY = "INSERT INTO userinfo (id, pw_hashed, nickname, email_local, email_domain, name_last, name_first, sex, birthday, phone, address, zipcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
USER_NICKNAME_QUERY = "SELECT nickname FROM userinfo WHERE id=%s"
WRITE_ARTICLE_QUERY = "INSERT INTO posts (title, author_id, author_nickname, content) VALUES (%s, %s, %s, %s)"
POST_SEARCH_QUERY = "SELECT title, author_nickname, created_at, views, content, id FROM posts WHERE id=%s"
VIEWS_INCREASE_QUERY = "UPDATE posts SET views = views + 1 WHERE id = %s"
COMMENTS_FETCH_QUERY = "SELECT author_nickname, created_at, content, id FROM comments WHERE post_id=%s ORDER BY created_at DESC"
REPLYS_FETCH_QUERY = "SELECT author_nickname, created_at, content, comment_id FROM replys WHERE post_id=%s ORDER BY created_at DESC"
WRITE_COMMENT_QUERY = "INSERT INTO comments (post_id, author_id, author_nickname, content) VALUES (%s, %s, %s, %s)"
WRITE_REPLY_QUERY = "INSERT INTO replys (post_id, comment_id, author_id, author_nickname, content) VALUES (%s, %s, %s, %s, %s)"

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

# 아이디 중복체크하는 함수
# 유저가 입력한 아이디가 현재 사용중인(DB에 존재하는) 아이디인지 체크
# 사용 가능시 True, 사용 불가능시 False 리턴
def userIdCheck(userID):
    connection = getConnection()
    cursor = connection.cursor()
    value = (userID)
    cursor.execute(USER_ID_CHECK_QUERY, value)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if not data:
        return True
    else:
        return False
    
# 닉네임 중복체크하는 함수
# 유저가 입력한 닉네임이 현재 사용중인(DB에 존재하는) 닉네임인지 체크
# 사용 가능시 True, 사용 불가능시 False 리턴
def userNicknameCheck(userNickname):
    connection = getConnection()
    cursor = connection.cursor()
    value = (userNickname)
    cursor.execute(USER_NICKNAME_CHECK_QUERY, value)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if not data:
        return True
    else:
        return False
    
# 이메일 중복체크하는 함수
# 유저가 입력한 이메일이 현재 사용중인(DB에 존재하는) 이메일인지 체크
# 사용 가능시 True, 사용 불가능시 False 리턴
def userEmailCheck(userEmailLocal, userEmailDomain):
    connection = getConnection()
    cursor = connection.cursor()
    value = (userEmailLocal, userEmailDomain)
    cursor.execute(USER_EMAIL_CHECK_QUERY, value)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if not data:
        return True
    else:
        return False
    
# 전화번호 중복체크하는 함수
# 유저가 입력한 전화번호가 현재 사용중인(DB에 존재하는) 전화번호인지 체크
# 사용 가능시 True, 사용 불가능시 False 리턴
def userPhoneCheck(userPhone):
    connection = getConnection()
    cursor = connection.cursor()
    value = (userPhone)
    cursor.execute(USER_PHONE_CHECK_QUERY, value)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if not data:
        return True
    else:
        return False
    
# 회원가입 함수
def signupRegister(id, pw, nickname, email_local, email_domain, last_name, first_name, sex, birthday, phone, address, zipcode):
    connection = getConnection()
    cursor = connection.cursor()
    pw_hashed = SHA256.encode(pw)
    data = (id, pw_hashed, nickname, email_local, email_domain, last_name, first_name, sex, birthday, phone, address, zipcode)
    cursor.execute(SIGNUP_QUERY, data)
    connection.commit()
    cursor.close()
    connection.close()
    
# 유저의 아이디로 닉네임 찾는 함수
def get_nickname_with_id(userid):
    connection = getConnection()
    cursor = connection.cursor()
    value = (userid)
    cursor.execute(USER_NICKNAME_QUERY, value)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if data:
        return data[0][0]
    else:
        return False
    
# 자유게시판 글 업로드 함수
def write_article(authorId, authorNickname, title, content):
    connection = getConnection()
    cursor = connection.cursor()
    data = (title, authorId, authorNickname, content)
    cursor.execute(WRITE_ARTICLE_QUERY, data)
    last_row_id = cursor.lastrowid
    connection.commit()
    cursor.close()
    connection.close()
    return str(last_row_id)

# 게시글 조회하는 함수
def get_post(postId):
    connection = getConnection()
    cursor = connection.cursor()
    value = (postId)
    cursor.execute(POST_SEARCH_QUERY, int(value))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if data:
        return data[0][0], data[0][1], data[0][2], data[0][3], data[0][4], data[0][5]
    else:
        return False, False, False, False, False

# 댓글 불러온느 함수
def get_comments(postId):
    connection = getConnection()
    cursor = connection.cursor()
    value = (postId)
    cursor.execute(COMMENTS_FETCH_QUERY, int(value))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if data:
        print('댓글', data)
        return data
    else:
        return False
    
# 대댓글 불러오는 함수
def get_replys(postId):
    connection = getConnection()
    cursor = connection.cursor()
    value = (postId)
    cursor.execute(REPLYS_FETCH_QUERY, int(value))
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    if data:
        print('대댓글', data)
        return data
    else:
        return False
    
# 게시글 조회수 올리는 함수
def view_count_post(postId):
    connection = getConnection()
    cursor = connection.cursor()
    value = (postId)
    cursor.execute(VIEWS_INCREASE_QUERY, int(value))
    connection.commit()
    cursor.close()
    connection.close()
    
# 댓글 작성 함수
def write_comment(postId, authorId, content):
    authorNickname = get_nickname_with_id(authorId)
    connection = getConnection()
    cursor = connection.cursor()
    value = (postId, authorId, authorNickname, content)
    cursor.execute(WRITE_COMMENT_QUERY, value)
    connection.commit()
    cursor.close()
    connection.close()

# 대댓글 작성 함수
def write_reply(postId, commentId, authorId, content):
    authorNickname = get_nickname_with_id(authorId)
    connection = getConnection()
    cursor = connection.cursor()
    value = (postId, commentId, authorId, authorNickname, content)
    cursor.execute(WRITE_REPLY_QUERY, value)
    connection.commit()
    cursor.close()
    connection.close()
    