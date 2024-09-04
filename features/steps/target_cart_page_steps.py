from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#CART_HEADER =
#CRT_SUMMARY=
#CART_ITEM_TITLE =

@then('"Your cart is empty" message is shown')
def verify_empty_cart(context):
    assert context.driver.find_element(By.XPATH, "//*[text='Your cart is empty']").is_displayed()
    #OR
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, "h1.[clss*='StyledHeading']").text
    # assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"


@then('Check cart has individual item')
def verify_cart_item(context):
    context.driver.find_element(By.XPATH, '//div[contains(text(), "San Francisco Bay Coffee")]').is_displayed()

