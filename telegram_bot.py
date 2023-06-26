import requests

def sendmsg(msg=10):
   
    

    telegram_auth_token = "6069169314:AAExM_ZNhWKfU5FtDaEYNGjzkNOlW0c0nSo" # Authentication token provide
    telegram_group_id = "-1001920376344"  # Telegram group name
    
    def send_msg_on_telegram (message):
        telegram_api_url = f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id={telegram_group_id}&text={message}"
        tel_resp = requests.get(telegram_api_url)

        if tel_resp.status_code == 200:
            print ("INFO : Nodification has been sent on Telegram")
        else:
            print ("ERROR: Could not send Message")

    #Function Call
    send_msg_on_telegram(msg)


    