import hashlib

# 문자열을 받아 SHA-256 알고리즘으로 인코딩한 결과물을 리턴하는 함수(64자리의 문자열)
def encode(inputString):
    input_bytes = inputString.encode('utf-8')
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_bytes)
    encoded_string = sha256_hash.hexdigest()
    return encoded_string