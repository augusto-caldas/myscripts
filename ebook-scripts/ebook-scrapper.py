import time

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Setup Selenium
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

while True:
    # Prompt user about ebook info
    url = input("Enter the ebook URL >> ")
    num_pages = int(input("Enter the number of pages to download >> "))
    ebook_name = input("Enter ebook name >> ")
    save_folder = os.path.join("ebooks", ebook_name)

    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    driver.get(url)
    # Wait for user to start scrapper
    input("Press any key to start...")

    # Download pages
    for page in range(1, num_pages + 1):
        # Take screenshot
        screenshot_path = os.path.join(save_folder, f"page_{page}.png")
        driver.save_screenshot(screenshot_path)

        # Press right arrow to go to next page
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys(Keys.ARROW_RIGHT)

        # Wait page to load
        time.sleep(0.5)

    if input("Press enter to crop next ebook or 0 to quit") == "0":
        exit()
