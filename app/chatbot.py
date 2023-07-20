from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class ChatBot:
    def start_driver(self, p_b_cookie, bot_name):
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=options)
        self.driver.get(f"https://poe.com/")
        self.driver.add_cookie({"name": "p-b", "value": p_b_cookie})
        self.driver.get(f"https://poe.com/{bot_name}")

    def get_latest_message(self):
        messages = self.driver.find_elements(By.CLASS_NAME, "Markdown_markdownContainer__UyYrv")
        return messages[-1].text
    def abort_message(self):
        abort_button = self.driver.find_element(By.CLASS_NAME, "ChatStopMessageButton_stopButton__LWNj6")
        abort_button.click()

    def send_message(self, message):
        text_area = self.driver.find_element(By.CLASS_NAME, "GrowingTextArea_textArea__eadlu")
        text_area.send_keys(message)
        text_area.send_keys(Keys.RETURN)

    def clear_context(self):
        clear_button = self.driver.find_element(By.CLASS_NAME, "ChatBreakButton_button__EihE0")
        clear_button.click()

    def is_generating(self):
        stop_button_elements = self.driver.find_elements(By.CLASS_NAME, "ChatStopMessageButton_stopButton__LWNj6")
        return len(stop_button_elements) > 0
    
    def get_suggestions(self):
        suggestions_container = self.driver.find_elements(By.CLASS_NAME, "ChatMessageSuggestedReplies_suggestedRepliesContainer__JgW12")
        if not suggestions_container:
            return []
        suggestion_buttons = suggestions_container[0].find_elements(By.TAG_NAME, "button")
        return [button.text for button in suggestion_buttons]

    def restart_driver(self):
        self.kill_driver()
        self.start_driver()

    def kill_driver(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def __del__(self):
        if hasattr(self, "driver"):
            self.kill_driver()