# Importing necessary  packages
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.driverLocator import executable_path
from pageObjects.locator_elements import *
from pageObjects.pageTitles import *
from pageObjects.variables import *


# Create Test class
class Test_Wikipedia:
    url = page_url

    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path=executable_path)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_001_get_page(self):
        self.driver.get(self.url)
        assert self.driver.title == search_page_title

    def test_002_enter_keyword_and_search(self):

        self.driver.find_element(By.XPATH, search_input_box).send_keys("Nepal")
        self.driver.find_element(By.XPATH, search_button).click()
        time.sleep(3)
        # self.driver.find_element(By.ID, id_search_box_2).send_keys('Nepal')
        # time.sleep(3)  # wait for 3 seconds
        # # Click on search button
        # self.driver.find_element(By.XPATH, click_search_button).click()
        # time.sleep(5)  # wait for 5 seconds
        assert self.driver.title == search_nepal_page_title

    def test_go_back_to_main_page(self):
        self.driver.get(page_url)
        main_page = self.driver.find_element(By.XPATH, xpath_main_page)
        main_page.click()
        assert self.driver.title == main_page_title
