from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CELL = (By.CSS_SELECTOR, 'div.cell-item-content')



@given('Open Target.com/circle')
def open_target_circle(context):
    context.driver.get('https://www.target.com/circle')


@then('{number_of_cells} are present')
def number_of_cells(context, number_of_cells):
    cells = context.driver.find_elements(*CELL)
    print(cells) #prints a list
    assert len(cells) == int(number_of_cells), f"Expected {number_of_cells} but got {len(cells)}"
