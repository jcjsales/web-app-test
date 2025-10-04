from utils.page_actions import PageActions

class Homepage:
    SEARCH_BUTTON = "//*[text()='Browse']/.."
    COOKIES_ADD_CHOICES_TITLE ="//p[text()='Cookies and Advertising Choices']"
    ACCEPT_COOKIES_BUTTON = "//button[@data-a-target='consent-banner-accept']"

    def __init__(self, driver):
        self.driver = driver
        self.page_actions = PageActions(self.driver)

    def click_search_button(self):
        self.page_actions.wait_for_element_and_click(self.SEARCH_BUTTON)

    def accept_cookies(self):
        self.page_actions.wait_for_element_and_click(self.ACCEPT_COOKIES_BUTTON)
