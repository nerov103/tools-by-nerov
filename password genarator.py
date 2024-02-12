from random import sample
from colorama import Fore, Style

error = "please enter your password length!"
chr_list = "aqwehbnotpc"
chr_up = chr_list.upper()
num_list = "0123459"
symple = "!@#$%^&*()_+}{|\":?><,/;\][=-]}"
password_lenthd = str(input(Fore.GREEN + "enter your password len> "))
password = ""
password_stor = []
if password_lenthd=="q":
    exit()
else:
    for i in chr_list:
        for n in num_list:
            for s in symple:
                for p in chr_up:
                    password_stor.append(i)
                    password_stor.append(n)
                    password_stor.append(s)
                    password_stor.append(p)

try:
    get_password = sample(password_stor, int(password_lenthd))
    print(Fore.LIGHTRED_EX, Style.BRIGHT + "".join(get_password))
except ValueError:
    print(error)
except NameError:
    print(error)
    


#all code write by mr.pydor

