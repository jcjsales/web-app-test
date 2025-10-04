import pytest
from utils.driver_manager import create_mobile_emulator
from mobile_pages.homepage import Homepage
from mobile_pages.browse_page import BrowsePage
from mobile_pages.channel_page import ChannelPage

@pytest.fixture(params=["Samsung Galaxy S20 Ultra", "Samsung Galaxy S8+", "Pixel 7"], scope="function")
def mobile_driver(request):
    device_name = request.param
    mobile_driver = create_mobile_emulator(device_name)
    mobile_driver.get("https://m.twitch.tv/")
    yield mobile_driver
    mobile_driver.quit()

@pytest.fixture
def pages (mobile_driver):
    class Pages:
        def __init__(self, mobile_driver):
            self.homepage = Homepage(mobile_driver)
            self.browse_page = BrowsePage(mobile_driver)
            self.channel_page = ChannelPage(mobile_driver)
    return Pages(mobile_driver)
