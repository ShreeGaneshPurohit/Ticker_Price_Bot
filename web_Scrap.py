from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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