import pandas as pd
import datetime

ogrenciler = pd.read_csv("data/ogrenciler.csv")
gelirler = pd.read_csv("data/gelirler.csv")
giderler = pd.read_csv("data/giderler.csv")
paketler = pd.read_csv("data/paketler.csv")
personel = pd.read_csv("data/personel.csv")
deneme_sinavlari = pd.read_csv("data/deneme_sinavlari.csv")

print(gelirler.shape)
print(gelirler.head())
print(gelirler.dtypes)
print(gelirler.isnull().sum())


#gelirler["tutar"] = (gelirler["tutar"].str.replace("₺","",regex=False).str.replace(".","",regex=False).str.replace(",",".",regex=False).astype(float))
#gelirler["tarih"] = pd.to_datetime(gelirler["tarih"], format="mixed", dayfirst=True)

def para_temizle(sutun):
    return (sutun
            .str.replace("₺","",regex=False)
            .str.replace(".","",regex=False)
            .str.replace(",",".",regex=False)
            .str.replace("%","",regex=False)
            .str.strip()
            .astype(float)
            )
gelirler["tutar"] = para_temizle(gelirler["tutar"])
gelirler["tarih"] = pd.to_datetime(gelirler["tarih"],format="mixed",dayfirst=True)

giderler["tarih"]= pd.to_datetime(giderler["tarih"],format="mixed",dayfirst=True)
giderler["tutar"]= para_temizle(giderler["tutar"])

ogrenciler["dogum_tarihi"] = pd.to_datetime(ogrenciler["dogum_tarihi"],format="mixed",dayfirst=True)

paketler["indirim_orani"] = para_temizle(paketler["indirim_orani"])

personel["maas"] = para_temizle(personel["maas"])
personel["ise_baslama_tarihi"] = pd.to_datetime(personel["ise_baslama_tarihi"],format="mixed",dayfirst=True)

deneme_sinavlari["tarih"] = pd.to_datetime(deneme_sinavlari["tarih"],format="mixed",dayfirst=True)
deneme_sinavlari["ucret"] = para_temizle(deneme_sinavlari["ucret"])
deneme_sinavlari["toplam_gelir"] = para_temizle(deneme_sinavlari["toplam_gelir"])

print("Düzenlemeler Yapıldı.")

print(giderler.dtypes)
print(personel.dtypes)
print(deneme_sinavlari.dtypes)
print(gelirler.dtypes)
