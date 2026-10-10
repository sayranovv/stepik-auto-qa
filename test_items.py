import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_product_page_has_add_to_basket_button(browser):
    browser.get(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    )
    time.sleep(30)

    selector = "#add_to_basket_form button.btn-add-to-basket"
    button = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
    )
    assert len(browser.find_elements(By.CSS_SELECTOR, selector)) == 1, (
        "На странице должна быть ровно одна кнопка добавления в корзину"
    )
    assert button.is_displayed(), "Кнопка добавления в корзину должна быть видна"
