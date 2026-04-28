from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SurveyPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    CREATE_SURVEY_BTN = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/main[1]/div[1]/div[1]/button[1]")
    SURVEY_NAME_SECTION = (By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div/div/label")
    SAMPLE_SIZE_SECTION = (By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[2]/div/div[2]/div[5]/div/div/div/div[1]/label")
    BRAND_LIFT_STUDY = (By.XPATH, "/html/body/div[2]/div/main/div/div/div/div[2]/div/div[2]/div[6]/div[2]/div[2]/div[1]/label")

    # Actions
    def click_create_survey(self):
        self.wait.until(EC.element_to_be_clickable(self.CREATE_SURVEY_BTN)).click()

    def scroll_to_survey_name(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SURVEY_NAME_SECTION))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_sample_size(self):
        element = self.wait.until(EC.visibility_of_element_located(self.SAMPLE_SIZE_SECTION))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_to_bottom(self):
        container = self.driver.find_element(By.CSS_SELECTOR, ".scroll-smooth")  # update
        self.driver.execute_script(
            "arguments[0].scrollTop = arguments[0].scrollHeight", container
        )

    def click_brand_lift_study(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.BRAND_LIFT_STUDY)
        )

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        element.click()

    # Assertions
    def is_create_survey_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.CREATE_SURVEY_BTN))

    def is_survey_name_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.SURVEY_NAME_SECTION))

    def is_sample_size_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.SAMPLE_SIZE_SECTION))

    # def is_brand_lift_selected(self):
    #     element = self.driver.find_element(*self.BRAND_LIFT_OPTION)
    #     return "selected" in element.get_attribute("class")

    def is_brand_lift_selected(self):
        return WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.BRAND_LIFT_OPTION)
                      .get_attribute("aria-checked") == "true"
        )