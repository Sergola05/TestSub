from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 60)

try:
    driver.get("https://demo.opencart.com")
    print("Страница загружена")
    time.sleep(2)


    pc_category_menu = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/a")
    ))
    pc_category_menu.click()
    print("Меню категории PC открыто")
    time.sleep(2)

    pc_category = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='narbar-menu']/ul/li[1]/div/div/ul/li[1]/a")
    ))
    pc_category.click()
    print("Переход в категорию PC выполнен")
    time.sleep(2)

    empty_page_message = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='content']/p[contains(text(), 'There are no products to list in this category.')]")
    ))
    if empty_page_message:
        print("Страница пуста: товаров нет")
    else:
        print("На странице есть товары")

except Exception as e:
    print(f"Ошибка: {str(e)}")
    print("Текущий URL:", driver.current_url)
    driver.save_screenshot("error_screenshot.png")

finally:
    time.sleep(2)
    driver.quit()
    print("Браузер закрыт")