'''
Created on 2018. 7. 8.

@author: J
'''
from bs4 import BeautifulSoup
from collections import Iterable
from urllib.request import urlopen

import time
from selenium import webdriver

from selenium.common.exceptions import NoAlertPresentException, TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from asyncio.tasks import sleep


class tool:
    def __init__(self):
        path = "C:/Users/J/Desktop/pro/webCR/chromedriver_win32/chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def visit(self,  url):
        self.driver.get(url)
        return self

    def id_selecter(self,  element_id):
        self.driver.find_element_by_id(element_id).click()
        return self
    
    def css_selector(self,  css_selector):
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(css_selector).click()
        return self
    
    def class_selecter(self,  class_name):
        time.sleep(0.2)
        self.driver.find_element_by_class_name(class_name).click()
        return self
    
    def link_text_selecter(self,  link_text):
        self.driver.find_element_by_link_text(link_text).click()
        return self
    
    def xpath_selecter(self,  xpath):
        time.sleep(0.5)
        self.driver.find_element_by_xpath(xpath)
        return self

    def wait(self,  element_id, timeout):
        expected = EC.presence_of_element_located((By.ID, element_id))
        WebDriverWait(self.driver, timeout).until(expected)
        return self

    def switch_to_frame(self,  frame_id):
        self.driver.switch_to_frame(frame_id)
        return self
    
    def alert_dismiss(self):
        try:
            self.driver.switch_to_alert().dismiss()
        except NoAlertPresentException as e:
            print(e)
        return self
    
    def css_scrolled_next(self,  css_selector):
        time.sleep(0.5)
        self.driver.find_element_by_css_selector(css_selector).location_once_scrolled_into_view()
        return self
    
    def ex(self,  xpath):
        select = self.driver.find_element_by_xpath(xpath)
        print(select)
        time.sleep(2)
        
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", select)
        
        self.last_height = self.driver.execute_script("return arguments[0].scrollHeight();", select)
        print("끼오옷"+self.last_height)
        
        while True:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", select)
            time.sleep(0.5)
            new_height = self.driver.execute_script("return arguments[0].scrollHeight();", select)
            if new_height == self.last_height:
                break
            last_height = new_height
            
        pass
        
            
    def page_source(self):
        print("pgS="+self.driver.page_source)
        return self
    
    def quit(self):
        self.driver.quit()
        return self
    
    
    
class main():
    url = "http://www.hira.or.kr/rd/hosp/getHospList.do?pgmid=HIRAA030002020000"

    #
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    #
    driver = tool()
    driver.visit(url)
    #
    driver.link_text_selecter("호스피스전문기관")
    driver.css_selector("#chk_all_dtl")
    #driver.css_selector("#chk_all_oft")
    ##hosp-form > div > div.search-condition.type2 > a
    driver.css_selector("#hosp-form > div > div.search-condition.type2 > a")
    
    
    time.sleep(5)
    web = urlopen("https://www.hira.or.kr/rd/hosp/hospSrchListAjax.do")
    soup = BeautifulSoup(web,  "html.parser")
    print(soup)
    ##hosp-form > div > div.search-hospital-area > div.search-hospital-wrap > div.select-hospital-list > div.list-box.list4 > div > table > tbody > tr:nth-child(10)
    driver.css_selector("#hosp-form > div > div.search-hospital-area > div.search-hospital-wrap > div.select-hospital-list > div.list-box.list4 > div > table > tbody > tr:nth-child(10)")
    
    driver.ex("//*[@id="+'"hosp-form"'+"]/div/div[2]/div[2]/div[1]/div[4]/div/table")
    print("완")
    
    
    
    
if __name__ == '__main__':
    main()


