import time

from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(executable_path='C:\\browserdriver\chromedriver.exe')


@when('open lander homepage')
def openHomePage(context):
    context.driver.get("https://freesamplesprousa.com/?cid=i739j&test=1")
    time.sleep(3)


@then('verify h2 text displayed on page')
def verifyLogo(context):
    time.sleep(3)
    status = context.driver.find_element_by_xpath("//*[contains(text(),'Confirm your email address')]").is_displayed()
    assert status is True


@then('close browser')
def closeBrowser(context):
    context.driver.close()


@when('Enter email "{data}" in email field')
def enterEmail(context, data):
    time.sleep(5)
    context.driver.find_element_by_xpath("//input[@type='email']").send_keys(data)


@when('Click on continue button')
def performClick(context):
    context.driver.find_element_by_xpath("//button[@type='submit']").click()


@then('User must redirect to registration page')
def CheckElementPresent(context):
    time.sleep(5)
    value = context.driver.find_element_by_xpath("//input[@id='firstName']").is_displayed()
    assert value is True
