# pages/urun_sayfasi.py
from selenium.webdriver.common.by import By
from utilities.base import BasePage

class UrunSayfasi(BasePage):
    # Elementlerin locator'ları
    SEPETE_EKLE_BUTONU = (By.ID, "add-to-cart-button")  # Sepete ekle butonu
    SEPET_SAYISI = (By.ID, "nav-cart-count")  # Sepet sayısı

    def __init__(self, driver):
        super().__init__(driver)

    def sepete_ekle(self):
        # Ürünü sepete ekle
        self.tikla(self.SEPETE_EKLE_BUTONU)

    def urun_eklendi_mi(self):
        # Ürünün sepete eklendiğini kontrol et
        return "1" in self.element_metnini_al(self.SEPET_SAYISI)