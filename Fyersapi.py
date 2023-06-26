from fyers_api import accessToken ,fyersModel
def api(auth_code):
    client_id = "24I95P3FDW-100"
    secret_key = "R1KWLP3X9W"
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
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token, log_path='J:\Price_Bot\Ticker_Price_Bot\logs')
    data = {"symbols":"MCX:SILVER23JULFUT"}
    fyers.quotes(data)
    print("Data Feched")