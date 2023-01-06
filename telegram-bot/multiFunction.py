import requests
import urllib
from datetime import datetime

# global variable
token     = "5930317051%3AAAEKT1asXjV43Fpc5hlVUMqeuxPjI_mEHdw"
messageID = "-503556289"
typeText  = "HTML" # Markdown / HTML, default=Markdown but html more smooth than markdown
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SAMSUNG-SM-N900A Build/LRX21V)",
}

    
def doaPagi():
    Text = """ 
<b>[ DOA PAGI ]</b>

Reminding for all personel shifting in gti to join weekly briefing on 8.30 am.

Link Teams:
https://bit.ly/3ay1psM
Update Form:
https://forms.gle/vw8XvJakEk3P3MiF7

Ops:
@Btech_Openstack
@Btech_Instance
@btech_k8s """

    ParsedRestultText = urllib.parse.quote_plus(Text)
    response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={messageID}&text={ParsedRestultText}&parse_mode={typeText}", headers=headers)
    # log
    now = datetime.now()
    wib = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('/home/ajinha/workdir/python/botTelegram/bribot/bot.log', 'a') as f:
        print(wib, '-',response.text, file=f)    

def dailySync():
    Text = """ 
<b>[ Daily Sync ]</b>

Temen2 ops BRI yang sedang shift, mohon untuk bergabung di internal daily sync.

Link Teams:
https://s.id/btech-bri-ops-daily-sync  

Ops:
@Btech_Openstack
@Btech_Instance
@btech_k8s """


    ParsedRestultText = urllib.parse.quote_plus(Text)
    response = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={messageID}&text={ParsedRestultText}&parse_mode={typeText}", headers=headers)
    # log
    now = datetime.now()
    wib = now.strftime("%d/%m/%Y %H:%M:%S")
    with open('/home/ajinha/workdir/python/botTelegram/bribot/bot.log', 'a') as f:
        print(wib, '-', response.text, file=f)

if __name__ == "__main__":    
    doaPagi()
    dailySync()
