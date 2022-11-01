from behave import given, when
from selenium import webdriver
from page_object_model.locators.home_locators import HomePageLocators
from data.constants import Constants

@given('I go to AutomationPractice website on Chrome')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(Constants.URL_TEST)


@when('I search for a product on the searchbar')
def step_impl(context):
    context.driver.find_element(*HomePageLocators.SearchBar_Inp).send_keys("Dress")
    context.driver.find_element(*HomePageLocators.SearchBar_Btn).click()
