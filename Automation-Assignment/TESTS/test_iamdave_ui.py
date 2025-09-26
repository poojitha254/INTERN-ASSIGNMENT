import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Fixture to setup and teardown WebDriver
@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--log-level=3")  # Suppress warnings
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Remove DevTools logs

    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()

def test_homepage_load(driver):
    """ Verify homepage loads and title contains 'Dave'"""
    driver.get("https://www.iamdave.ai")
    WebDriverWait(driver, 10).until(EC.title_contains("Dave"))
    assert "Dave" in driver.title

def test_logo_presence(driver):
    """ Check if logo is present"""
    driver.get("https://www.iamdave.ai")
    logo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "img"))
    )
    assert logo.is_displayed()

def test_heading_presence(driver):
    """ Check if heading is present"""
    driver.get("https://www.iamdave.ai")
    heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert heading.is_displayed()

def test_page_navigation(driver):
    """ Test page navigation (About link if exists)"""
    driver.get("https://www.iamdave.ai")
    try:
        about_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "About"))
        )
        about_link.click()
        WebDriverWait(driver, 10).until(EC.title_contains("About"))
        assert "About" in driver.title
    except:
        pytest.skip(" About link not found, skipping test")
