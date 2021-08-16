import bs4

with open('./test3.html', 'r') as f:
    text = f.read()

bs4 = bs4.BeautifulSoup(text, 'lxml')
body = bs4.find('div', attrs={'id': 'bak_0'})
text = body.text
if text.find('今日您已经填报过了'):
    print('好耶')
