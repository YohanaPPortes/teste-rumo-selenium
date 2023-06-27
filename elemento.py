from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome()

driver.get("https://playwright.dev/")



element = driver.find_element(By.XPATH, '//span[@class="DocSearch-Button-Placeholder"]')
element.click()

if element.is_displayed():
    print("O elemento está presente na página.")
else:
    print("O elemento não está presente na página.")

time.sleep(5)

driver.quit()