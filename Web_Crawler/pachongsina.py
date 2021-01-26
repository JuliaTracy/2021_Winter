import requests
from bs4 import BeautifulSoup
newsurl='http://news.sina.com.cn/china/'
res=requests.get(newsurl)
res.encoding='utf-8'
#print(res.text)
'''html_sample=' \
<html> \
 <body> \
 <h1 id="title">Hello World</h1> \
 <a href="#" class="link">This is link1</a> \
 <a href="# link2" class="link">This is link2</a> \
 </body> \
 </html>'
'''
soup=BeautifulSoup(res.text, 'html.parser')
i=0
for news in soup.select('.right-content'):
    while i<=100:
        if (len(news.select('li'))>0):
            li=news.select('li')[i].text
            a=news.select('a')[i]['href']
            print(li,a)
        i=i+1
