from sms_automation import *


def test_logged_in_page(driver_login):
    """
    Case description: Login to way2sms.com and validate if the home page is visible
    """
    expected = "SEND SMS"

    assert driver_login.find_element_by_xpath('//*[@id="sendButton"]').text == expected


def test_send_sms(driver_login):
    """
    Case description: Send an sms from the registered account
    """
    driver_login.find_element_by_id("mobile").send_keys(SMS_USER)
    driver_login.find_element_by_id("message").send_keys(
        "This is a test message " "from Selenium"
    )
    driver_login.find_element_by_xpath('//*[@id="sendButton"]').click()

    assert driver_login.find_element_by_id("mobile").text == ""


def test_schedule_sms(driver_login):
    """
    Case description:
        1. Click on the Future SMS link
        2. Validate if the scheduling page loads successfully
        3. Schedule an SMS
    """
    try:
        expected_text = "Future SMS"
        assert (
            driver_login.find_element_by_xpath('//*[@id="futsms"]/a/span').text
            == expected_text
        )
    except AssertionError:
        pytest.fail('There is no text called "Future SMS"', pytrace=False)

    try:
        button_text = "SCHEDULE"
        driver_login.find_element_by_xpath('//*[@id="futsms"]/a/span').click()
        time.sleep(2)
        assert (
            driver_login.find_element_by_xpath('//*[@id="sendButton"]').text
            == button_text
        )
    except AssertionError:
        pytest.fail("There is no Schedule SMS button", pytrace=False)

    try:
        driver_login.find_element_by_xpath('//*[@id="futsms"]/a/span').click()
        driver_login.find_element_by_xpath('//*[@id="mobile"]').send_keys(SMS_USER)
        driver_login.find_element_by_xpath('//*[@id="message"]').send_keys(
            "This is a test message from Selenium!"
        )
        driver_login.find_element_by_xpath('//*[@id="sdate"]').clear()
        driver_login.find_element_by_xpath('//*[@id="sdate"]').send_keys("29/06/2019")

        driver_login.find_element_by_xpath('//*[@id="stime"]').clear()
        driver_login.find_element_by_xpath('//*[@id="stime"]').send_keys("05:00")
        driver_login.find_element_by_xpath('//*[@id="sendButton"]').click()
        time.sleep(2)
        assert driver_login.find_element_by_xpath('//*[@id="message"]').text == ""
        os.system("taskkill /f /im chromedriver.exe")
    except AssertionError:
        pytest.fail("Could not schedule SMS", pytrace=False)
