import auth_code_fyers
import Fyersapi
import readingdfiles
import web_Scrap
import telegram_bot


#Step-1 Gen Auth Code

url = auth_code_fyers.autgen()
auth_code = web_Scrap.webscrap(url)
#set auth_code
Fyersapi.api(auth_code)

#Step -2 Aet Authcode and Retrive price

msg = readingdfiles.read()

telegram_bot.sendmsg(msg)

#Step - 