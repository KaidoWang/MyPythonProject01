from bs4 import BeautifulSoup
import time, re
import urllib.request
import ssl
import os
import re
import requests
import io

ssl._create_default_https_context = ssl._create_unverified_context

"""
    2023.07.29 编写的python脚本 用于下载图片 用在 https://www.xrmn02.cc/XiuRen/ 
"""


class MyCount:
    jpg_count = 1


def scanpage(url):
    print("dada")
    picUrls = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    websiteurl = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(websiteurl).read()
    soup = BeautifulSoup(html)
    pageurls = soup.find_all("a", href=True)
    for links in pageurls:
        pic = links.get("href")
        if (pic.startswith("/XiuRen/2023/" + url.split("/")[5].split('.')[0])):
            picUrl = "https://www.xrmn02.cc" + pic
            if picUrl not in picUrls:
                picUrls.append(picUrl)
    return picUrls


def download(file_path, pic_url):
    print("开始下载")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 ",
    }
    r = requests.get(pic_url, headers=headers)
    with open(file_path, 'wb') as f:
        f.write(r.content)


def down(url):
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}
    url = urllib.request.Request(url=url, headers=headers)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html)
    imgs = soup.find_all("img")
    pic_list = []
    for img in imgs:
        src = img.get('src')
        if src.startswith('/upload'):
            pic_list.append("https://www.xrmn02.cc" + img.get('src'))

    os.makedirs('/Users/kaidongwang/Desktop/秀人/', exist_ok=True)  # 输出目录

    for pic_url in pic_list:
        file_name = str(MyCount.jpg_count) + ".jpg"
        file_path = '/Users/kaidongwang/Desktop/秀人/' + file_name
        download(file_path, pic_url)
        MyCount.jpg_count += 1


# master
if __name__ == '__main__':
    pic = scanpage("https://www.xrmn02.cc/XiuRen/2023/202313518.html")

    i = 1
    for url in pic:
        time.sleep(3)
        down(url)
        i = i + 1
