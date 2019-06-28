import pytest
import os
import time

from selenium import webdriver


SMS_USER = os.environ.get("SMS_USER")
SMS_PASSWORD = os.environ.get("SMS_PASSWORD")

URL = "https://www.way2sms.com/"


@pytest.fixture
def driver_login():
    driver = webdriver.Chrome()
    driver.get(URL)

    time.sleep(1)

    driver.find_element_by_id("mobileNo").send_keys(SMS_USER)
    driver.find_element_by_id("password").send_keys(SMS_PASSWORD)
    driver.find_element_by_xpath('//*[@id="loginform"]/div[2]/div[2]/button').click()

    time.sleep(2)
    yield driver

    time.sleep(2)
    driver.quit()
