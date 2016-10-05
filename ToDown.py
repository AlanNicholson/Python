import threading
import urllib.request
import os
import re
from fake_useragent import UserAgent
from selenium import webdriver
import time
# urllib.request.urlretrieve(url, full_name
ua = UserAgent()
a = input('Enter keywords: ')
q = input('Enter Quality: ')
T = input('Enter time in seconds: ')
r = input('Enter site: ')
#browser = webdriver.Chrome('C:/Users/A/Desktop/New folder/chromedriver.exe')
#R=browser.get('https://pirateproxy.red/')
R = urllib.request.Request('https://pirateproxy.red/user/'+r,
   data=None,headers={'User-Agent': ua.random})

page1 = urllib.request.urlopen(R).read()
page1D = page1.decode('utf-8')
#print(page1D)
b=str('&dn='+a)
A = re.search(b,page1D)
while A == None:
    time.sleep(int(T))
    A = re.search(b,page1D)
if A != None:
    aS = A.start() - 200
    aF = A.end() + 400
    page1D = page1D[aS:aF]
    A = re.search('magnet:',page1D)
    B = re.search('" title',page1D)
    aS =A.start()
    aF =B.start()
    page1D = page1D[aS:aF]
    C = re.search(q,page1D)
    while C == None:
        time.sleep(int(T))
    if C != None:
        print(page1D)
        os.startfile(str(page1D))
        exit()

    
