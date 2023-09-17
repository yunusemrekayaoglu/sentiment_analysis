import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
from tqdm import tqdm
import time
import os



def yorum_cek(urun_adi, urun_linki, sayfa_sayisi):
    try:
        os.mkdir("data")
        print(f"data adında yeni bir klasör oluşturuldu.")
    except FileExistsError:
        print(f"data adında bir klasör zaten var.")

    headers_param = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"}
    pages = sayfa_sayisi + 1
    liste = []
    yorumsira = 0
    for page in tqdm(range(1, pages), desc=f"{urun_adi} için yorumlar çekiliyor"):
        time.sleep(random.uniform(0.5, 1))
        istek = requests.get(f"{urun_linki}-yorumlari?sayfa={str(page)}", headers=headers_param)
        kaynak = BeautifulSoup(istek.content, "lxml")
        yorumlar = kaynak.find_all("div", {"class": "hermes-ReviewCard-module-dY_oaYMIo0DJcUiSeaVW"})
        for i in yorumlar:
            yorum = BeautifulSoup(str(i), "lxml")
            try:
                kisi_yorumu = yorum.find_all("span", {"itemprop": "description"})[0].text
            except:
                kisi_yorumu = str("yorum yok")
            yildiz = yorum.find_all("div", {"class": "star"})
            yildiz_sayisi = len(yildiz)
            if yildiz_sayisi >= 5:
                yildiz_sayisi = 5
            liste.append([kisi_yorumu, yildiz_sayisi])
    print(f"{urun_adi} için bütün yorumlar çekildi.\n")


    liste.sort(key=lambda x: x[1], reverse=True)  # Yıldız sayısına göre sıralama
    df = pd.DataFrame(liste, columns=["Yorum_Icerik", "Yildiz"])
    df = df.drop_duplicates()
    df.to_excel(f"{urun_adi}.xlsx", index=False)

    comments = df.copy()
    comments = comments[~comments["Yorum_Icerik"].str.contains("yorum yok")]
    comments.to_csv(".\data\yorumlar.csv", index=False)


urun_adi = input("Ürün adını giriniz: ")
urun_linki = input("Ürün linkini giriniz: ")
sayfa_sayisi = int(input("Kaç sayfa yorum çekmek istiyorsunuz: "))

yorum_cek(urun_adi = urun_adi, urun_linki = urun_linki, sayfa_sayisi = sayfa_sayisi)

