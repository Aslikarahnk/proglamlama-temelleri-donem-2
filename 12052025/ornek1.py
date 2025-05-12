liste=[]
toplam=0
for i in range (7):
    liste .append (int(input("bir sayıyı girin:")))
for sayi in liste:
    toplam=toplam+sayi
if toplam %2==0:
    print("listedeki sayıların toplamı çift")
else:
    print("listedeki sayıların toplamı tektir")