from bs4 import BeautifulSoup
import time, re
import urllib.request
import ssl
import os
import re
import requests
import io

ssl._create_default_https_context = ssl._create_unverified_context

def xiaohongshu(url):
    websiteurl = url
    html = urllib.request.urlopen(websiteurl).read()
    soup = BeautifulSoup(html)
    print(soup)


if __name__ == '__main__':
    xiaohongshu("https://www.xiaohongshu.com/user/profile/583904ed82ec391587171401?xhsshare=CopyLink&appuid=5561f042a75c951f6bd845c5&apptime=1676791971")
