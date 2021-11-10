import ropsten_faucet

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait



driver = ropsten_faucet.driver
ropsten_faucet.extention()

driver.quit()

ropsten_faucet.drivers()
ropsten_faucet.extention()