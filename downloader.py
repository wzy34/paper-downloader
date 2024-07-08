import os
import requests
import random
from bs4 import BeautifulSoup

subject = input("学科：(仅支持physics与math)")
year = input("年份：")
codes = {"math":"Mathematics%20(9709)","physics":"Physics%20(9702)"}
url = "https://papers.gceguide.net/A%20Levels/" + codes[subject] + "/" + year
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15"
    ]
header = random.choice(user_agent_list)
headers = {
    'User-Agent':'Mozilla/5.0',
    'Content-Type':'application/json',
    'method':'GET',
    'Accept':'application/vnd.github.cloak-preview'
    }
headers['User-Agent'] = header
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
a_tags = soup.find_all('a')
file_path = "C:\\Users\\GodWu\\Desktop\\" + codes[subject].replace("%20", "") + "\\" + year
pdf_links = []
if not os.path.exists(file_path):
    os.makedirs(file_path)
for a_tag in a_tags:
    href = a_tag.get('href')
    if href.endswith('.pdf'):
        pdf_links.append(href)
for link in pdf_links:
    response = requests.get(url+"/"+link)
    filename = link.split('/')[-1]
    filepath = os.path.join(file_path, filename)
    with open(filepath, 'wb') as f:
        f.write(response.content)
    print(f'{filename} 下载完成')