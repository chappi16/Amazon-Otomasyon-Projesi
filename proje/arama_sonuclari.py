# pages/arama_sonuclari.py
from selenium.webdriver.common.by import By
from utilities.base import BasePage

class AramaSonuclariSayfasi(BasePage):
    # Elementlerin locator'ları
    ARAMA_SONUCLARI = (By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")  # Arama sonuçları
    IKINCI_SAYFA_BUTONU = (By.CSS_SELECTOR, "a.s-pagination-item[aria-label='2. sayfaya git']")  # 2. sayfa butonu
    IKINCI_SAYFA_AKTIF = (By.CSS_SELECTOR, "span.s-pagination-item.s-pagination-selected")  # Aktif sayfa

    def __init__(self, driver):
        super().__init__(driver)

    def sonuclari_dogrula(self):
        # Arama sonuçlarının görünür olup olmadığını kontrol et
        return self.element_gorunuyor_mu(self.ARAMA_SONUCLARI)

    def ikinci_sayfaya_git(self):
        # 2. sayfaya git
        self.tikla(self.IKINCI_SAYFA_BUTONU)

    def ikinci_sayfa_dogrula(self):
        # 2. sayfanın aktif olup olmadığını kontrol et
        return "2" in self.element_metnini_al(self.IKINCI_SAYFA_AKTIF)

    def ucuncu_urunu_tikla(self):
        # 3. ürüne tıkla
        urunler = self.driver.find_elements(*self.ARAMA_SONUCLARI)
        urunler[2].click()