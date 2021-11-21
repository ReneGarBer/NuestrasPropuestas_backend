import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.common import exceptions as EX

class bot_scraping:
    url: str
    ser_path: str
    service: Service
    driver: webdriver
    key: str
    links: list[str]
    element: WebElement

    def __init__(self,ser_path)-> None:
        self.ser_path = ser_path
        self.service = Service(self.ser_path)
        self.service.start()
        self.driver = webdriver.Remote(self.service.service_url)

    def __repr__(self)-> str:
        return "url: " + self.url + ", ser_path: " + self.ser_path + ", element: " + self.element

    def open_page(self,url,titulo)->str:
        self.url = url
        self.driver.get(self.url)
        self.driver.minimize_window()
        try:
            self.element = wait(self.driver,10).until(EC.title_is(titulo))
        except EX as ex:
            return ex

    def find_element_by(self,by,locator)-> WebElement:
        if by == 'id':
            self.element = self.driver.find_element(By.ID,locator)

        elif by == 'xpath':
            self.element = self.driver.find_element(By.XPATH,locator)

        elif by == 'link text':
            self.element = self.driver.find_element(By.LINK_TEXT,locator)

        elif by == 'partial link text':
            self.element = self.driver.find_element(By.PARTIAL_LINK_TEXT,locator)
        
        elif by == 'name':
            self.element = self.driver.find_element(By.NAME,locator)
        
        elif by == 'tag name':
            self.element = self.driver.find_element(By.TAG_NAME,locator)
        
        elif by == 'class name':
            self.element = self.driver.find_element(By.CLASS_NAME,locator)
        
        elif by == 'css selector':
            self.element = self.driver.find_element(By.CSS_SELECTOR,locator)

        else:
            print('la opcion no es valida')
        
        return self.element

    def select_option(self,option: str,by,locator)->None:
        self.element = self.find_element_by(by,locator)
        select_object = Select(self.element)
        select_object.select_by_value(option)
        try:
            element = wait(self.driver,50).until(EC.url_changes(self.url))
        except EX as ex:
            print(ex)

    def click_button(self,by,locator)->None:
        self.element = self.find_element_by(by,locator)
        try:
            self.element.click()
            wait(self.driver,15)
        except EX as ex:
            print(ex)

    def find_pdf_links_dy_locator(self,by,locator) -> list[str]:
        self.element = self.driver.find_elements(by,locator)
        for link in self.element:
            if ".pdf" in link.get_attribute('href'):
                self.links.append(link.get_attribute('href')) 
        return self.links

    def find_pdf_links(self)->list[str]:
        self.element = self.driver.find_elements(By.TAG_NAME,'a')
        for link in self.element:
            if link.get_attribute('href') != None:
                if ".pdf" in link.get_attribute('href'):
                    #self.links.append(link.get_attribute('href'))
                    print(link.get_attribute('href'))
        return self.links

    def insert_key_into(self,keys: str,by,locator)-> None:
        self.element = self.find_element_by(by,locator)
        self.element.send_keys(keys)

    def close_window(self)->None:
        self.driver.close()
