import pandas as pd
from main import gelirler, giderler, personel, deneme_sinavlari, paketler, ogrenciler

#Aylık Toplam Gelir
gelirler["ay"] = gelirler["tarih"].dt.to_period("M")
aylik_gelir = gelirler.groupby("ay")["tutar"].sum()
print(aylik_gelir)

#Aylık Toplam Giderler
giderler["ay"] = giderler["tarih"].dt.to_period("M")
aylik_gider = giderler.groupby("ay")["tutar"].sum()
print(aylik_gider)

#Aylara göre Gelir - Gider Karşılaştırması
print("\n--- NET ------")
net_kar = aylik_gelir - aylik_gider
print(net_kar)

#Toplam gelir, gider, kar
print(f"Toplam Gelir: {gelirler["tutar"].sum():,.0f} TL")
print(f"Toplam Gider: {giderler["tutar"].sum():,.0f} TL")
print(f"Net Kar: {gelirler["tutar"].sum() - giderler["tutar"].sum():,.0f} TL")

#En Çok satan paket
print("\n--- EN ÇOK SATAN PAKET TUR----")
paket_gelir = gelirler.groupby("paket_id")["tutar"].sum().reset_index()
paket_gelir = paket_gelir.merge(paketler[["paket_id","paket_adi"]], on="paket_id")
paket_gelir = paket_gelir.sort_values("tutar", ascending=False)
print(paket_gelir[["paket_adi","tutar"]])

#Ödeme Yöntemlerine göre gelir dağılımı
print("\n---Ödeme Yönetmi Dağılımı----")
odeme_dagilim = gelirler.groupby("odeme_yontemi")["tutar"].sum().sort_values(ascending= False)
print(odeme_dagilim)

#Taksitli vs Peşin
print("\n----Taksit & Peşin-----")
taksitandpesin = gelirler.groupby("taksit_mi")["tutar"].sum()
print(taksitandpesin)

#Gider Kategorileri
print("\n----Giderli Kategorilere Göre-----")
giderktg = giderler.groupby("kategori")["tutar"].sum().sort_values(ascending=False)
print(giderktg)

#Personel Maaş
print("\n----- Personel Analizi -----")
pozisyon_maas = personel.groupby("pozisyon")["maas"].sum()
print(pozisyon_maas)

#Deneme Sınavı Analiz
print("\n-----Deneme Sınav Analizi-----")
print(f"Toplam Yapılan Deneme Sınavı Sayısı= {len(deneme_sinavlari)}")
print(f"Toplam Katılımcı: {deneme_sinavlari["katilimci_sayisi"].sum()}")
print(f"Sınav Gelirleri: {deneme_sinavlari["toplam_gelir"].sum():,.0f} TL")

#ÖĞRENCİ ANALİZİZ
print("\n SInıf Türleri")
sinif_dagilim = ogrenciler["sinif_turu"].value_counts()
print(sinif_dagilim)