from datetime import datetime
import requests
import time
import urllib
import hashlib
import html

## telegram
tg_token     = "your_bot_token" ## telegram bot
tg_chat_id = "telegram_group_id"
tg_chat_type  = "HTML" # Markdown / HTML, default=Markdown but html more smooth than markdown
coc_clan_id = "coc_clan_id"

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer <coc_developer_api>'
}


## Previous state
previous_state = None

while True:
    try:
        # Get JSON war_data
        response = requests.get('https://api.clashofclans.com/v1/clans/%{coc_clan_id}/currentwar', headers=headers)
        war_json = response.json()
        # Get important JSON data
        warValue, teamSize, opponentValue, clanValue, startValue = war_json['state'], war_json['teamSize'], war_json['opponent']['name'], war_json['clan']['name'], war_json['startTime']

        convert_starTimestamp = datetime.strptime(startValue, "%Y%m%dT%H%M%S.%fZ")
        wib_time = datetime.strptime(convert_starTimestamp.strftime("%H:%M:%S"), "%H:%M:%S") - datetime.strptime("15:00:00", "%H:%M:%S")
        # Get members participating in the war
        members_list = '\n'.join([f"- {member['name']}" for member in war_json['clan']['members']])

        # Check if the state has changed
        if warValue != previous_state:
            # Handle different states
            if warValue == "preparation":
                # Create and send preparation message
                tg_messages = f"""
                War has been declared against <b dir='rtl'>{opponentValue}</b>\n\n#PreparationDAY
                """
                url_encode = urllib.parse.quote_plus(str(tg_messages))
                response = requests.post(f"https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={tg_chat_id}&text={url_encode}&parse_mode={tg_chat_type}")
                ## Debug
                if response.ok:
                    print("Preparation message sent successfully!")
                else:
                    print(f"Failed to send preparation message. Status code: {response.status_code}, Response: {response.text}")
            elif warValue == "inWar":
                # Create and send inWar message
                tg_messages = f"""
                Today is a Battle Day 🛡️⚔️ \n\nMember participating (<b>{teamSize}</b>):\n{html.escape(members_list)} \n\nDon't forget to launch your attacks against <b dir='rtl'>{opponentValue}</b> before the battle ends.
                """
                url_encode = urllib.parse.quote_plus(str(tg_messages))
                response = requests.post(f"https://api.telegram.org/bot{tg_token}/sendMessage?chat_id={tg_chat_id}&text={url_encode}&parse_mode={tg_chat_type}")
                ## Debug
                if response.ok:
                    print("InWar message sent successfully!")
                else:
                    print(f"Failed to send inWar message. Status code: {response.status_code}, Response: {response.text}")

            # Update previous state
            previous_state = warValue

        # Wait for 30 seconds before checking again
        time.sleep(30)
    except Exception as e:
        print("Error:", e)
