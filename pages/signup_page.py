from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators (update if needed)
    EMAIL_INPUT = (By.XPATH, "//*[@id='companyEmail']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='password']")
    SIGNIN_BUTTON = (By.XPATH, "/html/body/div[2]/div/div/div[2]/form/button")

    def load(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        email_field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        password_field.clear()
        password_field.send_keys(password)

    def is_signin_enabled(self):
        button = self.wait.until(EC.presence_of_element_located(self.SIGNIN_BUTTON))
        return button.is_enabled()

    def click_signin(self):
        button = self.wait.until(EC.element_to_be_clickable(self.SIGNIN_BUTTON))
        button.click()