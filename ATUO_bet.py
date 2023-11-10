import re,json,os
import requests,random,string,sys
from bs4 import BeautifulSoup
import random

id=int(input("Enter Your BET iD:-  "))
opt=int(input("\n[1] __8.89%\n[2]__6.21%\n[3]__3.99%\n[4]__0.99%\n[5]__1.01%\n[6]__1.20%\n[7]__1.05%\n[8]__2.50%\n[9]__1.08%\n[10]__1.06%\n[11]__1.10%\n[12]__1.02%\n[13]__1.14%\n[14]__1.07%\n[15]__1.18%\n[16]__1.16%\n[17]__1.12%\n[18]__1.03%\n\n[#]please choise Your option:- "))
pro=input("Enter Your proFiT:- ")


for i in range(501):
    try:
        registration_url = "https://onefootballf66.com/index.php/login"

# Send a GET request to the registration page
        response = requests.get(registration_url)
        cookie=response.headers["Set-cookie"].split(";")[0]

        soup = BeautifulSoup(response.text, 'html.parser')

        token_input = soup.find('input', {'name': '_token'})
        if token_input:
            token_value = token_input['value']
        else:
                print("Token not found in the HTML.")
                token_value = ""

    # Generate a CAPTCHA code (you can modify this part as needed)
        def generate_captcha():
                alphabets = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
        
                first = random.choice(alphabets)
                second = str(random.randint(0, 9))
                third = str(random.randint(0, 9))
                fourth = random.choice(alphabets)
                fifth = random.choice(alphabets)
        
                captcha = first + second + third + fourth + fifth
                return captcha

        captcha = generate_captcha()
        headers={
            "Cookie": f"{cookie}"
    }
        C=i+1
        directory = f"/sdcard/ONE_BET/ONE_BET{C}.json"
        with open(directory, 'r') as file:
                data = file.read()
                ck=data.split('=')[1].split('password')[0]
                ck2=data.split('=')[2]
        form_data = {
        "username": f"{ck}",
        "password": f"{ck2}",
        "code": captcha,
        "_token": token_value,
    }

        login_resp=requests.post(registration_url, headers=headers, data=form_data)
        ckie=login_resp.headers.get("set-cookie").split(';')[0]
        chk={
    "cookie": ckie,
    }
        A=requests.get("https://onefootballf66.com/index.php/user/event-list", headers=chk)
        js_code = A.text
        token_match = re.search(r"_token:\s*'([^']*)'", js_code)
        token = token_match.group(1)
        ckiee=A.headers["Set-cookie"].split(';')[0]
        bet_url = "https://onefootballf66.com/index.php/user/place-bet"
        bet_headers = {
    'authority': 'onefootballf66.com',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': f'{ckiee}',
    'origin': 'https://onefootballf66.com',
    'referer': 'https://onefootballf66.com/index.php/user/event-list',
    'x-requested-with': 'XMLHttpRequest'
        }
        bet_data = {
            '_token': token,
            'id': f'{id}',
            'option': f'{opt}',
            'amount': '150',
            'profit': f'{pro}'
        }
        bet_response = requests.post(bet_url, headers=bet_headers, data=bet_data)
        print(i+1,bet_response.text)
    except Exception as e:
            print("\n",i+1,f"\nError: {e}\n")
            pass
        
