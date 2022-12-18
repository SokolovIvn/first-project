import random

import pytest

from Locators import FIELD_EMAIL, FIELD_PASSWORD, BUTTON_MAIN_ENTER, BUTTON_ENTER, BUTTON_ORDER, BUTTON_ENTER_LK, HREF_PROFILE
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_login_go_to_lk_with(get_fixture_email, get_fixture_pswd):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    email = get_fixture_email
    password = get_fixture_pswd

    driver.find_element(By.XPATH, BUTTON_MAIN_ENTER).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    driver.find_element(By.XPATH, BUTTON_ENTER_LK).click()

    WebDriverWait(driver, 15).until(expected_conditions.visibility_of_element_located((By.XPATH, HREF_PROFILE)))

    assert "https://stellarburgers.nomoreparties.site/account/profile" in driver.current_url

    driver.quit()
