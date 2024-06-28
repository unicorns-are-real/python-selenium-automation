from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# wait for 5 sec
sleep(10)

# click Sign in button
driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()
# or driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']//span[text()='Sign in']")
# click Sign in button from the expanded side menu
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()

# verify search results
sleep(10)
searched_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
assert searched_text == actual_text, f"Expected header {searched_text} not in {actual_text}"
signin_button = driver.find_element(By.ID, "login").is_displayed(), 'Logi button not shown' # True / False
print('Test Passed')

driver.quit()

