from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

try:
    driver.get("https://demo.opencart.com")
    print("Главная страница загружена")
    time.sleep(2)

    search_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='search']/input")
    ))
    search_input.send_keys("iPhone")
    print("Поисковое слово введено")
    time.sleep(2)

    search_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='search']/button")
    ))
    search_button.click()
    print("Кнопка поиска нажата")
    time.sleep(2)

    try:
        results = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='content']//h1[contains(text(), 'Search')]")
        ))
        print("Результаты поиска отображены")
    except:
        error_message = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//div[@id='content']//p[contains(text(), 'There is no product that matches the search criteria.')]")
        ))
        if error_message:
            print("Ошибка: Ничего не найдено")
        else:
            print("Неизвестная ошибка при поиске")

except Exception as e:
    print(f"Ошибка: {str(e)}")
    print("Текущий URL:", driver.current_url)
    driver.save_screenshot("error_screenshot.png")

finally:
    time.sleep(2)
    driver.quit()
    print("Браузер закрыт")