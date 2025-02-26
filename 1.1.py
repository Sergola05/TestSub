import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://demo.opencart.com/")
    time.sleep(3)

    macbook_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='product-thumb']//h4/a"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", macbook_element)
    time.sleep(1)
    actions = ActionChains(driver)
    actions.move_to_element(macbook_element).click().perform()
    print("Клик по MacBook выполнен!")

    WebDriverWait(driver, 10).until(EC.url_contains("product/macbook"))
    print("Переход на страницу MacBook успешен!")

    image_thumbnails = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='col-sm']//a/img"))
    )
    for thumbnail in image_thumbnails:
        actions.move_to_element(thumbnail).click().perform()
        print(f"Клик по картинке {thumbnail.get_attribute('src')} выполнен!")
        time.sleep(1)

    main_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='image magnific-popup']//a/img"))
    )
    print(f"Текущее изображение товара: {main_image.get_attribute('src')}")
except Exception as e:
    print(f"Ошибка во время выполнения теста: {e}")
finally:
    driver.quit()
