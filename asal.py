def is_prime(sayi1): #fonk
    if sayi1 < 2:
        return False
    if sayi1 in (2, 3):  # 2 ve 3 özel durumlar istisna
        return True
    if sayi1 % 2 == 0 or sayi1 % 3 == 0:  # 2 veya 3'e bölünebilen sayılar asal değildir
        return False
    
    i = 5 #baslangıc degeri
    while i * i <= sayi1:  # 6k ± 1 optimizasyonu kural matematik
        if sayi1 % i == 0 or sayi1 % (i + 2) == 0:
            return False
        i += 6  # 6'nın katları arasında kontrol yap
    
    return True

num = int(input("Bir sayi girin: "))

print(f"{num} bir asal sayidir."
     if is_prime(num) else f"{num} asal değildir.")