hava_sicakligi=int(input("hava sıcaklıgını giriniz"))
if hava_sicakligi  <=5  :
    print("soguk")
elif hava_sicakligi >=6 and hava_sicakligi <14 :
    print("ılık")
elif hava_sicakligi >=5 :
    print("sıcak")
else :
    print("yanlış derece")             