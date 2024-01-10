import pyautogui
import time
import os
from shutil import rmtree

re_commit_mess = str(input('enter your commit message[+]'))
repo_url = str(input('enter your repo.Url[+]'))
commit_mess = f"\"{re_commit_mess}\""
# repo_url = "https://github.com/nerov103/example.git"

def github():
    step_0 = "git init"
    step_1 = "git add ."
    step_2 = f"git commit -m {commit_mess}" #enter your commit meassge
    step_3 = "git branch -M main"
    step_4 = f"git remote add origin {repo_url}" #enter your reponame
    step_5 = "git push -u -f origin main"

    clik = pyautogui.moveTo(800, 1000)
    pyautogui.click(clik)


    #stetment for git init command
    time.sleep(2)
    if os.access(".git", os.F_OK):
        print("exists .git")
    else:
        pyautogui.write(step_0)
        pyautogui.press('enter')
        time.sleep(0.5)
    #None error in git  add . command
    pyautogui.write(step_1)
    pyautogui.press('enter')
    time.sleep(0.5)
    #stetment for git commit meassge
    pyautogui.write(step_2)
    pyautogui.press('enter')
    time.sleep(0.5)
    # print(" plaess double quotation marks "" in the commit meassge")

    #eror handler in exists repo
    # root_path = "/home/backbox/For BackBox/Pyautogui/.git/config"
    # with open(os.path.join(root_path), 'r') as f:
    #     config_file_text_len = len(f.read())
    #     if int(config_file_text_len) <=92:
    #         print('repo. exists')
    #     if config_file_text_len >=92:
    #         pyautogui.write(step_3)
    #         pyautogui.press('enter')
    #         time.sleep(0.5)
    pyautogui.write(step_3)
    pyautogui.press('enter')
    time.sleep(0.5)

    pyautogui.write(step_4)
    pyautogui.press('enter')
    time.sleep(0.5)

    pyautogui.write(step_5)
    pyautogui.press('enter')
    time.sleep(0.5)




    print("=================================")
    print(step_0)
    print(step_1)
    print(step_2)
    print(step_3)
    print(step_4)

    mess = "Code Run in Successly"
    for i in mess:
        print(i, end="", flush=True)
        time.sleep(0.2)

    print("Success!")
# print(commit_mess)

# getdir = os.getcwd()
# ro_path = os.path.join(getdir, ".git")
# rmtree(ro_path)


github()
