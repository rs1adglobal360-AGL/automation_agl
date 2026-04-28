from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Sidebar CTAs (update locators if needed)
    SURVEY_LIST = (By.XPATH, "/html/body/div[2]/aside/div/nav/div[2]")
    SURVEY_LIST_FILTER_OPEN = (By.XPATH, "/html/body/div[2]/div/main/div/div[1]/div[2]/button[1]")
    SURVEY_LIST_FILTER_CLOSE = (By.XPATH, "/html/body/div[12]/div/div/div/div[1]/button")
    REPORT_LIST = (By.XPATH, "/html/body/div[2]/aside/div/nav/div[3]")
    REPORT_LIST_FILTER_OPEN = (By.XPATH, "/html/body/div[2]/div/main/div/div[1]/div[2]/button[1]")
    REPORT_LIST_FILTER_CLOSE = (By.XPATH, "/html/body/div[4]/div/div/div/div[1]/button")
    BRANDS = (By.XPATH, "/html/body/div[2]/aside/div/div[3]/div/div[1]")
    BRANDS_FILTER_OPEN = (By.XPATH, "/html/body/div[2]/div/main/div/div[2]/div[2]/button[1]")
    BRANDS_FILTER_CLOSE = (By.XPATH, "/html/body/div[4]/div/div/div/div[1]/button")
    ADD_BRAND_POPUP_OPEN = (By.XPATH, "/html/body/div[2]/div/main/div/div[1]/button")
    ADD_BRAND_POPUP_CLOSE = (By.XPATH, "/html/body/div[2]/div/main/div/div[4]/div/div[1]/button")


    def click_survey_list(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SURVEY_LIST))
        element.click()

    def click_survey_filter_open(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SURVEY_LIST_FILTER_OPEN))
        element.click()

    def click_survey_filter_close(self):
        element = self.wait.until(EC.element_to_be_clickable(self.SURVEY_LIST_FILTER_CLOSE))
        element.click()

    def click_report_list(self):
        element = self.wait.until(EC.element_to_be_clickable(self.REPORT_LIST))
        element.click()

    def click_report_filter_open(self):
        element = self.wait.until(EC.element_to_be_clickable(self.REPORT_LIST_FILTER_OPEN))
        element.click()

    def click_report_filter_close(self):
        element = self.wait.until(EC.element_to_be_clickable(self.REPORT_LIST_FILTER_CLOSE))
        element.click()

    def click_brands(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BRANDS))
        element.click()

    def click_brands_filter_open(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BRANDS_FILTER_OPEN))
        element.click()

    def click_brands_filter_close(self):
        element = self.wait.until(EC.element_to_be_clickable(self.BRANDS_FILTER_CLOSE))
        element.click()

    def click_add_brands_open(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_BRAND_POPUP_OPEN))
        element.click()

    def click_add_brands_close(self):
        element = self.wait.until(EC.element_to_be_clickable(self.ADD_BRAND_POPUP_CLOSE))
        element.click()

    # Assertions helpers
    def is_survey_list_page(self):
        return "survey" in self.driver.current_url.lower()

    def is_report_list_page(self):
        return "report" in self.driver.current_url.lower()

    def is_brands_page(self):
        return "brand" in self.driver.current_url.lower()