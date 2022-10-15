from bs4 import BeautifulSoup
import time, re
import urllib.request
import ssl
import os
import re
import requests
import io

# picUrl = []
ssl._create_default_https_context = ssl._create_unverified_context


def scanpage(url):
    websiteurl = url
    t = time.time()
    n = 0
    html = urllib.request.urlopen(websiteurl).read()
    soup = BeautifulSoup(html)
    pageurls = soup.find_all("a", href=True)
    print("=======")
    picUrl = []
    picUrl.append(url)
    for links in pageurls:
        pic = links.get("href");
        if (pic.startswith("/m/")):
            picUrl.append("http://q.quantuwang1.com" + pic)
            # print("http://q.quantuwang1.com"+pic)
    return picUrl


def get_html(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
    }
    html = requests.get(url, headers=headers).text

    return html


def parse_html(html_text):
    picre = re.compile(r'[a-zA-z]+://[^\s]*\.jpg')  # 本正则式得到.jpg结尾的url
    pic_list = re.findall(picre, html_text)

    return pic_list


def download(file_path, pic_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
    }
    r = requests.get(pic_url, headers=headers)
    image_b = io.BytesIO(r.content).read()
    size = len(image_b)
    if size > 35000:
        with open(file_path, 'wb') as f:
            f.write(r.content)


def down(url):
    # 使用时修改url即可
    # url = 'http://q.quantuwang1.com/m/93b1407db2dc1c86.html'
    html_text = get_html(url)
    pic_list = parse_html(html_text)

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    date1 = soup.find("span")
    os.makedirs('/Users/kaidongwang/Desktop/林月儿/{0}/'.format(date1.text), exist_ok=True)  # 输出目录
    for pic_url in pic_list:
        file_name = pic_url.split('/')[-1]
        file_path = '/Users/kaidongwang/Desktop/林月儿/{0}/'.format(date1.text) + file_name

        download(file_path, pic_url)


def scanpage2(url):
    websiteurl = url
    html = urllib.request.urlopen(websiteurl).read()
    soup = BeautifulSoup(html)
    print("dada:", soup)
    pageurls = soup.find_all("a", href=True)
    print("=======")
    picUrl = []
    for links in pageurls:
        pic = links.get("href");
        if (pic.startswith("/m/")):
            picUrl.append("http://qq.quantuwang1.com" + pic)
            #
            # html = urllib.request.urlopen("http://q.quantuwang1.com"+pic).read()
            # soup = BeautifulSoup(html)
            # date1 = soup.find("span")
            # print(date1.text)
            #
    return picUrl


def ppp(url):
    picUrl = scanpage(url)
    print(len(picUrl))
    i = 1
    for url in picUrl[:len(picUrl) - 9]:
        down(url)
        print(str(i) + ':' + url)
        i = i + 1


if __name__ == '__main__':
    print("begin")
    pp = []
    pp = scanpage2("http://qq.quantuwang1.com/t/600bcd316870a0b5.html")
    print("网页多少个链接")
    print(len(pp))

    for p in pp[11:]:
        time.sleep(1)
        print(p)
        ppp(p)
        print("=================")
