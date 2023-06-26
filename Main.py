# Authcode Library
from fyers_api import accessToken

#Web_Scraping 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#for Datafetching 
from fyers_api import accessToken ,fyersModel

#importing for delay 
from time import sleep

import readingdfiles

import telegram_bot


def autgen(client_id,secret_key):    
    redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
    response_type = "code"
    state = "sample_state"

    session=accessToken.SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri=redirect_uri, 
        response_type=response_type
    )

    response = session.generate_authcode()
    

    return response


def webscrap(url) :
    driver = webdriver.Chrome('/path/to/chromedriver')

    driver.get(url)


    element = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "s_auth_code"))
    )

    auth_key = element.text
    print(auth_key)

    driver.quit()
    return(auth_key)

def api(client_id,secret_key,auth_code,delay):
    
    redirect_uri = "https://trade.fyers.in/api-login/redirect-uri/index.html"
    response_type = "code"
    grant_type = "authorization_code"


    session = accessToken.SessionModel(
        client_id=client_id,
        secret_key=secret_key, 
        redirect_uri=redirect_uri, 
        response_type=response_type, 
        grant_type=grant_type
    )
    session.set_token(auth_code)
    response = session.generate_token()
    print(response)
    access_token = response['access_token']


    #Geting Script info 
    log_path_ = "J:\Price_Bot\Ticker_Price_Bot\logs"
    fyers = fyersModel.FyersModel(client_id = client_id, token = access_token, log_path = log_path_)
   
    i =0
    scrip_List = [{"symbols":"MCX:SILVER23JULFUT"},{"symbols":"MCX:ZINCMINI23JULFUT"},{"symbols":"MCX:CRUDEOIL23JULFUT"}]
    while (i<2):
        sleep(delay)
        telegram_bot.sendmsg(msg="Price Update....")
        for j in range(0,3):
            data = scrip_List[j]
            fyers.quotes(data)
            print("Data Feched")
            j = j+1
            msg = readingdfiles.read()

            telegram_bot.sendmsg(msg)
        i = i + 1

if __name__ == "__main__" :
    
    #Setting Client Credentials
     
    client_id = "24I95P3FDW-100"
    secret_key = "R1KWLP3X9W"

    #Genrating Authentication Code Webpage Url

    url = autgen(client_id,secret_key)
    auth_code = webscrap(url)

    #Calling Fetch Api
    api(client_id,secret_key,auth_code,delay=10)

