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
    print("Страница загружена")

    currency_switcher = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='form-currency']/div/a")
    ))
    currency_switcher.click()
    print("Меню валют открыто")

    wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='form-currency']/div/ul")
    ))
    print("Список валют отображен")

    euro_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='form-currency']/div/ul/li[1]/a")
    ))
    euro_option.click()
    print("Выбрана валюта EUR")

    wait.until(EC.text_to_be_present_in_element(
        (By.XPATH, "//*[@id='form-currency']/div/a/strong"), "€"
    ))
    print("Валидация успешна: валюта EUR активна")

except Exception as e:
    print(f"Ошибка: {str(e)}")
    print("Текущий URL:", driver.current_url)
    driver.save_screenshot("error_screenshot.png")

finally:
    time.sleep(2)
    driver.quit()
    print("Браузер закрыт")