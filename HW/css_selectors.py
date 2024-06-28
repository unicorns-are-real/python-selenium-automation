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

# CSS, connect by ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
# same as By.ID which will be preferred: driver.find_element(By.ID, 'twotabsearchtextbox')
# CSS, connect by class
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us.icp-nav-flag') #multiple classes
# by TAG + class / ID / attr (if necessary for locating elements)
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox') # not for IDs coz it's unique
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-us.icp-nav-flag')
# by attr
driver.find_element(By.CSS_SELECTOR,"[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][aria-label='Search Amazon']")
# by attr + id + class
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox.nav-input[placeholder='Search Amazon']")
# Partial attr: 'contain' use *
driver.find_element(By.CSS_SELECTOR, "[aria-describedby*='Dropdown']")
driver.find_element(By.CSS_SELECTOR, "[class*='search-dropdown']") # treat classes and IDs as attr
# To connect to a child element inside a parent element: separate them by space
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")

