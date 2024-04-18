from flask import Flask, render_template, session, url_for, request, redirect
from modules import DB

app = Flask('EzJam Web')
app.secret_key = 'zoo@123456'

def isUserLoggedIn():
    if 'userID' in session:
        return True
    else:
        return False

@app.route('/')
def index():
    if isUserLoggedIn():
        return render_template('index.html', loginInfo = session['userID'])
    else:
        return render_template('index.html', loginInfo = None)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인 검증 루틴
        print('로그인 페이지 POST')
        userNameAndNickname = DB.loginValidation(request.form['user-id'], request.form['user-pw'])
        if not userNameAndNickname:
            print("로그인 실패")
        else:
            print("로그인 성공")
            print(userNameAndNickname)
            session['userID'] = request.form['user-id']
        return render_template('index.html', loginInfo = request.form['user-id'])
    else:
        # 그냥 로그인 페이지 요청했을 경우
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    if isUserLoggedIn():
        session.pop('userID', None)
        return redirect(url_for('index'))
        
    

if __name__ == '__main__':
    app.run(debug=True)