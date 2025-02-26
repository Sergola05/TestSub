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
    time.sleep(2)

    account_menu = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div")
    ))
    account_menu.click()
    print("Меню аккаунта открыто")
    time.sleep(2)

    register_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='top']/div/div[2]/ul/li[2]/div/ul/li[1]/a")
    ))
    register_option.click()
    print("Переход на страницу регистрации выполнен")
    time.sleep(2)


    first_name = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='input-firstname']")
    ))
    first_name.send_keys("Cергей")
    print("Имя заполнено")
    time.sleep(2)

    last_name = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='input-lastname']")
    ))
    last_name.send_keys("Иванов")
    print("Фамилия заполнена")
    time.sleep(2)

    email = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='input-email']")
    ))
    email.send_keys("isss@ls.com")
    print("Email заполнен")
    time.sleep(2)

    password = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//*[@id='input-password']")
    ))
    password.send_keys("Password123!")
    print("Пароль заполнен")
    time.sleep(2)


    agree_checkbox = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='form-register']/div/div/input")
    ))
    agree_checkbox.click()
    print("Согласие с условиями отмечено")
    time.sleep(2)

    register_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//*[@id='form-register']/div/button")
    ))
    register_button.click()
    print("Кнопка 'Зарегистрироваться' нажата")
    time.sleep(2)


    success_message = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//div[@id='content']//h1[contains(text(), 'Your Account Has Been Created!')]")
    ))
    if success_message:
        print("Регистрация успешна!")
    else:
        print("Регистрация не удалась")
    time.sleep(2)

except Exception as e:
    print(f"Ошибка: {str(e)}")
    print("Текущий URL:", driver.current_url)
    driver.save_screenshot("error_screenshot.png")

finally:
    time.sleep(2)
    driver.quit()
    print("Браузер закрыт")