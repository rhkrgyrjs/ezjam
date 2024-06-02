from flask import Flask, render_template, session, url_for, request, redirect, jsonify, current_app
from modules import DB
from modules import RegEx
import os
import datetime
import uuid
import random
from werkzeug.utils import secure_filename

app = Flask('EzJam Web')
app.secret_key = 'zoo@123456'

# 유저가 로그인되어있나 확인하는 함수
def isUserLoggedIn():
    if 'userID' in session:
        return True
    else:
        return False

# 메인 페이지 핸들러
@app.route('/')
def index():
    if isUserLoggedIn():
        return render_template('index.html', loginInfo = session['userID'])
    else:
        return render_template('index.html', loginInfo = None)

# 로그인 요청 핸들러
@app.route('/login', methods=['GET', 'POST'])
def login():
    if isUserLoggedIn():
        return render_template('error.html', errorMessage = "이미 로그인 중입니다.")
    if request.method == 'POST':
        print('로그인 페이지 POST')
        userNameAndNickname = DB.loginValidation(request.form['user-id'], request.form['user-pw'])
        if not userNameAndNickname:
            return render_template('login.html', loginMessage = "아이디 또는 비밀번호가 일치하지 않습니다.")
        else:
            userNickName = userNameAndNickname[0][0]
            session['userID'] = request.form['user-id']
            return render_template('index.html', loginInfo = userNickName)
    else:
        return render_template('login.html')

# 로그아웃 요청 핸들러
@app.route('/logout')
def logout():
    if isUserLoggedIn():
        session.pop('userID', None)
        return redirect(url_for('index'))
    
