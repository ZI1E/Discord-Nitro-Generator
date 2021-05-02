import random, string
import webbrowser
import time
import requests
from colorama import init, Fore


time.sleep(2)
print(Fore.BLUE + "Created By ZIE")
print(Fore.BLUE + "[+]ZIE Nitro Gen - Cheack")
time.sleep(0.3)

num=input('Input How Many Codes to Generate and Check: ')

f = open("Nitro Codes.txt","w", encoding='utf-8')

print(Fore.MAGENTA + "Wait, Generating for you!")
      
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()

#====================[Checker]====================#
#=====================[Enjoy]=====================#
#====================[Checker]====================#


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Fore.GREEN + " Valid | {} ".format(line.strip("\n")))
        else:
        	print(Fore.RED + " Not Working | {} ".format(line.strip("\n")))
input(Fore.BLUE + "The end! Press Enter to close the program.")