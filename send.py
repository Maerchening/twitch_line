import requests
from json import loads
import time

client_id = ""
client_secret = ""

Twitch_ID = ''
ment = "방송켰다~ 당장 달려와~"

oauth_key = requests.post(
        "https://id.twitch.tv/oauth2/token?client_id=" + client_id + "&client_secret=" + client_secret + "&grant_type=client_credentials")
access_token = loads(oauth_key.text)["access_token"]
token_type = 'Bearer '
authorization = token_type + access_token
check = False

twitch_headers = {'client-id': client_id, 'Authorization': authorization}
response_channel = requests.get('https://api.twitch.tv/helix/streams?user_login=' + Twitch_ID,
                                headers=twitch_headers)

while True:
    try:
        TARGET_URL = 'https://notify-api.line.me/api/notify'
        token = ''
        headers={
            'Authorization': 'Bearer ' + token
        }
        data = {
            'message': ment + '\nhttps://www.twitch.tv/' + Twitch_ID
        }
        if loads(response_channel.text)['data'][0]['type'] == 'live' and check == False:
            response = requests.post(TARGET_URL, headers=headers, data=data)
            check = True

    except Exception as ex:
        print(ex)
        check = False

    time.sleep(10)
