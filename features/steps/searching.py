import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from searching_filtration import SearchingFiltration

class Searching(webdriver.Chrome):
    def __init__(self, driver_path="./chromedriver.exe"):
        self.driver_path = driver_path
        os.environ['PATH'] += os.pathsep + self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Searching, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def close_page(self):
        self.quit()

    def land_first_page(self):
        self.get("https://www.amazon.com/")

    def content_search(self, content):
        self.find_element(By.ID, "twotabsearchtextbox").send_keys(content)

    def click_search(self):
        search_button = self.find_element(By.ID, 'nav-search-submit-button')
        search_button.click()

    def apply_filtrations(self):
        filtration = SearchingFiltration(driver=self)
        filtration.sort_custom_review()
        filtration.apply_age_range("5 to 7")

    def add_item_to_cart(self, number):
        num_list = list(range(2, int(number) + 2))
        item_list = []
        total_number = 0
        for index in num_list:
            element = self.find_element(By.CSS_SELECTOR, f"img[data-image-index='{index}']")
            element.click()
            title = self.find_element(By.CSS_SELECTOR, 'h1[id="title"]')
            item_list.append(title.text)
            add_card = self.find_element(By.ID, "add-to-cart-button")
            add_card.click()
            total_number += 1
            self.back()
            self.back()
        return total_number, item_list

    def check_cart(self, number, item_list):
        cart = self.find_element(By.ID, "nav-cart-count-container")
        cart.click()
        all_item = self.find_elements(By.CLASS_NAME, "sc-list-item-content")
        find_number = 0
        for element in item_list:
            for item in all_item:
                if item.text[0:10] in element[0:10]:
                    find_number += 1
        return find_number

