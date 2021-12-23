import time

from behave import *
from selenium import webdriver


@when('Open HRM homepage')
def openurl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")


@when('Enter username "{username}" and password  "{password}"')
def enterData(context, username, password):
    context.driver.find_element_by_id("txtUsername").send_keys(username)
    context.driver.find_element_by_id("txtPassword").send_keys(password)


@when('Click on login button')
def buttonClick(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('User must succesfully login to Dashboard page')
def checkText(context):
    data = context.driver.find_element_by_xpath("//div[@class='head']/h1").text
    assert data == "Dashboard"
