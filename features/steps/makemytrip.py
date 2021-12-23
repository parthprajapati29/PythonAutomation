import time
from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains


@given('Open browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path='C:\\browserdriver\chromedriver.exe')
    context.driver.maximize_window()


@when('Open make my trip url')
def step_impl(context):
    context.driver.get("https://www.makemytrip.com/")
    time.sleep(3)


@when('Enter from')
def step_impl(context):
    context.driver.find_element_by_xpath("//li[@data-cy='account']").click()
    context.driver.find_element_by_xpath("//label[@for='fromCity']").click()
    context.driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("BOM")

    context.driver.execute_script('document.getElementsByTagName("li")[18].click()')
    context.driver.find_element_by_xpath("//input[@placeholder='To']").send_keys("ixb")
    context.driver.execute_script('document.getElementsByTagName("li")[19].click()')
    time.sleep(5)


@when('Select departure and return')
def departure_return(context):
    context.driver.execute_script('document.getElementsByClassName("dateInnerCell")[22].click()')
    context.driver.execute_script('document.getElementsByTagName("label")[3].click()')
    context.driver.execute_script('document.getElementsByClassName("dateInnerCell")[51].click()')
    # time.sleep(5)


@when('Select two travellers')
def departure_return(context):
    context.driver.execute_script('document.getElementsByTagName("label")[4].click()')
    context.driver.execute_script('document.getElementsByTagName("li")[19].click()')
    context.driver.execute_script('document.getElementsByTagName("button")[0].click()')
    context.driver.execute_script('document.getElementsByTagName("a")[23].click()')


@then('Redirect to next page where user has validate tag text for departure')
def tagValidation(context):
    time.sleep(5)
    getText = context.driver.find_element_by_xpath("//div[@class='paneView']/p/b").text
    print(getText)
    assert getText == "Mumbai → New Delhi", "executed"
