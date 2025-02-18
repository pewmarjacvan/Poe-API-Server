from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_stealth import stealth
import markdownify

class ChatBot:
    def start_driver(self, p_b_cookie, bot_name):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(options=options)
        stealth(self.driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
        
        self.driver.get(f"https://poe.com/")
        self.driver.add_cookie({"name": "p-b", "value": p_b_cookie})
        self.driver.get(f"https://poe.com/{bot_name}")

    def get_latest_message(self):
        bot_messages = self.driver.find_elements(By.XPATH, '//div[contains(@class, "Message_botMessageBubble__CPGMI")]//div[contains(@class, "Markdown_markdownContainer__UyYrv")]')
        if bot_messages:
            latest_message = bot_messages[-1]
            return markdownify.markdownify(latest_message.get_attribute('innerHTML'), heading_style="ATX")
        else:
            return None
    
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

    def kill_driver(self):
        if hasattr(self, "driver"):
            self.driver.quit()

    def __del__(self):
        if hasattr(self, "driver"):
            self.kill_driver()