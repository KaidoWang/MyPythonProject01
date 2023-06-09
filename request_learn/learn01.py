import requests

if __name__ == '__main__':
    myobj = {"fname": "RUNOOB", "lname": "Boy"}
    res = requests.post('https://www.runoob.com/try/ajax/demo_post2.php', params= myobj,data=myobj)
    print(res.url)
    print(res.text)