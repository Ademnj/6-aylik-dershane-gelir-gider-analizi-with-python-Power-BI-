# 📊 Dershane Gelir-Gider Analizi

Python, Pandas ve SQL kullanılarak gerçekçi bir dershane senaryosu üzerinden yapılan 9 aylık finansal veri analizi projesi.

---

## 📁 Proje Yapısı

```
dershane_analiz/
├── data/
│   ├── gelirler.csv
│   ├── giderler.csv
│   ├── ogrenciler.csv
│   ├── paketler.csv
│   ├── personel.csv
│   └── deneme_sinavlari.csv
├── main.py        # Veri yükleme & temizleme
├── analiz.py      # Analiz soruları & hesaplamalar
└── README.md
```

---

## 🔍 Proje Hakkında

Bir dershanenin **Ekim 2025 – Mart 2026** tarihleri arasındaki gelir ve gider verilerinin analizi yapılmıştır.

**Veri seti:**
- 800+ gelir kaydı
- 6 farklı tablo
- 9 aylık finansal veri

---

## 📈 Temel Bulgular

| Metrik | Değer |
|--------|-------|
| Toplam Gelir | 6.732.040 TL |
| Toplam Gider | 2.767.500 TL |
| **Net Kar** | **3.964.540 TL** |

### Paket Bazında Gelir Dağılımı
| Paket | Gelir |
|-------|-------|
| AYT Paketi | 5.740.000 TL (%85) |
| TYT Paketi | 752.040 TL (%11) |
| Deneme Sınavı | 240.000 TL (%4) |

### Ödeme Yöntemi Dağılımı
| Yöntem | Tutar |
|--------|-------|
| Havale/EFT | 5.705.680 TL |
| Nakit | 1.026.360 TL |

### En Büyük Gider Kalemleri
| Kategori | Tutar |
|----------|-------|
| Personel Maaşı | 1.500.000 TL (%54) |
| Vergi & SGK | 600.000 TL (%22) |
| Kira | 270.000 TL (%10) |

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3.12**
- **Pandas** — Veri temizleme & analiz
- **NumPy** — Sayısal hesaplama
- **Matplotlib / Seaborn** — Görselleştirme *(yakında)*
- **SQLite** — Veri sorgulama *(yakında)*
- **Power BI** — Dashboard *(yakında)*

---

## 🚀 Kurulum

```bash
pip install pandas numpy matplotlib seaborn
```

```python
python main.py   # Veriyi temizler
python analiz.py # Analizleri çalıştırır
```

---

## 📌 Yapılacaklar

- [ ] Matplotlib ile gelir-gider grafikleri
- [ ] Seaborn ile korelasyon analizi
- [ ] SQLite entegrasyonu
- [ ] Power BI dashboard

---

## 👤 Geliştirici

**Adem Karpuz** — [github.com/Ademnj](https://github.com/Ademnj) | [linkedin.com/in/ademkzj](https://linkedin.com/in/ademkzj)
