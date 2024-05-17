from bs4 import BeautifulSoup
import pyautogui as py
import time

with open("C:\\Users\\Windows 11\\Downloads\\Python\\auto.txt") as file:
    data = file.read()


    
soup = BeautifulSoup(data, 'html.parser')
div = soup.find('div', id='test-text')

spans = soup.find_all('span', {'class': 'test-char'})


for sn in spans:
    latter = sn.text
    py.write(latter, interval=0.30)



