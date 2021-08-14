# import required package
import requests
from bs4 import BeautifulSoup
import re


def encode(page):
    text = page.text.encode(page.encoding).decode(page.apparent_encoding)
    return text


def valid(page):
    if page.status_code == 200:
        return encode(page)
    else:
        return None


def strSearch(res: str, target):
    patterns = re.compile(res)
    outputs = patterns.search(target)
    return outputs


def parse(text, label: str, attrs: dict, target: str):
    bs4 = BeautifulSoup(text, 'lxml')
    body = bs4.find(label, attrs=attrs)
    return body.get(target)


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
}

login_url = r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
uid = '***'  # 用户号
upw = '***'  # 密码

data = {
    'uid': uid, 'upw': upw
}

page = requests.post(login_url, data=data, headers=headers)
text = encode(page)  # 得到登陆后的界面，但是还没有开始正式填写

output = strSearch(r'location="(.*?)"', text)

addr = output.group(1)
outputs = strSearch('ptopid=(.*)&sid=(.*)', addr)

ptopid = outputs.group(1)
sid = outputs.group(2)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': rf'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first6?ptopid={ptopid}&sid={sid}'
}
page = requests.get(addr, headers=headers)

text = valid(page)
if text is None:
    raise Exception

src = parse(text=text, label='iframe', attrs={
            'id': 'zzj_top_6s'},  target='src')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': src
}

outputs = strSearch(r'ptopid=(.*)&sid=(.*)', src)
ptopid = outputs.group(1)
sid = outputs.group(2)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': src,
    'Content-Type': 'application/x-www-form-urlencoded'
}

page = requests.get(src, headers=headers)
text = encode(page)

form = {
    'day6': 'b',
    'did': '1',
    'door': '',
    'men6': 'a',
    'ptopid': ptopid,
    'sid': sid
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': src,
}

src = parse(text=text, label='form', attrs={
            'name': 'myform52'}, target='action')

page = requests.post(src, data=form, headers=headers)
textt = encode(page=page)

form = {
    "myvs_1": "否",
    "myvs_2": "否",
    "myvs_3": "否",
    "myvs_4": "否",
    "myvs_5": "否",
    "myvs_6": "否",
    "myvs_7": "否",
    "myvs_8": "否",
    "myvs_9": "否",
    "myvs_10": "否",
    "myvs_11": "否",
    "myvs_12": "否",
    "myvs_13a": "41",
    "myvs_13b": "4108",
    "myvs_13c": "云台花园",
    "myvs_14": "否",
    "myvs_14b": "",
    "memo22": "[待定]",
    "did": "2",
    "door": "",
    "day6": "b",
    "men6": "a",
    "sheng6": "",
    "shi6": "",
    "fun3": "",
    "jingdu": "0.0000",
    "weidu": "0.0000",
    "ptopid": ptopid,
    "sid": sid
}

src = parse(text=text, label='form', attrs={
            'name': 'myform52'}, target='action')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': src,
    'Content-Type': 'application/x-www-form-urlencoded'
}

page = requests.post(src, data=form, headers=headers)  # 填表
text = encode(page)

bs4 = BeautifulSoup(text, 'lxml')
body = bs4.find('form', attrs={'name': 'myform52'})
text = body.getText()
if text.find('感谢'):
    print('好耶')
else:
    print('不好')
