# pages/sepet_sayfasi.py
from selenium.webdriver.common.by import By
from utilities.base import BasePage

class SepetSayfasi(BasePage):
    # Elementlerin locator'ları
    SEPET_ELEMANI = (By.CSS_SELECTOR, "div.sc-list-item-content")  # Sepetteki ürün
    SIL_BUTONU = (By.CSS_SELECTOR, "input[value='Sil']")  # Sil butonu
    BOS_SEPET_MESAJI = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")  # Boş sepet mesajı

    def __init__(self, driver):
        super().__init__(driver)

    def sepet_sayfasi_dogrula(self):
        # Sepet sayfasında olduğunu doğrula
        return self.element_gorunuyor_mu(self.SEPET_ELEMANI)

    def urunu_sil(self):
        # Ürünü sepetten sil
        self.tikla(self.SIL_BUTONU)

    def urun_silindi_mi(self):
        # Ürünün silindiğini doğrula
        return self.element_gorunuyor_mu(self.BOS_SEPET_MESAJI)