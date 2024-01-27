from enum import Enum


class Credentials(Enum):
    USERNAME = "test"
    PASSWORD = "test"
    NEW_USERNAME = "anzor.gubzhokov13@yandex.ru"
    NEW_PASSWORD = "dzonya14"


LINK = "https://zaycev.net/"

SELECTORS = {
            'button_login': '//div[@class="wfuhyz-11 hkLzAz"]',
            'button_name': '//input[@class="ji2meo-1 bRfJnD"]',
            'button_pass': '//input[@class="ji2meo-1 gOLHdn"]',
            'button_click': '//button[@class="c4ymd0-0 kdnyEc"]',
            'error_text': '//h1[@class="sc-1kvxqaa-3 fTgslz"]',
            'button_privat': '//button[@class="wfuhyz-13 gggOte"]',
            'button_': '//button[@class="wfuhyz-10 WekGP"]',
            'button_quit': '//div[@class="xvjpdk-1 jDqlCJ"]',
            'main_menu': '//a[@class="sc-1vuj2t8-0 pbfhi wfuhyz-5 enSKgm"]',
            'button_new': '//ul[@class="sc-1k28xbs-1 hmZctp"]/li[2]',
            'collection': '//ul[@class="gsnbbv-1 GXlBx"]/li[2]',
            'one_collection': '//ul[@class="sc-1t33r2c-2 dcgQQE"]/li',
            'search': '//input[@class="wfuhyz-18 gGsMDx"]',
            'search_button': '//button[@class="wfuhyz-19 hYUsQe"]',
            'table_with_music': '//ul[@class="bm5dwu-0 hJYea"]',
            'check_collection': '//span[@class="pp9dwd-11 iWWJMi"]',
             }

