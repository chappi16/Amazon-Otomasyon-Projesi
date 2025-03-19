# tests/test_amazon.py
import pytest
from selenium import webdriver
from pages.ana_sayfa import AnaSayfa
from pages.arama_sonuclari import AramaSonuclariSayfasi
from pages.urun_sayfasi import UrunSayfasi
from pages.sepet_sayfasi import SepetSayfasi

@pytest.fixture
def driver():
    # Tarayıcıyı başlat
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com.tr/")
    yield driver
    # Tarayıcıyı kapat
    driver.quit()

def test_amazon_otomasyon(driver):
    # Sayfa sınıflarını başlat
    ana_sayfa = AnaSayfa(driver)
    arama_sonuclari = AramaSonuclariSayfasi(driver)
    urun_sayfasi = UrunSayfasi(driver)
    sepet_sayfasi = SepetSayfasi(driver)

    # Ana sayfada olduğunu doğrula
    assert "Amazon.com.tr" in driver.title

    # 'samsung' için arama yap
    ana_sayfa.arama_yap("samsung")

    # Arama sonuçlarını doğrula
    assert arama_sonuclari.sonuclari_dogrula()

    # 2. sayfaya git ve doğrula
    arama_sonuclari.ikinci_sayfaya_git()
    assert arama_sonuclari.ikinci_sayfa_dogrula()

    # 3. ürüne tıkla
    arama_sonuclari.ucuncu_urunu_tikla()

    # Ürün sayfasında olduğunu doğrula
    assert "Samsung" in driver.title

    # Ürünü sepete ekle
    urun_sayfasi.sepete_ekle()

    # Ürünün sepete eklendiğini doğrula
    assert urun_sayfasi.urun_eklendi_mi()

    # Sepet sayfasına git
    driver.get("https://www.amazon.com.tr/gp/cart/view.html")

    # Sepet sayfasını ve ürünü doğrula
    assert sepet_sayfasi.sepet_sayfasi_dogrula()

    # Ürünü sil ve silindiğini doğrula
    sepet_sayfasi.urunu_sil()
    assert sepet_sayfasi.urun_silindi_mi()

    # Ana sayfaya dön ve doğrula
    driver.get("https://www.amazon.com.tr/")
    assert "Amazon.com.tr" in driver.title