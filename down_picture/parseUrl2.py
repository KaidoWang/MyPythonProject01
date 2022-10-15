from bs4 import BeautifulSoup
import urllib.request




def scanpage2(url):
  websiteurl=url
  html=urllib.request.urlopen(websiteurl).read()
  soup=BeautifulSoup(html)
  print("dada:",soup)
  pageurls=soup.find_all("a",href=True)
  print("=======")
  picUrl = []
  for links in pageurls:
    pic = links.get("href");
    if(pic.startswith("/m/")):
      picUrl.append("http://q.quantuwang1.com"+pic)
  return picUrl



if __name__ == '__main__':
  picUrl=scanpage2("http://q.quantuwang1.com/t/15c3767f8a07de21.html")
  print(len(picUrl))
  i = 1
  for url in picUrl:
    print(str(i) + ':' + url)
    i = i + 1
