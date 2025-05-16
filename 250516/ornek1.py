toplam=0   #ders notları toplamı olucak
ogrenci_notlari=[] #ögrenci notları girilicek
for i in range(6):
    ogrenci_notlari.append(int(input("notu girin :")))
for ogr_not in ogrenci_notlari:
    toplam=toplam+ogr_not
ortalama=toplam/6
print("ortalamanız:" , ortalama)   
