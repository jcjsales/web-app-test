from selenium.common import NoSuchElementException

from utils.page_actions import PageActions
from selenium.webdriver.common.by import By

class BrowsePage:
    SEARCH_FIELD = "//input[@type='search']"
    SEARCH_LIST_BY_INDEX = "//ul//li[{}]"
    STREAMER_NAME_ELEMENT = "(//*[@id='page-main-content-wrapper']//button)[{}]"
    STREAMER_NAME_CHANNEL_LIST = "(//*[@id='page-main-content-wrapper']//button)[1]//h2"
    DIALOG_CLOSE_BUTTON = "//*[@class='Layout-sc-1xcs6mc-0 haxzqw']"
    DIALOG_CLOSE_BUTTON_JS = "document.getElementsByClassName('Layout-sc-1xcs6mc-0 haxzqw')[0].click()"


    def __init__(self, driver):
        self.driver = driver
        self.page_actions = PageActions(self.driver)

    def input_search_field(self, text):
        self.page_actions.wait_for_textfield_and_input_text(self.SEARCH_FIELD, text)

    def select_from_search_list(self, index):
        search_result_xpath = self.SEARCH_LIST_BY_INDEX.format(index)
        self.page_actions.wait_for_element_and_click(search_result_xpath)

    def select_streamer_by_index_and_return_name(self, index):
        streamer_element_by_name = self.STREAMER_NAME_ELEMENT.format(index)
        self.page_actions.wait_for_element_and_click(streamer_element_by_name)
        element = self.driver.find_element(By.XPATH, self.STREAMER_NAME_CHANNEL_LIST)
        selected_streamer_name = element.text
        return selected_streamer_name

    def close_dialog_if_visible(self):
        try:
            dialog_close_element = self.driver.find_element(By.XPATH, self.DIALOG_CLOSE_BUTTON)
            if dialog_close_element.is_displayed():
                self.driver.execute_script(self.DIALOG_CLOSE_BUTTON_JS)
        except NoSuchElementException:
            pass
