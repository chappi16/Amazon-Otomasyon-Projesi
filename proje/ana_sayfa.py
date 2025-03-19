# pages/ana_sayfa.py
from selenium.webdriver.common.by import By
from utilities.base import BasePage

class AnaSayfa(BasePage):
    # Elementlerin locator'ları
    ARAMA_KUTUSU = (By.ID, "twotabsearchtextbox")  # Arama kutusu
    ARAMA_BUTONU = (By.ID, "nav-search-submit-button")  # Arama butonu

    def __init__(self, driver):
        super().__init__(driver)

    def arama_yap(self, urun_adi):
        # Arama kutusuna ürün adını yaz ve ara
        self.yazi_yaz(self.ARAMA_KUTUSU, urun_adi)
        self.tikla(self.ARAMA_BUTONU)