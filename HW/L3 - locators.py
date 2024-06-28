# amazon logo
from selenium.webdriver.common.by import By
$$('.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')
# create account header
$$('h1.a-spacing-small')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
# your name field
$$('#ap_customer_name')
driver.find_element(By.ID, 'ap_customer_name')
# email field
$$('#ap_email')
driver.find_element(By.ID, 'ap_email')
# password field
$$('#ap_password')
driver.find_element(By.ID, 'ap_password')
# i password must be at least 6 characters
$$("div.a-box.a-alert-inline.a-alert-inline-info")
driver.find_element(By.CSS_SELECTOR, 'div.a-box.a-alert-inline.a-alert-inline-info')
# re-enter password
driver.find_element(By.ID, 'ap_password_check')
# create your amazon account button
driver.find_element(By.ID, 'continue')
# conditions of use
$x("//a[contains(@href, 'ap_register_notification_condition_of_use')]")
$x("//div[@id='legalTextRow']//a[text()='Conditions of Use']")
# privacy notice
$x("//div[@id='legalTextRow']//a[text()='Privacy Notice']")
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[text()='Privacy Notice']")
# sign in
$$("a.a-link-emphasis")
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis')