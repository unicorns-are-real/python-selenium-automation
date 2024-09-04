from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    actual_word = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_word, f'Expected word {expected_result} not in {actual_word}'


@then('Page url has search term {expected_part_url}')
def verify_search_page_url(context, expected_part_url):
    url = context.driver.current_url
    assert expected_part_url in url, f'Expected {expected_part_url} not in {url}'
# do not provide logic for opening and killing the browser, it's already in the environment.py file
# steps should be separated with 2 blank lines