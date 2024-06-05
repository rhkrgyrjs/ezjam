import re

def regexCheck(pattern, text):
    if re.fullmatch(pattern, text):
        return True
    else:
        return False

# 아이디 조건 : 8자~16자 / 영어,숫자 허용 / 숫자로 시작하면 안 됨
def idCheck(id):
    return regexCheck("^[a-zA-Z][a-zA-Z\d]{7,15}$", id)

# 닉네임 조건 : 2~10자 / 한글/영어/숫자 허용
def nicknameCheck(nickname):
    return regexCheck("^(?=.*[a-zA-Z가-힣0-9]).{2,10}$", nickname)

# 비밀번호 조건 : 8~20자 / 영어,숫자,특수문자 허용 / 영어소문자,영어대문자,숫자,특수문자 각각 1개 이상씩 포함
def passwordCheck(password):
    return regexCheck('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?":{}|<>])[a-zA-Z\d!@#$%^&*(),.?":{}|<>]{8,20}$', password)

# 이메일의 로컬 파트 조건 : RFC 5322
def emailLocalCheck(emailLocal):
    return regexCheck("^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]{1,64}(\.[a-zA-Z0-9!#$%&'*+/=?^_`{|}~-]{1,64})*$", emailLocal)

# 이메일의 도메인 파트 조건 : RFC 5322
def emailDomainCheck(emailDomain):
    return regexCheck("^[a-zA-Z0-9.-]{1,63}(\.[a-zA-Z0-9-]{1,63})*\.[a-zA-Z]{2,}$|^([a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$", emailDomain)

# 성/이름 조건
def nameCheck(name):
    return regexCheck("^[a-zA-Z가-힣]{1,50}$", name)

# 전화번호 조건
def phoneCheck(phone):
    return regexCheck("^0\d{10}$", phone)

# 주소 조건 (주소는 선택사항임)
def addressCheck(address):
    return regexCheck("^.{1,100}$", address)

# 우편번호 조건
def zipcodeCheck(zipcode):
    return regexCheck("^\d{5}$", zipcode)