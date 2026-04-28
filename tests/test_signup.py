import time
import pytest
import pyautogui
from utils.driver_factory import get_driver
from utils.screenshot_util import ScreenshotUtil
from pages.signup_page import SignUpPage
from pages.dashboard_page import DashboardPage
from config import BASE_URL, EMAIL, PASSWORD


@pytest.fixture
def setup():
    driver = get_driver()
    yield driver
    driver.quit()

def test_signup_flow(setup):
    driver = setup
    screenshot = ScreenshotUtil()
    page = SignUpPage(driver)

    # Step 1: Open URL
    page.load(BASE_URL)
    assert "PulseShift" in driver.title or driver.current_url == BASE_URL
    screenshot.capture(driver, "01_landing_page")

    # Step 2: Enter Email
    page.enter_email(EMAIL)
    time.sleep(0.5)
    screenshot.capture(driver, "02_email_entered")

    email_value = driver.find_element(*page.EMAIL_INPUT).get_attribute("value")
    assert email_value == EMAIL

    # Step 3: Enter Password
    page.enter_password(PASSWORD)
    time.sleep(1)
    screenshot.capture(driver, "03_password_entered")

    password_value = driver.find_element(*page.PASSWORD_INPUT).get_attribute("value")
    assert password_value == PASSWORD

    # Step 4: Button Enabled
    assert page.is_signin_enabled() == True

    # Step 5: Click Sign-in
    page.click_signin()
    time.sleep(3)
    screenshot.capture(driver, "04_home_page")

    assert driver.current_url != BASE_URL

    # ==========================
    # 🔽 NEW NAVIGATION FLOW
    # ==========================

    dashboard = DashboardPage(driver)

    # Step 6: Click Survey List
    dashboard.click_survey_list()
    time.sleep(0.5)
    screenshot.capture(driver, "05_survey_list")
    dashboard.click_survey_filter_open()
    time.sleep(0.5)
    screenshot.capture(driver, "06_survey_filter_open")
    dashboard.click_survey_filter_close()

    assert dashboard.is_survey_list_page()

    # Step 7: Click Report List
    dashboard.click_report_list()
    time.sleep(0.5)
    screenshot.capture(driver, "07_report_list")
    dashboard.click_report_filter_open()
    time.sleep(0.5)
    screenshot.capture(driver, "08_report_filter_open")
    dashboard.click_report_filter_close()

    assert dashboard.is_report_list_page()

    # Step 8: Click Brands
    dashboard.click_brands()
    time.sleep(0.5)
    screenshot.capture(driver, "09_brands")
    dashboard.click_brands_filter_open()
    time.sleep(0.5)
    screenshot.capture(driver, "10_brands_filter_open")
    dashboard.click_brands_filter_close()
    time.sleep(0.5)
    dashboard.click_add_brands_open()
    time.sleep(0.5)
    screenshot.capture(driver, "11_add_brands_open")
    dashboard.click_add_brands_close()

    assert dashboard.is_brands_page()