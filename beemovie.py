import time 
import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 


driver = webdriver.Chrome('D:/Personal/Programs/chromedriver')

def goes_to_whatsapp(target):
    """
    target: name of the contact and/or group on whatsapp

    The target MUST be visibile, otherwise the program will wait until the contact is visible
    
    TODO: get the contact from the search option

    """
    driver.get("https://web.whatsapp.com/") 
    wait = WebDriverWait(driver, 600)
    time.sleep(5)


    # Clicks on the user base on the  contact/group name
    x_arg = f"//span[contains(@title,\"{target}\")]"
    group_title = wait.until(EC.presence_of_element_located(( By.XPATH, x_arg))) 
    group_title.click() 


def type_data_on_chat(movie='bee'):
    
    """
    txt: text to be sent, word by word, by default it will be the Bee Movie script

    """
    root_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"]'
    inp_xpath = f'{root_xpath}[@data-tab="1"][@dir="ltr"][@spellcheck="true"]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(2)

    if movie == 'bee':
        
        ROOT = 'https://gist.githubusercontent.com/The5heepDev/a15539b297a7862af4f12ce07fee6bb7/raw/'
        URL = f'{ROOT}/7164813a9b8d0a3b2dcffd5b80005f1967887475/entire_bee_movie_script'

        response = requests.get(URL).text
    else: 
        URL = f'https://www.imsdb.com/scripts/{movie}.html' 
        html = requests.get(URL).text
        soup = BS(html, "html.parser")
        soup = str(soup.find_all("pre"))
        soup = soup.replace("<b>", "")
        soup = soup.replace("</b>", "")
        soup = soup.replace("</pre>]", "")
        soup = soup.rstrip('\r\n')
        response = soup

    response = response.split(" ")
        
    for word in response:
        input_box.send_keys(word + Keys.ENTER)
        time.sleep(1)




goes_to_whatsapp('Ideas')
type_data_on_chat()