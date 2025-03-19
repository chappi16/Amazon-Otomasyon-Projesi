# utilities/base.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def tikla(self, locator):
        # Belirtilen elementi tıklar
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def yazi_yaz(self, locator, metin):
        # Belirtilen elemente metin yazar
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(metin)

    def element_gorunuyor_mu(self, locator):
        # Belirtilen elementin görünür olup olmadığını kontrol eder
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).is_displayed()

    def element_metnini_al(self, locator):
        # Belirtilen elementin metnini alır
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text