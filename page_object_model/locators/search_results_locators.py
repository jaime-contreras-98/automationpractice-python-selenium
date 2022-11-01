from selenium.webdriver.common.by import By

class SearchResultsLocators(object):
    FirstProdAdd_Btn = (By.CSS_SELECTOR, "ul.product_list > li:nth-child(1) > div > div.right-block > div.button-container > a.ajax_add_to_cart_button")
    SecondProdAdd_Btn = (By.CSS_SELECTOR, "ul.product_list > li:nth-child(2) > div > div.right-block > div.button-container > a.ajax_add_to_cart_button")
