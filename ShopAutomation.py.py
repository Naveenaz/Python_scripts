from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class ShopStyle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.shopstyle.com/browse/dresses?fts=red+dress"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_shop_style(self):
        driver = self.driver
        driver.get(self.base_url + "/browse/dresses?fts=red+dress")
        driver.find_element_by_css_selector("img.cellImg").click()
        # ERROR: Caught exception [ERROR: Unsupported command [waitForPopUp | ssretailer427431415 | 30000]]
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name={"zapposWindow":true,"counter":1,"lazyEye":"CqACCAEQwdXU2IUoGMkoIL8CKPQBMK4GONUEQnMKAwoBQRIFYnJhbmQSJmdhZS1jbGljaypQcm9kdWN0LVBhZ2UqVGl0bGUqQnJhbmROYW1lGiRodHRwOi8vY291dHVyZS56YXBwb3MuY29tL3JhY2hlbC1yb3kqDAoKUmFjaGVsIFJveUIJCMYCEAUYfCAcUhwvcHJvZHVjdC84MTI2MTc4L2NvbG9yLzEzNDc4WgsKA0RJVhIEd3JhcFoOCgNESVYSB2NvbnRlbnRaDgoDRElWEgd0aGVhdGVyWhMKA0RJVhIMcHJvZHVjdFN0YWdlWgQKAkgxYAOiBigKJgokOTg0Njc5MDctMzYyNC02YjIxLTVkYTUtMDMyNjg5OGNjOTAw"} | ]]
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Rachel Roy Sexy Red Dress[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("span.price.salePrice").click()
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*\$184\.99[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        # Warning: verifyTextPresent may require manual changes
        try: self.assertRegexpMatches(driver.find_element_by_css_selector("BODY").text, r"^[\s\S]*Rachel Roy[\s\S]*$")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
