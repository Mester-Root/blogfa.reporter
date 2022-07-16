# !/usr/bin/python
# report blogfa
#-------------------------------------------
import os,sys,time,random
from bs4 import BeautifulSoup
try:
    import requests
except:
    os.system('pip install requests')
    import requests
try:
    from colorama import *
except:
    os.system('pip install colorama')
    import colorama
try:
    import pyuseragents
except:
    os.system('pip install pyuseragents')
    import pyuseragents
try:
    from pyfiglet import *
except:
    os.system('pip install pyfiglet')
    from pyfiglet import *
try:
    import datetime
except:
    os.system('pip install datetime')
    import datetime

#------------------------------------------
print()
#-------
try:
    os.system('clear')
except:
    os.system('cls')
#--------
print()
time.sleep(2)
#----------------------------------
logo = ['BLOGFA','REPORTER','REPORT','FILTERIMG','RePoRtEr','bLoGfA','blogfa . com']

bnr = (random.choice(logo))
banner = (figlet_format(bnr))
print(Fore.YELLOW+'')
print(banner)
time.sleep(1)
target = input(Fore.GREEN+'\n\nenter target blogfa'+Fore.WHITE+' _> '+Fore.RED+'')
print()
try:
    ul = requests.get(f'http://{target}.blogfa.com')
    if ul.status_code == 200:
        print(f'\n\033[31m[+] \033[36mpage found => \033[0m@\033[92m{target}\n')
    else:
        print(f'\n\033[31m[!] \033[35mpage not found => \033[0m@\033[92m{target}\n')
        time.sleep(1)
        try:
            exit(5)
        except:
            sys.exit()
except:
    time.sleep(1)
    print(f'\n\033[31m[!] \033[35mserver offline\n')
    time.sleep(1)
    try:
        exit(5)
    except:
        sys.exit()
time.sleep(1)
num = input(Fore.BLUE+'NUMBER FOR |REPORT| [#]> ')
print()
time.sleep(1)
date = (datetime.datetime.today())
print(Fore.BLUE+f'\n\n\n[#]: \033[36m[{date}]'+Fore.RED+' _ '+Fore.GREEN+'>_<\n\n\n')
#--------------------------------------------


# http://blogfa.com/WebResource.axd?d=pynGkmcFUV13He1Qd6_TZKA1MaRrNfdTMjHE8DOzzEG8JtXFKTduVZcv4GbHcdQyx6NxzA2&t=637729620413207958&

#----

head = {'Host':'http://blogfa.com','Content-Type':'application/x-www-form-urlencoded charset=utf-8','User-Agent': pyuseragents.random(),'content-encoding':'gzip','content-length':'6007','content_type':'application/x-javascript','date':'Sat, 18 Jun 2022 16','expires':'Sun, 18 Jun 2023 14','last-modified':'Fri, 19 Nov 2021 23','nel':'{"success_fraction"','report-to':'{"endpoints"','server':'cloudflare','vary':'Accept-Encoding','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate, br','Content-Type':'application/x-www-form-urlencoded','Content-Length': '175','Origin': 'https://blogfa.com','Connection': 'keep-alive','Referer': 'https://blogfa.com/desktop/login.aspx?r=637860193478105692','Upgrade-Insecure-Requests': '1','Pragma': 'no-cache','Cache-Control': 'no-cache'}


# ------------------------------------------
url = requests.get('http://blogfa.com/report-abuse/').text

testing = BeautifulSoup(url, 'html.parser')
test = testing.find('input')['value']

data = {'_tt': test,'usrid': target,'submit':'ارسال پیام','ups': None}

json = {'lastreport': target}

number = 0
numb = int(num)

while number != numb:
    try:
        requests.post('http://blogfa.com/report-abuse/',headers=head,json=json,data=data)
        time.sleep(2.5)
        print(Fore.BLUE+f'\n[REPORT:~#]'+Fore.GREEN+' SENTED'+Fore.YELLOW+' ~>'+Fore.RED+f' [{target}]\n')
    except:
        time.sleep(2.5)
        print(Fore.RED+'\nNOT !> SENTRD\n')
    numb = (numb-1)
# --------------------------------------
