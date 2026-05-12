import sqlite3
import pandas as pd
from main import gelirler,giderler,personel,deneme_sinavlari,paketler,ogrenciler

conn = sqlite3.connect("dershane.db")

gelirler.to_sql("gelirler",conn, if_exists="replace", index=False)
giderler.to_sql("giderler",conn, if_exists="replace", index=False)
personel.to_sql("personel",conn, if_exists="replace", index=False)
deneme_sinavlari.to_sql("deneme_sinavlari",conn, if_exists="replace", index=False)
paketler.to_sql("paketler",conn, if_exists="replace", index=False)
ogrenciler.to_sql("ogrenciler",conn, if_exists="replace", index=False)


sorgu1 = """SELECT strftime("%Y-%m", tarih)as ay, SUM(tutar) as toplam_gelir FROM gelirler GROUP BY ay ORDER BY ay"""
print("── Aylık Toplam Gelir ──")
print(pd.read_sql(sorgu1, conn))
sorgu2 ="""SELECT paketler.paket_adi,SUM(gelirler.tutar) as toplam_gelir, COUNT(*) as satis_adedi FROM gelirler JOIN paketler ON gelirler.paket_id = paketler.paket_id GROUP BY paketler.paket_adi ORDER BY toplam_gelir DESC"""
print("\n── Paket Bazında Gelir ──")
print(pd.read_sql(sorgu2, conn))
sorgu3 = """SELECT kategori,SUM(tutar) as toplam_gider, ROUND(SUM(tutar) * 100.0 / (SELECT SUM(tutar) FROM giderler), 1) as yuzde FROM giderler GROUP BY kategori ORDER BY toplam_gider DESC"""
print("\n── Gider Kategorileri ──")
print(pd.read_sql(sorgu3, conn))
sorgu4 = """SELECT odeme_yontemi, COUNT(*) as islem_sayisi,SUM(tutar) as toplam_tutar FROM gelirler GROUP BY odeme_yontemi ORDER BY toplam_tutar DESC"""
print("\n── Ödeme Yöntemi Analizi ──")
print(pd.read_sql(sorgu4, conn))
sorgu5="""SELECT pozisyon,COUNT(*) as personel_sayisi,SUM(maas) as toplam_maas,AVG(maas) as ortalama_maas FROM personel GROUP BY pozisyon ORDER BY toplam_maas DESC"""
print("\n── Personel Maaş Dağılımı ──")
print(pd.read_sql(sorgu5, conn))



#BURADA EN DEĞERLİ DERKEN BİRAZ GARİP OLMUŞ OLABİLİR BURDA ANLATMAK İSTEDİĞİM DERSHANEYE EN FAZLA PARA HARCAYAN 5 OGRENCİYİ GETİRTMEKTİ AMA HEPSİ AYNI TUTARI HARCADIĞI İÇİN MALASEF
endegerliogrenci = """SELECT ogrenciler.ad,ogrenciler.soyad,ogrenciler.sinif_turu,COUNT(gelirler.gelir_id) as odeme_sayisi,SUM(gelirler.tutar) as toplam_odeme FROM gelirler JOIN ogrenciler ON gelirler.ogrenci_id = ogrenciler.ogrenci_id GROUP BY ogrenciler.ogrenci_id ORDER BY toplam_odeme DESC LIMIT 5"""
print("\n── En Değerli 5 Öğrenci ──")
print(pd.read_sql(endegerliogrenci, conn))
conn.close()
print("\nVeritabanı bağlantısı kapatıldı!")