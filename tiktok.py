import http.client
import json

print("""
######## ##     ##  ######  ##    ## ######## ########      ######## #### ##    ## ########  #######  ##    ## 
##       ##     ## ##    ## ##   ##  ##       ##     ##        ##     ##  ##   ##     ##    ##     ## ##   ##  
##       ##     ## ##       ##  ##   ##       ##     ##        ##     ##  ##  ##      ##    ##     ## ##  ##   
######   ##     ## ##       #####    ######   ########         ##     ##  #####       ##    ##     ## #####    
##       ##     ## ##       ##  ##   ##       ##   ##          ##     ##  ##  ##      ##    ##     ## ##  ##   
##       ##     ## ##    ## ##   ##  ##       ##    ##         ##     ##  ##   ##     ##    ##     ## ##   ##  
##        #######   ######  ##    ## ######## ##     ##        ##    #### ##    ##    ##     #######  ##    ##


  Discord ┃ https://discord.gg/desk
  
  Youtube ┃ https://www.youtube.com/c/DeskCommunity     
  
  
  """)
  
id = input("Introduza o id do video")

sdoakd = "Denúncia enviada com sucesso by Desk Client"

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
  'Referer': f'https://www.tiktok.com/foryou?is_copy_url=1&is_from_webapp=v1&item_id={id}',
  'Connection': 'keep-alive',
  'TE': 'trailers'
}

while True:
    conn.request("POST", "/node/report/reasons_put?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6990406517787018758&region=DK&priority_region=&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1366&screen_height=768&browser_language=da&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows)&browser_online=true&app_language=en&timezone_name=Europe%252FCopenhagen", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print("Denúncia enviada com sucesso by Desk Client")