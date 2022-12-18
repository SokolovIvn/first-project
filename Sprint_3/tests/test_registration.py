import random

from Locators import FIELD_NAME, FIELD_EMAIL, FIELD_PASSWORD, BUTTON_REGISTRATION
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_registration_bad_pswd_check_fail_text_done(generate_name, generate_password):
    new_name = generate_name
    new_email = new_name + "@ya.ru"
    password = "12345"

    driver = webdriver.Chrome()

    # переходим на страницу регистрации.
    # да, можно было бы проверить через вход по кнопке, но в данном тесте мы проверяем только позитивный кейс формы реги
    driver.get("https://stellarburgers.nomoreparties.site/register")

    field_name = driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input")
    field_email = driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input")
    field_pswd = driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    # Ждем когда поле ввода станет активным для ввода
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable(field_name))

    # заполняем поля для регистрации
    field_name.send_keys(new_name)
    field_email.send_keys(new_email)
    field_pswd.send_keys(password)
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    # Ждем когда появится форма Авторизации
    WebDriverWait(driver, 15).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".input__error")))

    assert "Некорректный пароль" == driver.find_element(By.CSS_SELECTOR, ".input__error").text

    driver.quit()


def test_geristration_full(generate_name, generate_password):
    driver = webdriver.Chrome()

    new_name = generate_name
    new_email = new_name + "@ya.ru"
    password = generate_password

    # переходим на страницу регистрации.
    # да, можно было бы проверить через вход по кнопке, но в данном тесте мы проверяем только позитивный кейс формы реги
    driver.get("https://stellarburgers.nomoreparties.site/register")

    field_name = driver.find_element(By.XPATH, FIELD_NAME)
    field_email = driver.find_element(By.XPATH, FIELD_EMAIL)
    field_pswd = driver.find_element(By.XPATH, FIELD_PASSWORD)

    # Ждем когда поле ввода станет активным для ввода
    WebDriverWait(driver, 7).until(expected_conditions.element_to_be_clickable(field_name))

    # заполняем поля для регистрации
    field_name.send_keys(new_name)
    field_email.send_keys(new_email)
    field_pswd.send_keys(password)
    driver.find_element(By.XPATH, BUTTON_REGISTRATION).click()

    # Ждем когда появится форма Авторизации
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//h2[text()='Вход']")))

    driver.quit()
