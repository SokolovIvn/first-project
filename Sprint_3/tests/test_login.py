import random

from Locators import BUTTON_ORDER, BUTTON_MAIN_ENTER, FIELD_EMAIL, FIELD_PASSWORD, BUTTON_ENTER, BUTTON_ENTER_LK, BUTTON_ENTER_ON_FORM_REGISTR
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


def test_login_on_main_done(get_fixture_email, get_fixture_pswd):
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

    driver.quit()

def test_login_with_button_header(get_fixture_email, get_fixture_pswd):

    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    email = get_fixture_email
    password = get_fixture_pswd

    driver.find_element(By.XPATH, BUTTON_ENTER_LK).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    driver.quit()

def test_login_with_button_on_register_page(get_fixture_email, get_fixture_pswd):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/register")
    email = get_fixture_email
    password = get_fixture_pswd

    driver.find_element(By.XPATH, BUTTON_ENTER_ON_FORM_REGISTR).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(
    expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    driver.quit()


def test_login_on_page_forgot_password(get_fixture_email, get_fixture_pswd):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

    email = get_fixture_email
    password = get_fixture_pswd

    driver.find_element(By.XPATH, BUTTON_ENTER_ON_FORM_REGISTR).click()
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_password = driver.find_element(By.XPATH, FIELD_PASSWORD)
    button_enter = driver.find_element(By.XPATH, BUTTON_ENTER)

    field_email.send_keys(email)
    field_password.send_keys(password)
    button_enter.click()

    WebDriverWait(driver, 15).until(
        expected_conditions.element_to_be_clickable((By.XPATH, BUTTON_ORDER)))

    driver.quit()
