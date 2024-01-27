import time

import allure
from selenium.webdriver.common.by import By
from test_task.helpers import page_load_check, element_exists, authorize_account, quit_account, search_music
from test_task.constants import Credentials, LINK, SELECTORS


@allure.title("Тест на загрузку главной страницы")
def test_loading_home_page(browser):
    """
    Шаги теста:
    1. Открытие главной страницы.
    2. Проверка главной страницы на корректность работы
    """

    with allure.step("Шаг на открытие основной страницы"):
        browser.get(LINK)
    assert page_load_check(browser, SELECTORS['button_login']), 'page not load'


@allure.title("Тест логина в аккаунт с некорректными кредами")
def test_incorrect_login_page(browser):
    """
    Шаги теста:
    1. Открытие главной страницы.
    2. Нажатие на кнопку "Войти".
    3. Ввод неверных учетных данных.
    4. Проверка безуспешного входа в личный кабинет.
    """

    with allure.step("Открытие главной страницы"):
        browser.get(LINK)
    login_link = browser.find_element(By.XPATH, SELECTORS['button_login'])
    login_link.click()

    with allure.step("Ввод неверных данных на вход"):
        authorize_account(browser, Credentials.USERNAME.value, Credentials.PASSWORD.value)
    assert element_exists(browser, '//input[@class="ji2meo-1 bRfJnD"]'), "Login page element not found"
    #   constants


@allure.title("Проверка логина на ресурс")
def test_correct_login_page(browser):
    """
    Шаги теста:
    1. Открытие главной страницы.
    2. Нажатие на кнопку "Войти".
    3. Тест на вход подает верные и неверные данные для авторизации входа в личный кабинет.
    4. Следом проводится проверка, что страница загружается корректно
    """

    with allure.step("Открытие главной страницы"):
        browser.get(LINK)
    login_link = browser.find_element(By.XPATH, SELECTORS['button_login'])
    login_link.click()

    with allure.step("Ввод верных данных на вход"):
        authorize_account(browser, Credentials.NEW_USERNAME.value, Credentials.NEW_PASSWORD.value)
        assert element_exists(browser, SELECTORS['main_menu']), "Logout element not found"

    with allure.step("Нажатие на кнопку выхода"):
        quit_account(browser)


@allure.title("Проверка выхода из аккаунта")
def test_logout_from_account(browser):
    """
    Шаги теста:
    1. Открытие главной страницы.
    2. Нажатие на кнопку "Войти".
    3. Ввод верных учетных данных.
    4. Проверка успешного входа в личный кабинет.
    5. Тест выходит из личного кабинета проверяется, что страница загружается корректно
    """

    with allure.step("Открытие главной страницы "):
        browser.get(LINK)
    login_link = browser.find_element(By.XPATH, SELECTORS['button_'])
    login_link.click()

    with allure.step("Ввод верных данных от страницы"):
        authorize_account(browser, Credentials.NEW_USERNAME.value, Credentials.NEW_PASSWORD.value)
        assert element_exists(browser, SELECTORS['main_menu']), "exit to main menu"

    with allure.step("Нажатие на кнопку выхода"):
        quit_account(browser)


@allure.title("Проверка работы поиска")
def test_checking_the_search_operation(browser):
    """
      Этот тест проверяет корректность работы поиска на главной странице.
    Шаги теста:
    1. Открытие главной страницы.
    2. Нажатие на кнопку "Войти".
    3. Ввод верных учетных данных.
    4. Проверка успешного входа в личный кабинет.
    5. Выполнение поиска по запросу "Масло Черного Тмина".
    6. Проверка наличия таблицы с музыкой после выполнения поиска.
    7. Выход из аккаунта
    """

    with allure.step("Проверка открытия главной страницы "):
        browser.get(LINK)

    login_link = browser.find_element(By.XPATH, SELECTORS['button_'])
    login_link.click()

    with allure.step("Ввод верных данных от страницы"):
        authorize_account(browser, Credentials.NEW_USERNAME.value, Credentials.NEW_PASSWORD.value)
        assert element_exists(browser, SELECTORS['main_menu']), "exit to main menu"

    with allure.step("Поиск"):
        search_music(browser, "Масло Черного Тмина")

    with allure.step("Нажатие на кнопку выхода"):
        quit_account(browser)


@allure.title("Проверка работы сборников")
def test_open_collection(browser):
    """
    Шаги теста:
    1. Открытие главной страницы.
    2. Нажатие на кнопку "Войти".
    3. Ввод верных учетных данных.
    4. Проверка успешного входа в личный кабинет.
    5. Переход в раздел сборников
    6. Проверка корректного отображения сборников
    """
    with allure.step("Открытие главной страницы "):
        browser.get(LINK)

    login_link = browser.find_element(By.XPATH, SELECTORS['button_'])
    login_link.click()

    with allure.step("Ввод верных данных от страницы"):
        authorize_account(browser, Credentials.NEW_USERNAME.value, Credentials.NEW_PASSWORD.value)
        assert element_exists(browser, SELECTORS['main_menu']), "exit to main menu"

    with allure.step("Проверка корректного отображения сборников"):
        collection = browser.find_element(By.XPATH, SELECTORS['collection'])
        collection.click()
        time.sleep(2)
        new_collection = browser.find_element(By.XPATH, SELECTORS['button_new'])
        new_collection.click()
        time.sleep(2)
        one_collection = browser.find_element(By.XPATH, SELECTORS['one_collection'])
        one_collection.click()
        assert element_exists(browser, SELECTORS['check_collection']), "didn't enter the collection"
