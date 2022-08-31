import http.client
import json
from termcolor import colored

print(colored("d8888b. d88888b .d8888. db   dD  .o88b. db      d888888b d88888b d8b   db d888888b ㅤㅤㅤdb    db d8888b. ", 'green'))
print(colored("88  `8D 88'     88'  YP 88 ,8P' d8P  Y8 88        `88'   88'     888o  88 `~~88~~' ㅤㅤㅤ88    88 VP  `8D ", 'green'))
print(colored("88   88 88ooooo `8bo.   88,8P   8P      88         88    88ooooo 88V8o 88    88    ㅤㅤㅤY8    8P   oooY' ", 'green'))
print(colored("88   88 88~~~~~   `Y8b. 88`8b   8b      88         88    88~~~~~ 88 V8o88    88    ㅤㅤㅤ`8b  d8'   ~~~b. ", 'green'))
print(colored("88  .8D 88.     db   8D 88 `88. Y8b  d8 88booo.   .88.   88.     88  V888    88     ㅤㅤㅤ`8bd8'  db   8D ", 'green'))
print(colored("Y8888D' Y88888P `8888Y' YP   YD  `Y88P' Y88888P Y888888P Y88888P VP   V8P    YP       ㅤㅤㅤ YP    Y8888P' ", 'green'))
print("")
print("")
print("")
print(colored("by barbosa and sny666 // discord.gg/desk", 'red'))

id = input("Introduza o id do video ")
                

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
    print(colored("Denúncia enviada com sucesso by Desk Client v3' ", 'magenta'))
