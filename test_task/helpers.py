import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from test_task.constants import Credentials, SELECTORS
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def page_load_check(browser: WebDriver, locator: str) -> bool:
    """
    Шаги проверки:
    1.Проверка отображения корректной работы страницы
    2.Если не удается найти элемент и возникает исключение - возвращается False
    В положительных случаях - True
    """

    try:
        browser.find_element(By.XPATH, locator)
        WebDriverWait(browser, 10).until(
            ec.presence_of_element_located((By.TAG_NAME, "html")))
    except:
        return False
    return True


def element_exists(browser: WebDriver, locator: str, timeout: int = 10) -> bool:
    """
    Шаги проверки:
    1.Проверка существования элемента на странице.
    2.Возвращает True, если элемент существует, иначе False.
    """
    try:
        WebDriverWait(browser, timeout).until(
            ec.presence_of_element_located((By.XPATH, locator))
        )
        return True
    except (NoSuchElementException, TimeoutException):
        return False


def authorize_account(browser,
              login=Credentials.NEW_USERNAME.value,
              password=Credentials.NEW_PASSWORD.value):
    """
    Шаги проверки:
    1.Проверка авторизации личного кабинета
    """
    WebDriverWait(browser, 10).until(
        ec.presence_of_element_located((By.XPATH, SELECTORS['button_name']))
    )
    username_input = browser.find_element(By.XPATH, SELECTORS['button_name'])
    password_input = browser.find_element(By.XPATH, SELECTORS['button_pass'])
    submit_button = browser.find_element(By.XPATH, SELECTORS['button_click'])
    username_input.clear()
    username_input.send_keys(login)
    password_input.clear()
    password_input.send_keys(password)
    submit_button.click()


def quit_account(browser: WebDriver):
    """
    Шаги проверки:
    1.Проверка кликабельности кнопки войти
    2.Загрузка кнопки выхода на странице
    3.Прокрутка до кнопки выхода
    """

    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, SELECTORS['button_privat']))
    )
    login_button.click()

    logout_link = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, SELECTORS['button_quit']))
    )

    browser.execute_script("arguments[0].scrollIntoView();", logout_link)
    time.sleep(2)
    logout_link.click()
    assert element_exists(browser, SELECTORS['button_login']), "button_login is not present"


def search_music(browser: WebDriver, name):
    """
    Шаги проверки:
    1.Проверка работы поиска музыки
    """
    search = browser.find_element(By.XPATH, SELECTORS['search'])
    search.click()
    search.send_keys(name)
    search_button = browser.find_element(By.XPATH, SELECTORS['search_button'])
    search_button.click()
    assert element_exists(browser, SELECTORS['table_with_music']), "didn't find the table"