# 회원가입 요청 핸들러
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if isUserLoggedIn():
        session.pop('userID', None) # 로그인 되어있을 시 로그아웃 후 회원가입 진행함
        
    if request.method == 'POST':
        # 회원가입 검증 루틴
        # 정규식 검증 + 사용중인 아이디/닉네임/이메일인지 검증
        # 회원가입 성공시 리다이렉션 페이지로, 회원가입 실패시 json 보내기.
        userid = request.form.get('userid')
        userNickname = request.form.get('usernickname')
        userPassword = request.form.get('userpassword')
        userPasswordVal = request.form.get('userpasswordval')
        userEmailLocal = request.form.get('useremaillocal')
        userEmailDomain = request.form.get('useremaildomain')
        userLastName = request.form.get('userlastname')
        userFirstName = request.form.get('userfirstname')
        userSex = request.form.get('usersex')
        userBirthday = request.form.get('userbirthday')
        userPhone1 = request.form.get('userphone1')
        userPhone2 = request.form.get('userphone2')
        userPhone3 = request.form.get('userphone3')
        userPostcode = request.form.get('userzipcode')
        userAddress = request.form.get('useraddress')
        userAddressDetail = request.form.get('useraddressdetail')
    
        
        if DB.userIdCheck(userid) and RegEx.idCheck(userid): # 아이디 중복여부 / 정규식 체크
            if DB.userNicknameCheck(userNickname) and RegEx.nicknameCheck(userNickname): # 닉네임 중복여부 / 정규식 체크
                if userPassword == userPasswordVal and RegEx.passwordCheck(userPassword): # 비밀번호 확인 / 정규식 체크
                    if DB.userEmailCheck(userEmailLocal, userEmailDomain) and RegEx.emailLocalCheck(userEmailLocal) and RegEx.emailDomainCheck(userEmailDomain): # 이메일 중복여부 / 정규식 체크
                        if RegEx.nameCheck(userFirstName) and RegEx.nameCheck(userLastName): # 이름 정규식 체크
                            if DB.userPhoneCheck((userPhone1 + userPhone2 + userPhone3)) and RegEx.phoneCheck((userPhone1 + userPhone2 + userPhone3)): # 전화번호 중복여부 / 정규식 체크
                                if RegEx.zipcodeCheck(userPostcode): # 우편번호 체크
                                    if RegEx.addressCheck((userAddress + userAddressDetail)): # 주소 체크
                                        if userSex != None: # 성별 유효성 체크
                                            if userBirthday != '': # 생일 유효성 체크
                                                DB.signupRegister(userid, userPassword, userNickname, userEmailLocal, userEmailDomain, userLastName, userFirstName, userSex, userBirthday, (userPhone1 + userPhone2 + userPhone3), (userAddress + userAddressDetail), userPostcode)
                                                response = { 'status': 'success'}
                                                return jsonify(response)
                    # ================================ 여기서부터임. 유저 이메일 체크하는 루틴부터 계속
                    # 만약 성공하지 못했을 경우 response에 응답 메시지들 끼워넣는 것부터 계속
                    # signup.html에서도 회원가입 성공 못했을 경우 에러 메시지들 표시하는 것 추가해야함.
                    
        # 여기서부터는 회원가입 오류 시 처리루틴
        response = { 'status': 'error'}
        
        if not(DB.userIdCheck(userid)): # 아이디 중복 사용의 경우
            response['id_dup'] = 'error'
            response['id_dup_error'] = '아이디 중복체크를 하세요.'
        else:
            response['id_dup'] = 'success'
            
        if not(RegEx.idCheck(userid)): # 아이디 형식의 오류일 경우
            response['id_reg'] = 'error'
            response['id_reg_error'] = '아이디의 형식이 올바르지 않습니다.'
        else:
            response['id_reg'] = 'success'
            
            
        if not(DB.userNicknameCheck(userNickname)): # 닉네임 중복 사용의 경우
            response['nickname_dup'] = 'error'
            response['nickname_dup_error'] = '닉네임 중복체크를 하세요.'
        else:
            response['nickname_dup'] = 'success'
            
        if not(RegEx.nicknameCheck(userNickname)): # 닉네임 형식 오류의 경우
            response['nickname_reg'] = 'error'
            response['nickname_reg_error'] = '닉네임 형식이 올바르지 않습니다.'
        else:
            response['nickname_reg'] = 'success'
            
        if not(userPassword == userPasswordVal): # 비밀번호 확인이 안 된 경우
            response['password_val'] = 'error'
            response['password_val_error'] = '비밀번호가 일치하지 않습니다.'
        else:
            response['password_val'] = 'success'
            
        if not(RegEx.passwordCheck(userPassword)): # 비밀번호 형식이 올바르지 않을 경우
            response['password_reg'] = 'error'
            response['password_reg_error'] = '비밀번호 형식이 올바르지 않습니다.'
        else:
            response['password_reg'] = 'success'
            
        if not(DB.userEmailCheck(userEmailLocal, userEmailDomain)): # 사용중인 이메일인 경우
            response['email_dup'] = 'error'
            response['email_dup_error'] = '사용중인 이메일입니다.'
        else:
            response['email_dup'] = 'success'
            
        if not(RegEx.emailLocalCheck(userEmailLocal) and RegEx.emailDomainCheck(userEmailDomain)): # 이메일 형식이 올바르지 않을 경우
            response['email_reg'] = 'error'
            response['email_reg_error'] = '이메일 형식을 다시 확인하세요.'
        else:
            response['email_reg'] = 'success'
            
        if not(RegEx.nameCheck(userFirstName) and RegEx.nameCheck(userLastName)): # 이름의 형식이 올바르지 않을 경우
            response['name_reg'] = 'error'
            response['name_reg_error'] = '이름 형식이 잘못되었습니다.'
        else:
            response['name_reg'] = 'success'
            
        if not(DB.userPhoneCheck((userPhone1 + userPhone2 + userPhone3))): # 전화번호 중복 사용의 경우
            response['phone_dup'] = 'error'
            response['phone_dup_error'] = '사용중인 전화번호입니다.'
        else:
            response['phone_dup'] = 'success'
            
        if not(RegEx.phoneCheck((userPhone1 + userPhone2 + userPhone3))): # 전화번호 형식이 올바르지 않을 경우
            response['phone_reg'] = 'error'
            response['phone_reg_error'] = '전화번호 형식을 다시 확인하세요.'
        else:
            response['phone_reg'] = 'success'
            
        if not(RegEx.zipcodeCheck(userPostcode) and RegEx.addressCheck((userAddress + userAddressDetail))): # 주소 형식이 올바르지 않을 경우
            response['address_reg'] = 'error'
            response['address_reg_error'] = '주소 형식이 올바르지 않습니다.'
        else:
            response['address_reg'] = 'success'
            
        if not(userSex != None): # 성별을 선택하지 않았을 경우
            response['sex_reg'] = 'error'
            response['sex_reg_error'] = '성별을 선택하세요.'
        else:
            response['sex_reg'] = 'success'
            
        if not(userBirthday != ''): # 생일을 선택하지 않았을 경우
            response['birth_reg'] = 'error'
            response['birth_reg_error'] = '생일을 입력하세요.'
        else:
            response['birth_reg'] = 'success'
        
        print(response)
        return jsonify(response)
    else:
        return render_template('signup.html')

# 게임 접속 핸들러
@app.route('/game')
def game():
    if isUserLoggedIn():
        return render_template('game.html', loginInfo = session['userID'])
    else:
        return render_template('error.html', errorMessage = "게임에 접속하려면 먼저 로그인해야 합니다.")

# 회원가입 시 아이디 중복체크 핸들러
@app.route('/check_userid', methods=['POST'])
def check_id():
    userid = request.form.get('userid')
    # 빈칸도 걸러야함. 정규식 검사 하자.
    if userid == '':
        response = {'status': 'error', 'message': '사용할 아이디을 입력하세요.'}
        
    elif not(RegEx.idCheck(userid)):
        response = {'status': 'error', 'message': 'ID는 숫자로 시작하지 않는 8~16자의 영어/숫자 조합입니다.'}
        
    elif DB.userIdCheck(userid):
        response = {'status': 'success', 'message': '사용 가능한 아이디입니다.'}
    else:
        response = {'status': 'error', 'message': '이미 사용 중인 아이디입니다.'}
    return jsonify(response)
    
