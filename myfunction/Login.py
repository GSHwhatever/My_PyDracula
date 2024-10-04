# -*- coding:utf8 -*-
"""
金保登录接口
"""
from requests.exceptions import RequestException, ConnectionError, Timeout, TooManyRedirects
import requests, time, os, configparser


class Login:

    def __init__(self, path) -> None:
        self.config = configparser.ConfigParser()
        self.path = path
        self.config.read(path)
        self.host = 'http://' + self.config.get('Host', 'jb_host')
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.95 Safari/537.36"
        }

    def auth(self, name=None, idcard=None):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "51",
            "Content-Type": "application/x-www-form-urlencoded",
            # "Cookie": "SESSION=ZTcxYzNjYmQtYzUyMS00NzBmLWJmY2UtOTE1YzFiODBhYWIz; JSESSIONID=5A5583C8C9D700B0CE1696AEC32058D2",
            "Host": "10.64.2.100:30010",
            "If-Modified-Since": "0",
            "Origin": self.host,
            "Pragma": "no-cache",
            "Referer": self.host + "/portal/login.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
        }
        payload = {
            "aac002": idcard if idcard else self.config.get('Info', 'password'),
            "aac003": name if name else self.config.get('Info', 'username')
        }
        url = self.host + '/portal/queryUserInfoWithChannel'
        res = requests.post(url=url, data=payload, headers=headers)
        if res.status_code == 200:
            return res.json()

    def login(self, dic):
        headers_login = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Authorization": "Basic amJ4cHQ6c3lzdGVt",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "71",
            "Content-Type": "application/json",
            # "Cookie": "SESSION=ZTcxYzNjYmQtYzUyMS00NzBmLWJmY2UtOTE1YzFiODBhYWIz; JSESSIONID=5A5583C8C9D700B0CE1696AEC32058D2",
            "Host": self.host.split('/')[-1],
            "Origin": self.host,
            "Pragma": "no-cache",
            "Referer": self.host + "/portal/login.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "X-Requested-With": 'XMLHttpRequest'
        }
        payload_login = {
            "password": dic.get('ua0102'),
            "username": dic.get('ua0100')
        }
        url_login = self.host + '/api/auth/channel/login'
        res_login = requests.post(url=url_login, json=payload_login, headers=headers_login)
        if res_login.status_code == 200:
            return res_login.json()

    def run(self, idcard=None, name=None):
        dic = self.auth(name=name, idcard=idcard)
        if dic:
            r = self.login(dic)
            if r and r.get('msg')  == "登陆成功":
                token = r.get('map').get('Access-Token')
                self.config.set('Token', 'Acces_Token', token)
                with open(self.path, 'w') as configfile:
                    self.config.write(configfile)
                self.headers.update({'Access-Token': token})
                name = name if name else self.config.get('Info', 'username')
                # print(f'{name}登录成功')
                origin = self.get_origin()
                user = self.query_user()
                return user, origin
            else:
                print('登录失败')
                print(dic)
                print(f'r:{r}')
                return '未知', '未知'
        else:
            print("登录失败")
            return '未知', '未知'

    def get_origin(self):
        res = requests.post(url=self.host + '/user/s9010202/entrydatagrid', headers=self.headers)
        if res.status_code == 200:
            data = res.json()
            return "".join(list(data.values()))

    def query_user(self):
        res = requests.post(url=self.host + '/main/works/queryUser', headers=self.headers)
        if res.status_code == 200:
            data = res.json()
            lis = list(data.values())
            lis.reverse()
            return "".join(lis[:2])
    
    def read_ini(self):
        username = self.config.get('Info', 'username')
        password = self.config.get('Info', 'password')
        return username, password

    def read_all(self):
        dic = {
            "name": self.config.get('Info', 'username'),
            "idcard": self.config.get('Info', 'password'),
            "path": self.config.get('Path', 'download'),
            "host": self.config.get('Host', 'host'),
            "jb_host": self.config.get('Host', 'jb_host'),
            "exe": self.config.get('Path', 'exe')
        }
        return dic
    
    def set_ini(self, key, dic):
        for k, v in dic.items():
            self.config.set(key, k, v)
        with open(self.path, 'w') as configfile:
            self.config.write(configfile)

    def main(self, *arg, **kwargs):
        error = 'None'
        try:
            user, origin = self.run(*arg, **kwargs)
        except ConnectionError as e:
            error = '连接错误：你上飞机了吗?就登录，臭小子'
            user = origin = '未知'
            # print(error)
        except Timeout as e:
            error = '连接超时：请重试'
            user = origin = '未知'
            print(error)
        except TooManyRedirects as e:
            error = f'重定向次数过多：{e}'
            user = origin = '未知'
            print(error)
        except RequestException as e:
            error = f'请求异常：{e}'
            user = origin = '未知'
            print(error)
        finally:
            return user, origin, error


if __name__ == "__main__":
    l = Login()
    l.main(name='高升', idcard='230304199812134414')
    # l.main()
