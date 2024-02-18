import requests
import socket
import json
from colorama import Fore
from math import sqrt

#used to tasting this tools use this domin name
#example.com

url = str(input("Https://www."))

#red color text use by colorama.Fore
error_mes = Fore.RED+"please enter your valid domain address!"

#user input error handling
try:
    if sqrt(int(url)):
        print(error_mes)
except ValueError:
    try:
        send_request = requests.get("Https://"+url)
    except requests.exceptions.ConnectionError:
        print(error_mes)
        exit()
    
    #use to python socket programming
    get_ip = socket.gethostbyname(url)

    #use to ipinfo.io website
    get_more_detel = requests.get("https://ipinfo.io/"+get_ip+"/json")

    #use to python json Module
    get_more_detel = json.loads(get_more_detel.text)

    #print the target website header info
    print(send_request.headers)

    #print the terget domin name to ip
    print("www."+url+" Ip Address> "+get_ip)
    
    #give you more info your target url use www.ipinfo.io website useing
    print(f"This www.{str(url)} more info: ",get_more_detel)


'''
all code wite by mr.pydor
ima a boring coder!!
'''