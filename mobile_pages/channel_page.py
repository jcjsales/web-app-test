from selenium.webdriver.common.by import By

from utils.page_actions import PageActions

class ChannelPage:
    CHANNEL_LIVE_SCREEN = "//*[@id='channel-live-overlay']//div[@data-a-target='player-overlay-click-handler']"
    CHANNEL_AVATAR = "//*[starts-with(@class, 'ScAvatar-sc')]"
    CHANNEL_STREAMER_NAME = "//*[starts-with(@class, 'ScAvatar-sc')]/../../..//h1"
    CHANNEL_STREAM_TITLE = "//*[starts-with(@class, 'ScAvatar-sc')]/../../..//p[1]"
    CHANNEL_LIVE_CHAT_SCROLL = "//*[@data-a-target='chat-scroller']"
    CHANNEL_LIVE_WELCOME_TO_CHATROOM_TEXT = "//*[text()='Welcome to the chat room!']"

    def __init__(self, driver):
        self.driver = driver
        self.page_actions = PageActions(driver)

    def wait_for_live_channel_elements_to_be_visible(self):
        self.page_actions.wait_for_element_to_be_visible(self.CHANNEL_LIVE_SCREEN)
        self.page_actions.wait_for_element_to_be_visible(self.CHANNEL_AVATAR)
        self.page_actions.wait_for_element_to_be_visible(self.CHANNEL_STREAMER_NAME)
        self.page_actions.wait_for_element_to_be_visible(self.CHANNEL_STREAM_TITLE)
        self.page_actions.wait_for_element_to_be_visible(self.CHANNEL_LIVE_CHAT_SCROLL)
        self.page_actions.wait_for_element_to_be_visible(self.CHANNEL_LIVE_WELCOME_TO_CHATROOM_TEXT)

    def streamer_name_is_displayed (self, expected_streamer_name):
        element = self.driver.find_element(By.XPATH, self.CHANNEL_STREAMER_NAME)
        assert element.text == expected_streamer_name
