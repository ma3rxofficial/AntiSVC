import requests
import time
import random
import berserk

def proxy(user, password):
    n = requests.post("https://mskchess.ru/login", {"username": user, "password" : password}, headers={"X-Requested-With" : "XMLHttpRequest", "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/69.0"}, timeout=2)
    return n

def create_session(user, password):
    return proxy(user, password).cookies

def create_token(s):
    r = requests.post("https://mskchess.ru/account/oauth/token/create", data={"description" : str(random.randint(100, 100000000)), "scopes[]" : "msg:write"}, cookies=s, headers = {"Origin" : "https://mskchess.ru/", "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/69.0"}).text
    try:
     token = r.split("<code>")[1].split("</code>")[0]
    except: return r

    return token

for j in range(100):
  i = random.randint(1000, 100000000)
  try:
   r = requests.post(
     "https://mskchess.ru/signup",
     {"username" : "ma3rx"+str(i), "password" : "test"+str(i), "email" : "ma3rx"+str(i)+"@gmail.com", "fp" : "cff8bb5a86334203b11a55646a34e3b8", "agreement.assistance" : "true", "agreement.nice" : "true", "agreement.account" : "true", "agreement.policy" : "true"},
   )

   print("Account    "+"ma3rx"+str(i))
   print("Password   "+"test"+str(i))

   k = create_token(create_session("ma3rx"+str(i), "test"+str(i)))
   print("Token      "+str(k))
   print()

   open("tokens", "a").write(k+"\n")
  except Exception as e: e = None
