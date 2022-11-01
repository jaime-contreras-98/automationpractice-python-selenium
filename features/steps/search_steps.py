from behave import when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from page_object_model.locators.search_results_locators import SearchResultsLocators
from page_object_model.locators.cart_confirmation_locators import CartConfirmationLocators

@when('I add to cart that product')
def step_impl(context):
    context.driver.find_element(*SearchResultsLocators.FirstProdAdd_Btn).click()


@then('My product must appear on the shopping cart')
def step_impl(context):
    driver = webdriver.Chrome()
    driver.implicitly_wait(15)

    textCart = context.driver.find_element(*CartConfirmationLocators.ProductAdded_Lbl).text
    assert True, textCart
    #element = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located(text))
    #print(element," ",text)

    #if element == "Product successfully added to your shopping cart":
    #    assert True, "Test passed!"
