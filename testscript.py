import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 

class ExampleTests(unittest.TestCase):

    def setUp(self): 
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        

    def test_login_failure(self):
        driver = self.driver
        driver.get("https://www.esteelauder.com/")
        signed_out_link = driver.find_element(by=By.CLASS_NAME, value="signed-out-link")
        signed_out_link.click()
        assert driver.current_url == "https://www.esteelauder.com/account/signin.tmpl"

        email_textbox = driver.find_element(by=By.ID, value='form--signin--field--EMAIL_ADDRESS')
        password_textbox = driver.find_element(by=By.ID, value='form--signin--field--PASSWORD')

        email_textbox.send_keys("fake@email.com")
        password_textbox.send_keys("fakepassword123")
        # TODO: come back and import keys to make this more readable
        password_textbox.send_keys('\ue007')

        # TODO: figure out why 10 seconds doesn't work but 100 seconds passes imeadiately 
        error_message = WebDriverWait(driver, 100).until(lambda x: x.find_element(by=By.ID, value='no_account..signin'))
        text = error_message.text

        assert text in ["We do not have an account associated with that email address. Please register now.", "We do not ha...register now."]

    def test_create_account_failure_exists(self): 
        driver = self.driver
        driver.get("https://www.esteelauder.com/account/signin.tmpl")

        

        loyalty_panel = WebDriverWait(driver, 100).until(lambda x: x.find_element(by=By.CLASS_NAME, value='loyalty-signup-panel__header'))
        # time.sleep(500)
        
        close_button = driver.find_element(by=By.CLASS_NAME, value='gnav-signup-overlay__close')
        
        if(loyalty_panel.is_displayed()):
            close_button.click()

        create_account_tab = driver.find_element(by=By.CLASS_NAME, value='js-signin-panel-link')
        create_account_tab.click()

        firstname_textbox = WebDriverWait(driver, 100).until(lambda x: x.find_element(by=By.ID, value='form--registration--field--FIRST_NAME'))

        email_textbox = driver.find_element(by=By.ID, value='form--registration--field--PC_EMAIL_ADDRESS')
        password_textbox = driver.find_element(by=By.ID, value='form--registration--field--PASSWORD')
        
        firstname_textbox.click()
        firstname_textbox.send_keys("Angela")
        email_textbox.send_keys("angela.julian@gmail.com")
        password_textbox.send_keys("fakepassword123")
        # TODO: come back and import keys to make this more readable
        password_textbox.send_keys('\ue007')

        # TODO: figure out why 10 seconds doesn't work but 100 seconds passes imeadiately 
        error_message = WebDriverWait(driver, 100).until(lambda x: x.find_element(by=By.ID, value='account_exists..'))
        text = error_message.text

        assert text == "Our records indicate that you have an account with that email address. Please enter your password."

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__': 
    unittest.main()