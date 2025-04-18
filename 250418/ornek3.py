saat=int(input("otoparkta kaç saat kaldınız"))
if saat <=1 : 
    print("1 saate 5 tl")
elif saat >1 and saat <5 :
    print("ödenecek tutar" , saat*4) 
elif saat >5:
    print("ödenecek tutar" , saat*3)
else:
    print("gecersiz")           