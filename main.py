import requests
import re


class Connecter:

    def __init__(self):
        self.headers = {
            "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko)",
            "Accept-Encoding": "gzip, deflate",
        }
        self.user_id_list = []
        self.url_left = 'http://172.25.249.8/eportal/auth/jsonp/login?jsonp=getJSONP.getJSONPabc&userId='
        self.url_middle = '&password=419433c6c3d8057ac1ef5ef6817dfdd8f11def4536af193e1ed07536e8e9ee65285c6ff4d8de3251c0091518d1eb4dd7fcc20ee5300d292a0fb8bda678cad3e434041e8e854d15d3689bc51c84fb44f961e354409fa75deb2f3f1c263e8ab927cae0a4626031ddfc72f9a80a79a2cfa655c1754585659e293995d8d1f5466b49&service=&queryString=version%3D52472d65506f7274616c20454e54455250524953455f342e3231287032295f4275696c643230313730383136%26userip%3D'
        self.url_right = '%26wlanacname%3D%26nasip%3D171.88.130.251%26wlanparameter%3D8c-85-90-16-5d-87%26url%3Dhttp%3A%2F%2F123.123.123.123%2F%26userlocation%3Dethtrunk%2F3%3A291.3201&operatorPwd=&operatorUserId=&validcode='

    def get_internet_ip_addr(self):
        new_session = requests.session()
        response = new_session.get(url="http://123.123.123.123/';%3C/script%3E")
        url = response.url
        ip = re.findall(r'[0-9]+(?:\.[0-9]+){3}', url)
        return ip[1]

    def connect_to_internet(self):
        ip_addr = self.get_internet_ip_addr()
        headers = self.headers
        for user_id in self.user_id_list:
            print("trying to connect by " + str(user_id))
            response = requests.get(headers=headers,
                                    url=self.url_left + str(user_id) + self.url_middle + ip_addr + self.url_right)
            if 'success' in response.text:
                print("succeed to connect by " + str(user_id))
                break
            else:
                print("faild")


if __name__ == '__main__':
    Connecter().connect_to_internet()
