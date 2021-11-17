# -*- coding: utf-8 -*-

import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import ro_func

driver = ro_func.driver
count = 0
seed = ("bind orbit account repeat buddy sad clog property vapor cake raven original",
            "tower boost ready buddy task sudden lake lemon charge hamster capital organ",
            "mixed distance resemble valve saddle message post pledge acid nurse spider absorb",
            "heart endorse abstract caught cave edit rebel rain steak organ lyrics stomach",
            "fantasy dune decorate stuff fetch poet tornado place gown gasp gesture motion",
            "review ceiling fresh yellow guard vicious pole match bronze claw spawn measure",
            "mean demise deny exotic average stumble list silly visa floor wisdom equal",
            "laundry spirit defense doll fall rhythm solution more profit retreat cattle vibrant",
            "scatter lion acoustic error able pill service spot budget pattern absent father",
            "knife matrix waste begin abstract tennis bundle off edge credit fade draft")

while count <10:
    count = count + 1      
    ro_func.extention()
    driver = ro_func.driver
    driver.implicitly_wait(10)
    #metamask wallet 설정
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div[2]/div/div[2]/div[1]/button').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[4]/div[1]/div/input').send_keys(seed[count - 1])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys('vnfmsgk12#')
    driver.find_element_by_xpath('//*[@id="confirm-password"]').send_keys('vnfmsgk12#')
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/div[7]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/form/button').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div/button').click()
    time.sleep(3)
    #driver.find_element_by_xpath('//*[@id="popover-content"]/div/div/section/header/div/button').click()
    time.sleep(3)

    #wallet net 변경
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div/div[2]/div[1]/div/span').click()
    action = ActionChains(driver)
    submenu = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//span[contains(text(), "{}")]'.format('Ropsten 테스트 네트워크'))))
    action.move_to_element(submenu).click().perform()
    time.sleep(4)

    #ropsten faucet 선택
    driver.find_element_by_xpath('//*[@class="icon-button__circle"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/span/div[1]/div/div/div[2]/div/div[2]/div[3]/button').click()
    time.sleep(5)

    #faucet 창 전환
    driver.switch_to.window(driver.window_handles[-1])
    while True:
        try:
            time.sleep(3)
            #driver.refresh()        
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "section > div:nth-child(1) > div.panel-body > button"))).click()
            break
        except(StaleElementReferenceException):
            continue      

    time.sleep(1)    

    # wallet 확장 화면으로 전환 후 연결
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[4]/div[2]/button[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app-content"]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]').click()
    time.sleep(5)

    #faucet 화면으로 전환
    driver.switch_to.window(driver.window_handles[1])

    while True:
        try:
            time.sleep(3)
            #driver.refresh()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "section > div:nth-child(1) > div.panel-body > button"))).click()
            print('{}회 클릭'.format(count))                        
            break            
        except(StaleElementReferenceException):
            continue 
    time.sleep(10)
    while True:
        try:
            time.sleep(3)
            #driver.refresh()
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "section > div:nth-child(1) > div.panel-body > button"))).click()
            print('{}회 재 클릭'.format(count))                    
            time.sleep(10)
            driver.quit()
            time.sleep(3)
            ro_func.drivers()
            print('driver 재 시작')
            break            
        except(StaleElementReferenceException):
            continue

if count == 10:
    time.sleep(3)
    driver = ro_func.driver
    driver.quit()
    print('the end')
