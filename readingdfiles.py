from datetime import datetime,date
import pytz



def read():
    with open(f"J:\Price_Bot\Ticker_Price_Bot\logs\{date.today()}.txt",'r') as file:
        for line in file:
            grade_data = line.strip().split(',')
        lines = file.read().splitlines()
        if(len(lines) > 1 ):
            line = lines[len(lines)-1]
            grade_data = line.strip().split(',')
        


    s_name=grade_data[23]
    s_Cmp = grade_data[19]
    s_High = grade_data[17]
    s_Low = grade_data[18]

    IST = pytz. timezone('Asia/Kolkata')        # Selecting Timezone as Indian Standard Time
    raw_TS = datetime.now(IST)
    curr_date = raw_TS.strftime("%d-%m-%Y")
    curr_time = raw_TS.strftime("%H:%M:%S") #24 HR

    msg = f"Price of ={s_name[15:]}\nCMP ={s_Cmp[6:]} \nHigh ={s_High[14:]}\nLow ={s_Low[13:]} \n\nPrice @ {curr_date} at {curr_time}"
    
    return msg

