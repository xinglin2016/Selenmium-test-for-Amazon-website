from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class SearchingFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def apply_age_range(self, age_group):
        element_selected = ""
        elements = self.driver.find_elements(By.CSS_SELECTOR, "a[class='a-link-normal s-navigation-item']")
        for element in elements:
            if element.text == f'{age_group} Years':
                element_selected = element
        element_selected.click()

    def sort_custom_review(self):
        drop_down = self.driver.find_element(By.ID, 'a-autoid-0-announce')
        drop_down.click()
        element = self.driver.find_element(By.ID, 's-result-sort-select_3')
        element.click()
