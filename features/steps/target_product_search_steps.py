from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target.com')
def open_target_com(context):
    # open page in the browser
    context.driver.get('https://target.com/')


@when('Search for coffee')
def search_product(context):
    # input word to a search field
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    # click on search button
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(30)


@then('Search results for coffee are shown')
def verify_search_results_correct(context):
    actual_word = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'coffee' in actual_word, f'Expected word coffee not in {actual_word}'
    print('Test case passed')

# do not provide logic for opening and killing the browser, it's already in the environment.py file
# steps should be separated with 2 blank lines