# 회원가입 시 닉네임 중복체크 핸들러
@app.route('/check_usernickname', methods=['POST'])
def check_nickname():
    usernickname = request.form.get('usernickname')
    # 빈칸도 걸러야함. 정규식 검사 하자.
    if usernickname == '':
        response = {'status': 'error', 'message': '사용할 닉네임을 입력하세요.'}
    elif not(RegEx.nicknameCheck(usernickname)):
        response = {'status': 'error', 'message': '닉네임은 2~10자의 한글/영어/숫자 조합입니다.'}
    
    elif DB.userNicknameCheck(usernickname):
        response = {'status': 'success', 'message': '사용 가능한 닉네임입니다.'}
    else:
        response = {'status': 'error', 'message': '이미 사용 중인 닉네임입니다.'}
    return jsonify(response)
    
    
    
# 파일의 UUID 생성하는 함수
def gen_rnd_filename():
    filename_prefix = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    return '%s%s' % (filename_prefix, str(random.randrange(1000, 10000)))


# 글쓰기 페이지 핸들러
@app.route('/write', methods=['GET', 'POST'])
def write_post():
    # 로그인하지 않은 유저가 글쓰기 페이지에 접속하면, 로그인 페이지로 리다이렉션
    if not(isUserLoggedIn()):
        return render_template('login.html')

    # 글쓰기 페이지에 접속(GET) 요청을 한 경우, 글쓰기 페이지만 렌더링함.
    if request.method == 'GET':
        return render_template('write.html')
    
    # POST 요청시 글 작성
    if request.method == 'POST':
        print(request.form['title'])
        print(request.form['content'])
        print(session['userID'])
        print(DB.get_nickname_with_id(session['userID']))
        num_article = DB.write_article(session['userID'], DB.get_nickname_with_id(session['userID']), request.form['title'], request.form['content'])
        print('글번호 : ' + str(num_article))
        # 테스트
        return redirect('/post/' + num_article)
            
# 사진 업로드 핸들러
@app.route('/upload_img/', methods=['POST', 'OPTIONS'])
def upload_img():
    if request.method == 'POST' and 'upload' in request.files:
        fileobj = request.files['upload']
        
        # 파일 이름과 확장자 분리
        original_filename = secure_filename(fileobj.filename)
        fname, fext = os.path.splitext(original_filename)
        
        # 확장자가 없다면 기본 확장자 설정 (필요한 경우)
        if not fext:
            fext = '.jpg'  # 예시로 jpg를 기본 확장자로 사용
            # 또는
            # return jsonify({"error": {"message": "File extension is missing"}}), 400
        
        # 임의의 파일 이름 생성
        rnd_name = '%s%s' % (gen_rnd_filename(), fext)
        filepath = os.path.join(current_app.static_folder, 'upload', rnd_name)
        dirname = os.path.dirname(filepath)
        
        # 디렉토리 생성
        if not os.path.exists(dirname):
            try:
                os.makedirs(dirname)
            except Exception as e:
                return jsonify({"error": {"message": f"Could not create directory: {str(e)}"}}), 500
        
        # 디렉토리 쓰기 권한 확인
        if not os.access(dirname, os.W_OK):
            return jsonify({"error": {"message": "Directory is not writable"}}), 500

        try:
            # 파일 저장
            fileobj.save(filepath)
            url = url_for('static', filename=f'upload/{rnd_name}', _external=True)
            return jsonify({"url": url})
        except Exception as e:
            return jsonify({"error": {"message": f"Could not save file: {str(e)}"}}), 500
    
    return jsonify({"error": {"message": "Invalid request"}}), 400

# 자유게시판 페이지 핸들러
@app.route('/community')
def community():
    # 페이지 번호 및 페이지당 게시물 수
    page = request.args.get('page', 1, type=int)
    per_page = 10
    
    # 게시물 가져오기 (페이징 기능 추가)
    start_index = (page - 1) * per_page
    
    connection = DB.getConnection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, author_nickname, created_at FROM posts ORDER BY created_at DESC LIMIT %s, %s", (start_index, per_page))
    posts = cursor.fetchall()
    cursor.execute("SELECT COUNT(*) AS count FROM posts")
    total_count = cursor.fetchone()[0]
    cursor.close()
    connection.close()
    # 총 페이지 수 계산
    total_pages = (total_count // per_page) + (1 if total_count % per_page > 0 else 0)
    
    return render_template('community.html', posts=posts, page=page, total_pages=total_pages, loginInfo=session['userID'])

# 게시글 조회 페이지 핸들러
@app.route('/post/<int:post_id>')
def view_post(post_id):
    ## 임시
    title, author_nickname, content= DB.get_post(str(post_id))
    if title:
        return render_template('post.html', title=title, nickname=author_nickname, content=content)
    else:
        return render_template('post.html', title='게시글을 찾을 수 없습니다.', nickname='?', content='?')

if __name__ == '__main__':
    app.run(debug=True)