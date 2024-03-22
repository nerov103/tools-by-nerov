import pyautogui
import time

comments = ["Hi ima Mr.Pydor","Just commenting for fun","Checking my python comment bot","Just for fun","I am just checking my python skill","python is awesome","I am a Boring programmer", "How Are You?", "github/nerov103"]

time.sleep(5)

for i in range(100):
    pyautogui.typewrite(comments[i%len(comments)])
    pyautogui.typewrite("\n")
    time.sleep(2)
