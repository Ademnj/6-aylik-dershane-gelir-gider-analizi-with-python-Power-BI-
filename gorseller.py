import matplotlib.pyplot as plt
from analiz import aylik_gelir,aylik_gider,sinif_dagilim,net_kar,giderktg,paket_gelir,odeme_dagilim

plt.rcParams['font.family'] = 'DejaVu Sans'


# ── GRAFİK 1 — Aylık Gelir & Gider Karşılaştırması ──
fig, ax = plt.subplots(figsize=(10,5))

aylar = [str(a) for a in aylik_gelir.index]

ax.plot(aylar, aylik_gelir.values, marker='o', color='green', linewidth=2, label='Gelir')
ax.plot(aylar, aylik_gider.values, marker='o', color='red', linewidth=2, label='Gider')
ax.fill_between(aylar,aylik_gelir.values,aylik_gider.values, alpha = 0.1, color="green")

ax.set_title("Aylık Gelir & Gider Karşılaştırması", fontsize=14,fontweight="bold")
ax.set_xlabel("Ay")
ax.set_ylabel("Tutar (Milyon)")
ax.legend()
ax.grid(True, alpha = 0.3)
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig("gorseller/gelir_gider.png",dpi = 150)
plt.show()
plt.close("all")

print("Grafik 1 güNCELLENDİ")

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(paket_gelir["tutar"],labels=paket_gelir["paket_adi"],autopct="%1.1f%%",colors=['#2ecc71', '#e74c3c', '#3498db'],startangle=90,wedgeprops={"edgecolor":"white","linewidth":2})
ax.set_title("Paket bazında gelir dağılımı", fontsize =14, fontweight ="bold")
plt.tight_layout()
plt.savefig("gorseller/paket_dagilim.png",dpi=150)
plt.show()

print("Grafik 2 Güncellendi")

plt.close('all')

fig, ax = plt.subplots(figsize=(10, 6))

renkler = ['#e74c3c', '#e67e22', '#f39c12', '#27ae60', '#3498db', '#9b59b6', '#1abc9c', '#95a5a6', '#34495e']

bars = ax.barh(
    giderktg.index,
    giderktg.values,
    color=renkler
)
for bar, val in zip(bars, giderktg.values):
    ax.text(bar.get_width() + 10000, bar.get_y() + bar.get_height()/2,
            f'{val:,.0f} TL', va='center', fontsize=9)

ax.set_title('Gider Kategorilerine Göre Dağılım', fontsize=14, fontweight='bold')
ax.set_xlabel('Tutar (Milyon)')
ax.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('gorseller/gider_kategorileri.png', dpi=150)
plt.show()
print("Grafik Güncellendi")

plt.close("all")
fig, ax= plt.subplots(figsize=(10,5))

aylar = [str(a) for a in net_kar.index]
renkler = ["green" if x > 0 else "red" for x in net_kar.values]
bars = ax.bar(aylar, net_kar.values, color=renkler, edgecolor='white', linewidth=1.5)

for bar, val in zip(bars, net_kar.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 30000,
            f'{val:,.0f} TL', ha='center', fontsize=8, fontweight='bold')

ax.axhline(y=0, color='black', linewidth=1, linestyle='--')
ax.set_title('Aylık Net Kar / Zarar', fontsize=14, fontweight='bold')
ax.set_xlabel('Ay')
ax.set_ylabel('Tutar (Milyon)')
ax.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gorseller/net_kar.png', dpi=150)
plt.show()
print("Grafik 4 kaydedildi!")

# ── GRAFİK 5 — Ödeme Yöntemi Dağılımı bu kısımda hata var NOTT Düzeltilmedi──
plt.close('all')

fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(
    odeme_dagilim.index,
    odeme_dagilim.values,
    color=['#3498db', '#2ecc71'],
    edgecolor='white',
    linewidth=1.5,
    width=0.5
)

# Barların üstüne değer yaz
for bar, val in zip(bars, odeme_dagilim.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20000,
            f'{val:,.0f} TL', ha='center', fontsize=10, fontweight='bold')

ax.set_title('Ödeme Yöntemine Göre Gelir Dağılımı', fontsize=14, fontweight='bold')
ax.set_xlabel('Ödeme Yöntemi')
ax.set_ylabel('Tutar (Milyon)')
ax.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('gorseller/odeme_yontemi.png', dpi=150)
plt.show()
print("Grafik 5 kaydedildi!")