from Locators import FIELD_EMAIL, FIELD_PASSWORD, BUTTON_MAIN_ENTER, BUTTON_ENTER, BUTTON_ORDER, BUTTON_ENTER_LK, \
    HREF_PROFILE, BUTTON_HEADER_CONSTRUCTOR, SELECTED_IS_TOPPING, TAB_TOPPING, TAB_SAUCES, SELECTED_IS_SAUCES, SELECTED_IS_BUNS, TAB_BUNS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_goto_constructor_with_personal_account(get_fixture_email, get_fixture_pswd):
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
    driver.find_element(By.XPATH, BUTTON_HEADER_CONSTRUCTOR).click()

    assert "Соберите бургер" == driver.find_element(By.XPATH, ".//h1").text

    driver.quit()


def test_check_section_topping_is_selected(get_fixture_email, get_fixture_pswd):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH,TAB_TOPPING)))
    driver.find_element(By.XPATH, TAB_TOPPING).click()

    assert len(driver.find_elements(By.XPATH, SELECTED_IS_TOPPING)) == 1

    driver.quit()


def test_check_section_saucec_is_selected(get_fixture_email, get_fixture_pswd):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, TAB_SAUCES)))
    driver.find_element(By.XPATH, TAB_SAUCES).click()

    assert len(driver.find_elements(By.XPATH, SELECTED_IS_SAUCES)) == 1

    driver.quit()


def test_check_section_buns_is_selected(get_fixture_email, get_fixture_pswd):
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, TAB_BUNS)))
    driver.find_element(By.XPATH, TAB_SAUCES).click()
    driver.find_element(By.XPATH, TAB_BUNS).click()

    assert len(driver.find_elements(By.XPATH, SELECTED_IS_BUNS)) == 1

    driver.quit()
