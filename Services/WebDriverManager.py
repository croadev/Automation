from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverManager:
    def __init__(self, url):
        self.__driver = self.__setUp(url)
        self.wait = WebDriverWait(self.__driver, 20)

    def __setUp(self, url):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-gpu')

        # Instalar y configurar el servicio de ChromeDriver
        # service = Service(ChromeDriverManager().install())

        service = Service(r"C:\Users\CROA\AppData\Local\Programs\Python\Python312\chromedriver.exe")

        self.__driver = webdriver.Chrome(
            service=service) #options=chrome_options)
        self.__driver.set_window_size(1024, 600)
        self.__driver.maximize_window()
        self.__driver.implicitly_wait(15)
        self.__driver.get(url)
        return self.__driver

    def click(self, by: By, value: str):
        element = self.wait.until(EC.element_to_be_clickable((by, value)))
        element.click()

    def click2(self, by: By, value: str):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        element.click()

    def send_keys_delay(self, by: By, xpath: str, keys, delay=0.25):
        element = self.wait.until(EC.presence_of_element_located((by, xpath)))
        for key in keys:
            time.sleep(delay)
            element.send_keys(key)

    def send_keys(self, by: By, value: str, keys: str):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        element.click()
        element.send_keys(keys)

    def write(self, by: By, value: str, keys: str):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        element.send_keys(keys)

    def select_dropdown(self, by: By, value: str, visible_text: str):
        element = Select(self.wait.until(
            EC.presence_of_element_located((by, value))))
        element.select_by_visible_text(visible_text)

    def move_to_element(self, by: By, value: str):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        actions = ActionChains(self.__driver)
        actions.move_to_element(element).perform()

    def move(self, by: By, value: str):
        element = self.wait.until(EC.presence_of_element_located((by, value)))
        self.__driver.execute_script("arguments[0].scrollIntoView();", element)

    def select_by_value(self, by: By, value: str, value_text: str):
        element = Select(self.wait.until(
            EC.presence_of_element_located((by, value))))
        element.select_by_value(value_text)

    def wait_desappear(self, by: By, value: str):
        print(self.wait.until(EC.invisibility_of_element_located((by, value))))

    def wait_appear(self, by: By, value: str):
        return self.wait.until(EC.presence_of_element_located((by, value)))

    def get_driver(self):
        return self.__driver

    def get_url(self):
        return self.__driver.current_url

    def quit(self):
        self.__driver.quit()

    def __getattr__(self, name):
        return getattr(self.__driver, name)
