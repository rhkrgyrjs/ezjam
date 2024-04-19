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
    if isUserLoggedIn():
        return render_template('error.html', errorMessage = "이미 로그인 중입니다.")
    if request.method == 'POST':
        print('로그인 페이지 POST')
        userNameAndNickname = DB.loginValidation(request.form['user-id'], request.form['user-pw'])
        if not userNameAndNickname:
            return render_template('login.html')
        else:
            userNickName = userNameAndNickname[0][1]
            session['userID'] = request.form['user-id']
            return render_template('index.html', loginInfo = userNickName)
    else:
        return render_template('login.html')
    
@app.route('/logout')
def logout():
    if isUserLoggedIn():
        session.pop('userID', None)
        return redirect(url_for('index'))
    

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        return render_template('signup.html')
    else:
        return render_template('signup.html')

        
    

if __name__ == '__main__':
    app.run(debug=True)