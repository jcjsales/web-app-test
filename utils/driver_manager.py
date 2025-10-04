from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def create_mobile_emulator(device_name):
    mobile_emulation = {"deviceName": device_name}  #iPhone 14 Pro Max
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--disable-features=IntentPicker")
    chrome_options.add_argument("--disable-features=EnableEphemeralTab")
    chrome_options.add_argument("--disable-features=OpenInAppBanner")
    return webdriver.Chrome(options=chrome_options)