import time
import pytest
from utils.driver_factory import get_driver
from utils.screenshot_util import ScreenshotUtil
from pages.signup_page import SignUpPage
from pages.survey_page import SurveyPage
from config import BASE_URL, EMAIL, PASSWORD


@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()


def test_survey_flow(setup):
    driver = setup
    screenshot = ScreenshotUtil()
    signup = SignUpPage(driver)
    survey = SurveyPage(driver)

    # Step 1: Open URL
    signup.load(BASE_URL)
    screenshot.capture(driver, "01_landing")

    # Step 2: Enter Email
    signup.enter_email(EMAIL)
    time.sleep(0.5)
    screenshot.capture(driver, "02_email")

    assert driver.find_element(*signup.EMAIL_INPUT).get_attribute("value") == EMAIL

    # Step 3: Enter Password
    signup.enter_password(PASSWORD)
    time.sleep(1)
    screenshot.capture(driver, "03_password")

    assert driver.find_element(*signup.PASSWORD_INPUT).get_attribute("value") == PASSWORD

    # Step 4: Click Login
    assert signup.is_signin_enabled()
    signup.click_signin()

    time.sleep(3)
    screenshot.capture(driver, "04_dashboard")

    # Step 5: Click Create Survey
    assert survey.is_create_survey_visible()
    survey.click_create_survey()
    screenshot.capture(driver, "05_create_survey_clicked")

    # Step 6: Scroll to Survey Name
    survey.scroll_to_survey_name()
    screenshot.capture(driver, "06_survey_name")

    assert survey.is_survey_name_visible()

    # Step 7: Scroll to Sample Size
    survey.scroll_to_sample_size()
    screenshot.capture(driver, "07_sample_size")

    assert survey.is_sample_size_visible()

    # Step 8: Scroll to Bottom
    survey.scroll_to_bottom()
    screenshot.capture(driver, "08_bottom")

    # Step 9: Click Brand Lift Study
    survey.click_brand_lift_study()
    screenshot.capture(driver, "09_brand_lift_selected")

    assert survey.is_brand_lift_selected()