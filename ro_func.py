
from selenium import webdriver
from selenium.webdriver import ActionChains
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
packed_extension_path = '../crx/Metamask.crx' #chrome extension 위치에 따라 변경해야 함
options.add_extension(packed_extension_path)
driver = webdriver.Chrome(_chromedriver, options=options)

def extention():
    time.sleep(2)
    # 여러 Tab이 있을 경우 확장 프로그램이 실행된 Tab 찾아서 포커스 옮기
    if (len(driver.window_handles) > 1):
        driver.close()
        driver.switch_to.window(driver.window_handles[0]) # 첫번째 실행된 Tab이 확장 프로그
    time.sleep(2)