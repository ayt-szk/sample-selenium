import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

PROFILE_PATH="/home/seluser/.config/google-chrome"

class Selenium:
    def __init__(self):
        # Set Chrome Options
        options = webdriver.ChromeOptions()
        # ログイン情報を保持する場合
        # options.add_argument("--user-data-dir=" + PROFILE_PATH)
        
        # Connect Selenium Server
        self.__driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            # ログイン情報を保持する場合
            # command_executor="http://localhost:4444/session",
            desired_capabilities=options.to_capabilities(),
            options=options,
        )
        print("Initial setup completed.")
    

    def sample_function(self):
        self.__driver.get("https://www.yahoo.co.jp/")
        time.sleep(3)

        # FUll XPATHを元に要素の取得してログに表示
        elem_shopping = self.__driver.find_element(
            By.XPATH,
            "/html/body/div/div/main/div[1]/nav/div/div/ul/li[1]/div/a/p/span[1]/span",
        )
        elem_shopping_text = elem_shopping.text
        print(elem_shopping_text)

        # 検索キーワードの入力
        elem_serach_box = self.__driver.find_element(
            By.XPATH, 
            "/html/body/div/div/header/section[1]/div/form/fieldset/span/input"
        )
        elem_serach_box.send_keys("観葉植物　おすすめ")
        time.sleep(3)

        # 検索ボタンのクリック
        elem_serach_button = self.__driver.find_element(
            By.XPATH,
            '/html/body/div/div/header/section[1]/div/form/fieldset/span/button/span/span'
        )
        elem_serach_button.click()
        time.sleep(3)


    def driver_quit(self) -> None:
        self.__driver.quit()