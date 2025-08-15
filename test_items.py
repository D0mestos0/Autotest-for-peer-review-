import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_button(browser):
    print("Open browser")
    browser.get(link)

    # требование по заданию - оставить паузу для визуальной проверки текста на кнопке
    time.sleep(30)

    # убеждаюсь, что кнопка есть и видна
    button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")))
    assert button.is_displayed(), "The button was not found"



# Использую is_displayed(), чтобы проверить наличие кнопки
# Долго не могла понять, как вообще проверить без привязки к тексту кнопки, поэтому решила использовать этот способ, даже несмотря на то, что его мы не проходили в курсе
# Если будут какие-то советы или рекомендации, то я буду очень рада и благодарна