import requests
from bs4 import BeautifulSoup
import re


class Jkdk:
    login_url = r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'

    def __init__(self, uid='201924080230', upw='PyfDsZ25nc*nQG'):
        self.src = ''

        self.headers1 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Referer': r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
        }

        self.headers2 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Referer': self.src
        }

        self.headers3 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Referer': self.src,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.headers4 = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
            'Referer': self.src,
        }

        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Referer': self.src,
        'Content-Type': 'application/x-www-form-urlencoded'
        }

        self.uid = uid  # 用户号
        self.upw = upw  # 密码
        self.ptopid = ''
        self.sid = ''
        pass

    def encode(self, page):
        text = page.text.encode(page.encoding).decode(page.apparent_encoding)
        return text

    def valid(self, page):
        if page.status_code == 200:
            return self.encode(page)
        else:
            return None

    def strSearch(self, res: str, target):
        patterns = re.compile(res)
        outputs = patterns.search(target)
        return outputs

    def parse(self, text, label: str, attrs: dict, target: str):
        bs4 = BeautifulSoup(text, 'lxml')
        body = bs4.find(label, attrs=attrs)
        return body.get(target)

    def jkdk(self):
        session = requests.Session()
        self.jkdk1(session, header=self.headers1, data=None)
        pass

    def jkdk1(self, session, header, data):
        page = session.post(login_url, data=data, headers=self.headers1)
        text = self.encode(page)  # 得到登陆后的界面，但是还没有开始正式填写
        self.src = self.output.group(1)
        outputs = self.strSearch('ptopid=(.*)&sid=(.*)', self.src)

        self.septopid = outputs.group(1)
        self.sid = outputs.group(2)

    def jkdk2(self, session, header, data):
        page = session.get(self.src, headers=self.headers2)
        text = self.encode(page=page)
        self.src = self.parse(text=text, label='iframe', attrs={
            'id': 'zzj_top_6s'},  target='src')
        outputs = self.strSearch(r'ptopid=(.*)&sid=(.*)', self.src)
        self.ptopid = outputs.group(1)
        self.sid = outputs.group(2)
    
    def jkdk3(self, session, header, data):
        page = session.get(self.src, headers=self.headers3)
        text = self.encode(page)
        self.src = self.parse(text=text, label='form', attrs={
            'name': 'myform52'}, target='action')

    def jkdk4(self, session, header, data):
        page = session.post(self.src, data=self.form1, headers=self.headers4)
        text = self.encode(page=page)
        self.src = self.parse(text=text, label='form', attrs={
            'name': 'myform52'}, target='action')
    
    def jkdk5(self, session, header, data):

