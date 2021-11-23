
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import action_chains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import gspread
import warnings
import platform

warnings.filterwarnings('ignore')

sysOS = platform.system()
options = webdriver.ChromeOptions()
if (sysOS == 'Windows'):
    _chromedriver = '../driver/window_chromedriver' #chromedriver 위치에 따라 변경해야 함
    print('Windows')
else:
    _chromedriver = '../driver/chromedriver' #chromedriver 위치에 따라 변경해야 함    
    print('MacOS')

driver = webdriver.Chrome(_chromedriver)
driver.get('https://testnet.binance.org/faucet-smart')

def faucet_start():    
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="url"]').send_keys('0x1914627a35cf0822714f79D2584b278F92fC8be5')
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[1]/span[1]/button').click()
    action = ActionChains(driver)
    submenu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div[2]/div/div[1]/span[1]/ul/li/a')))
    action.move_to_element(submenu).click().perform()
    time.sleep(6)
    driver.quit()

print('good~good~good')