liste=[]
toplam=0
for i in range (6):
    liste .append (int(input("notu girin:")))
for ders_not in liste:
     toplam=toplam+ders_not
ortalama=toplam/6
print("toplam",toplam)