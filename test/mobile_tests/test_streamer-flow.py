from utils.page_actions import PageActions

class TestStreamerFlow:

    def test_browse_streamer_on_mobile(self, mobile_driver, pages):
        page_actions = PageActions(mobile_driver)
        pages.browse_page.close_dialog_if_visible()
        pages.homepage.accept_cookies()
        pages.homepage.click_search_button()
        pages.browse_page.input_search_field("Starcraft II")
        pages.browse_page.select_from_search_list(2)
        streamer_name = pages.browse_page.select_streamer_by_index_and_return_name(1)
        pages.channel_page.wait_for_live_channel_elements_to_be_visible()
        pages.channel_page.streamer_name_is_displayed(streamer_name)
        page_actions.capture_page_screenshot("mobile")
