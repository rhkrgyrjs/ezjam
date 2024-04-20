 const userID_RegEx = "^[0-9a-zA-Z]{8,16}$";
 const userPW_RegEx = "^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()-_+=|\\{}\[\]:;<>,.?\/]).{8,20}$";
 const userEmail_local_RegEx = "^[a-zA-Z0-9._%+-]{2,64}$";
 const userEmail_Domain_RegEx = "^[a-zA-Z0-9.-]{1,63}(\.[a-zA-Z0-9.-]{1,63})*\.[a-zA-Z]{2,63}$";
 const userLastName_RegEx = "^(?=.*[a-zA-Z가-힣])[a-zA-Z가-힣]{1,50}$";
 const userFirstName_RegEx = "^(?=.*[a-zA-Z가-힣])[a-zA-Z가-힣]{1,50}$"
 const userPhone_RegEx = "^010-\d{4}-\d{4}$";
 const userNickname_RegEx = "^[a-zA-Z0-9가-힣]{2,10}$";
 const userAddress_RegEx = "^[가-힣a-zA-Z0-9!#$%&()*+,-./:;<=>?@\[\]^_`{|}~]{1,100}$";
 const userZipcode_RegEx = "^\d{5}$";
 // birthday, gender는 선택해 입력하는 것이기 때문에 정규식 X
 
 // id, pw, emailL, emailD, nameL, nameF birthday, phone, nickname, gender, address, zipcode