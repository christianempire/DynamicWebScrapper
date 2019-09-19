import time
from selenium import webdriver

class DynamicWebScrapper():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_content(self, content_css_class = '_1ct7vg8q'):
        try:
            self.driver.maximize_window()
            content = self.driver.find_element_by_class_name(content_css_class).text.replace('\n', ' ')
            if len(content) > 0:
                return content
            else:
                time.sleep(1)
                return self.get_content(content_css_class)
        except:
            time.sleep(1)
            return self.get_content(content_css_class)

    def set_url(self, url):
        self.driver.get(url)