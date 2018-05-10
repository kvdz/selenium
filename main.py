import unittest
import time
from selenium import webdriver



class Chrome_HudlMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\kay\\Documents\\selenium\\chromedriver.exe')

    def test_main_page(self):
        driver = self.driver
        driver.get("https://www.hudl.com/")
        self.assertIn("Hudl", driver.title)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

class Chrome_HudleLogInPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\kay\\Documents\\selenium\\chromedriver.exe')


    def test_login_page(self):
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        self.assertIn("Hudl", driver.title)
        elem_email = driver.find_element_by_id('email')
        elem_email.send_keys("kay20@hotmail.com")
        elem_password = driver.find_element_by_id('password')
        elem_password.send_keys("0123456789")
        elem_login_btn = driver.find_element_by_id('logIn')
        elem_login_btn.click()
        time.sleep(2) # wait for page to load.
        # check title has changed into home dashboard.
        self.assertIn("Home - Hudl", driver.title)
        assert "No results found." not in driver.page_source

    def test_login_page_fault_login(self):
        driver = self.driver
        driver.get("https://www.hudl.com/login")
        self.assertIn("Hudl", driver.title)
        elem_email = driver.find_element_by_id('email')
        elem_email.send_keys("kay20@hotmail.com")
        elem_password = driver.find_element_by_id('password')
        elem_password.send_keys("0123")
        elem_login_btn = driver.find_element_by_id('logIn')
        elem_login_btn.click()
        time.sleep(2)
        # check if the error popup is shown.
        elem_fault_popup = driver.find_element_by_class_name("need-help")
        self.assertTrue(elem_fault_popup.is_displayed())
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()