# the main script needs to instantiate the Selenium webdriver
from selenium import webdriver
import time
import json
from selenium.webdriver.common.by import By
from collections import namedtuple

with open('env.json', 'r') as f:
    _env = json.load(f)
Env = namedtuple('Env', _env.keys())
env = Env(**_env)


def main():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")
    # driver.implicitly_wait(0.5)
    time.sleep(3)

    username_input = driver.find_element(By.NAME, "username")
    username_input.send_keys(env.USERNAME)

    password_input = driver.find_element(By.NAME, 'password')
    password_input.send_keys(env.PASSWORD)

    login_button = driver.find_element(By.XPATH, "//div[contains(text(), 'Log In')]")
    login_button.click()


    return
