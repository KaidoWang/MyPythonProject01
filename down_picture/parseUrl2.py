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

# 1:http://q.quantuwang1.com/m/5262747260cd23c7.html
# 2:http://q.quantuwang1.com/m/7eb990eb10977031.html
# 3:http://q.quantuwang1.com/m/6099159bfe2e3796.html
# 4:http://q.quantuwang1.com/m/0f0348514c775d72.html
# 5:http://q.quantuwang1.com/m/a72c3c81ead15492.html
# 6:http://q.quantuwang1.com/m/acaf60edb85eccb6.html
# 7:http://q.quantuwang1.com/m/85433be8d22c022a.html
# 8:http://q.quantuwang1.com/m/caa43feb280aadc5.html
# 9:http://q.quantuwang1.com/m/e89fa5f09d2ed4fc.html
# 10:http://q.quantuwang1.com/m/43eeab0c79d5a4ff.html
# 11:http://q.quantuwang1.com/m/92f963a843055a6e.html
# 12:http://q.quantuwang1.com/m/eb8e2b87ebda0cce.html
# 13:http://q.quantuwang1.com/m/60c8215328df1ec9.html
# 14:http://q.quantuwang1.com/m/5bbc250329b453eb.html
# 15:http://q.quantuwang1.com/m/96398d340ae0610e.html
# 16:http://q.quantuwang1.com/m/ca72583890319476.html
# 17:http://q.quantuwang1.com/m/a25a2147b5329a4d.html
# 18:http://q.quantuwang1.com/m/4d069ebd4c9b3c2e.html
# 19:http://q.quantuwang1.com/m/0153a9355d4441dd.html
# 20:http://q.quantuwang1.com/m/297768209bcc525a.html
# 21:http://q.quantuwang1.com/m/ecc8d5ccf10b658a.html
# 22:http://q.quantuwang1.com/m/99bba620d344ef73.html