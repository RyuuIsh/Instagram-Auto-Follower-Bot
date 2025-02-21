import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Load environment variables
load_dotenv()

SIMILAR_ACCOUNT = "pudgypenguins"
USERNAME = os.getenv("INSTA_USERNAME")
PASSWORD = os.getenv("INSTA_PASSWORD")


class InstaFollower:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(5)

        # Dismiss Cookie Warning (if present)
        try:
            decline_cookies = self.driver.find_element(By.XPATH, "//button[text()='Decline optional cookies']")
            decline_cookies.click()
        except NoSuchElementException:
            pass  # If no cookie warning, continue

        # Enter Login Credentials
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")
        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        # Dismiss Save Login & Notifications Prompt
        time.sleep(5)
        self.dismiss_popup("//button[contains(text(), 'Not now')]")  # Save login info
        self.dismiss_popup("//button[contains(text(), 'Not Now')]")  # Notifications

    def dismiss_popup(self, xpath):
        """Attempts to dismiss a popup if found."""
        try:
            button = self.driver.find_element(By.XPATH, xpath)
            button.click()
        except NoSuchElementException:
            pass

    def find_followers(self):
        """Opens the follower list of the target account and scrolls to load more followers."""
        time.sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(5)

        # Open followers modal
        try:
            followers_modal = self.driver.find_element(By.XPATH, "//div[@role='dialog']//ul")
            for _ in range(10):  # Scroll multiple times to load followers
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_modal)
                time.sleep(2)
        except NoSuchElementException:
            print("⚠️ Followers modal not found.")

    def follow(self):
        """Clicks follow buttons for users in the list."""
        time.sleep(3)
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button._acan._acap._acas._aj1-")

        for button in follow_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                self.dismiss_popup("//button[contains(text(), 'Cancel')]")  # Handles "Unfollow" popup

        print("✅ Successfully followed users!")

    def close_browser(self):
        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.close_browser()
