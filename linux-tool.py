import os
import fade
import clear
import colorama
from colorama import Fore

ascii_artt = '''
     
         _nnnn_
        dGGGGMMb
       @p~qp~~qMb
       M|@||@) M|
       @,----.JM|
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMP|   .'
     `-'       `--' 
     WORKING ONLY ON LINUX SYSTEM / WSL
     '''
clear.clear()
print(fade.water(ascii_artt))
choix = Fore.RED+"Your choice --> "
print()
print(Fore.RED+"_______________________________________________________________________")
print(Fore.RED+'[1]Check if a site has SQL vulnerabilities (via sqlmap)')
print(Fore.RED+'[2]scan the ports of an ip address (via autorecon)')
print(Fore.RED+'[3]scan the ports of an ip adress (via nmap)')
print(Fore.RED+'[4]Install all the tools needed for this multitool (very important!)')
print(Fore.RED+'[5]Exit') 
print("_______________________________________________________________________")
choicee = input(choix)
if choicee == '1':
    url = input(Fore.MAGENTA+"Enter the url --> ")
    os.system(f"sqlmap -u {url} --batch")  # sqlmap commands to check if a site has sql vuln , with  no input interaction like "Y"
    input(Fore.MAGENTA+"Scan finish...")
    os.system("python3 linux-tool.py")
if choicee == '2':
          url1 = input(Fore.MAGENTA+"Enter the ip to scan with autorecon --> ")
          os.system(f"sudo autorecon {url1}") # i use sudo (super do) because autorecon need root privilege ton scan udp port
          input(Fore.MAGENTA+"Scan finish...")
          os.system("python3 linux-tool.py")
if choicee =='3':
          url2 = input(Fore.MAGENTA+"Enter the ip to scan with nmap --> ")
          os.system(f"nmap {url2}")
          input(Fore.MAGENTA+"Scan finish...")
          os.system("python3 linux-tool.py")
if choicee == '4':
          os.system("sudo apt install autorecon && sudo apt install nmap && sudo apt install sqlmap") # I did this because on WSL, you have to install the tools manually 
          os.system("python3 linux-tool.py")
if choicee == '5':
          clear.clear()
          exit