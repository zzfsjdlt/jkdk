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


headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
}

login_url = r'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/login'
uid = '201924080230'  # 用户号
upw = 'PyfDsZ25nc*nQG'  # 密码

data = {
    'uid': uid, 'upw': upw
}
session = requests.Session()


page = session.post(login_url, data=data, headers=headers1)
text = encode(page)  # 得到登陆后的界面，但是还没有开始正式填写

output = strSearch(r'location="(.*?)"', text)

addr = output.group(1)
outputs = strSearch('ptopid=(.*)&sid=(.*)', addr)

ptopid = outputs.group(1)
sid = outputs.group(2)

headers2 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': rf'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first6?ptopid={ptopid}&sid={sid}'
}
page = session.get(addr, headers=headers2)

text = valid(page)
if text is None:
    raise Exception

src = parse(text=text, label='iframe', attrs={
            'id': 'zzj_top_6s'},  target='src')

outputs = strSearch(r'ptopid=(.*)&sid=(.*)', src)
ptopid = outputs.group(1)
sid = outputs.group(2)

headers3 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': src,
    'Content-Type': 'application/x-www-form-urlencoded'
}

page = session.get(src, headers=headers3)
text = encode(page)

form1 = {
    'day6': 'b',
    'did': '1',
    'door': '',
    'men6': 'a',
    'ptopid': ptopid,
    'sid': sid
}

headers4 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Referer': src,
}

src = parse(text=text, label='form', attrs={
            'name': 'myform52'}, target='action')

page = session.post(src, data=form1, headers=headers4)
text = encode(page=page)

form2 = {
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

page = session.post(src, data=form2, headers=headers)  # 填表
text = encode(page)

bs4 = BeautifulSoup(text, 'lxml')
body = bs4.find('form', attrs={'name': 'myform52'})
text = body.getText()
if text.find('感谢'):
    print('好耶')
else:
    print('不好')
