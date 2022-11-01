from selenium.webdriver.common.by import By

class HomePageLocators(object):
    SearchBar_Inp = (By.ID, "search_query_top")
    SearchBar_Btn = (By.NAME, "submit_search")
