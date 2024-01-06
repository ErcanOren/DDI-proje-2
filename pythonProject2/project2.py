from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver_path = "C:\PROGRAM SETUP\chromedriver.exe"
browser = "webdriver.Chrome(driver_path)"

kitap_adi = input("Kitap adını giriniz : ")
yayin_evi = input("Yayınevini giriniz : ")


def bkm_kitap():
    browser.get("https://www.google.com/")

    bkm_kitap_veri_girisi = browser.find_element_by_css_selector(".gLFyf")
    bkm_kitap_veri_girisi.send_keys(kitap_adi + " " + yayin_evi + " " + " site:bkmkitap.com")
    time.sleep(2)

    bkm_kitap_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    bkm_kitap_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/a")
    bkm_kitap_tikla.click()

    bkm_kitap_sayfa = browser.page_source
    bkm_kitap_soup = BeautifulSoup(bkm_kitap_sayfa, "lxml")

    bkm_kitap_bilgiler = bkm_kitap_soup.find("div", attrs={"id": "productInfo"})

    bkm_kitap_adi = bkm_kitap_bilgiler.find("h1").text
    bkm_kitap_yayin_evi = bkm_kitap_bilgiler.find("a").text.strip()

    bkm_kitap_yazar_adi = bkm_kitap_bilgiler.find("a", attrs={"id": "productModelText"}).text.strip()

    bkm_kitap_fiyat = bkm_kitap_soup.find("span", attrs={"class": "product-price"}).text

    print(
        "BKM KİTAP = " + bkm_kitap_adi + " , " + bkm_kitap_yayin_evi + " , " + bkm_kitap_yazar_adi + " , " + bkm_kitap_fiyat)


def kitapyurdu():
    browser.get("https://www.google.com/")

    kitapyurdu_veri_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    kitapyurdu_veri_girisi.send_keys(kitap_adi + " " + yayin_evi + " " + " site:kitapyurdu.com")
    time.sleep(2)

    kitapyurdu_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    kitapyurdu_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/a")
    kitapyurdu_tikla.click()

    kitapyurdu_sayfa = browser.page_source
    kitapyurdu_soup = BeautifulSoup(kitapyurdu_sayfa, "lxml")

    kitapyurdu_kitap_adi = kitapyurdu_soup.find("h1", attrs={"class": "pr_header__heading"}).text
    kitapyurdu_yazar_adi = kitapyurdu_soup.find("a", attrs={"class": "pr_producers__link"}).text.strip()
    kitapyurdu_yayin_evi = kitapyurdu_soup.find("div", attrs={"class": "pr_producers__publisher"}).text.strip()
    kitapyurdu_fiyat = kitapyurdu_soup.find("div", attrs={"class": "price__item"}).text.strip()

    print(
        "KİTAP YURDU = " + kitapyurdu_kitap_adi + " , " + kitapyurdu_yazar_adi + " , " + kitapyurdu_yayin_evi + " , " + kitapyurdu_fiyat)


def dr_kitap():
    browser.get("https://www.google.com/")

    dr_veri_girisi = browser.find_element_by_css_selector(".gLFyf.gsfi")
    dr_veri_girisi.send_keys(kitap_adi + " " + yayin_evi + " " + " site:dr.com.tr")
    time.sleep(2)

    dr_veri_girisi.send_keys(Keys.ENTER)
    time.sleep(2)

    dr_tikla = browser.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/a")
    dr_tikla.click()

    dr_sayfa = browser.page_source

    dr_soup = BeautifulSoup(dr_sayfa, "lxml")
    dr_yazar_adi = dr_soup.find("span", attrs={"class": "name"}).text
    dr_yayin_evi = dr_soup.find("h2").text
    dr_kitap_adi = dr_soup.find("h1", attrs={"class": "product-name"}).text.strip()
    dr_fiyat = dr_soup.find("span", attrs={"id": "salePrice"}).text

    print("DR KİTAP = " + dr_kitap_adi + " , " + dr_yayin_evi + " , " + dr_yazar_adi + " , " + dr_fiyat)


bkm_kitap()
kitapyurdu()
dr_kitap()
