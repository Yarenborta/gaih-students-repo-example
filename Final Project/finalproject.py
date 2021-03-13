

sorular= ["Krakow hangi ülkenin şehridir ?","Franz Kafka müzesi nerededir ?","Üçüncül müdahalelere karşı korumalı kripto para birimi hangisidir ?","Hangi ülkenin yüzölçümü Plüton gezegeninden bile daha büyüktür ?","En iyi kadın oyuncu ödülüne layık görülen aktrist kimdir ?","En şişman nüfusa sahip ada neresidir ?","Sular altında kalma tehlikesi olan ülkelerden biri hangisidir?","Üzerinde en çok göl bulunan ülke hangisidir ?","En çok çeşitliliği bir arada barındıran ülke hangisidir?","Hyundai Motor Company araba markası hangi ülkeye aittir ?"]

dogru_cevaplar=["Polonya","Çek Cumhuriyeti","BTC","Rusya","Renee Zellweger","Nauru Adası","Maldivler","Kanada","Hindistan","Güney Kore"]

def sor():
    puan =0

    print("Soru 1:",sorular[0])
    cevap_1=input("1.soru için cevabınız:")
    if (cevap_1==dogru_cevaplar[0]):
        print("Tebrikler!")
        puan +=10
    else:
        print("Cevabınız Yanlış. Doğru cevap: Polonya")


    print("Soru 2:", sorular[1])
    cevap_2=input("2.soru için cevabınız:")
    if(cevap_2==dogru_cevaplar[1]):
        print("Tebrikler!")
        puan +=10
    else:
        print("Cevabınız Yanlış. Doğru cevap: Çek Cumhuriyeti")

    print("Soru 3:", sorular[2])
    cevap_3 = input("3.soru için cevabınız:")
    if (cevap_3 == dogru_cevaplar[2]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış. Doğru cevap:BTC")

    print("Soru 4:", sorular[3])
    cevap_4 = input("4.soru için cevabınız:")
    if (cevap_4 == dogru_cevaplar[3]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış. Doğru cevap: Rusya")

    print("Soru 5:", sorular[4])
    cevap_5 = input("5.soru için cevabınız:")
    if (cevap_5== dogru_cevaplar[4]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış. Doğru cevap: Renee Zellweger")

    print("Soru 6:", sorular[5])
    cevap_6 = input("6.soru için cevabınız:")
    if (cevap_6 == dogru_cevaplar[5]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış. Doğru cevap: Nauru Adası")

    print("Soru 7:", sorular[6])
    cevap_7 = input("7.soru için cevabınız:")
    if (cevap_7== dogru_cevaplar[6]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış.Doğru cevap: Maldivler")

    print("Soru 8:", sorular[7])
    cevap_8 = input("8.soru için cevabınız:")
    if (cevap_8 == dogru_cevaplar[7]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış. Doğru cevap: Kanada")

    print("Soru 9:", sorular[8])
    cevap_9 = input("9.soru için cevabınız:")
    if (cevap_9 == dogru_cevaplar[8]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış. Doğru cevap: Hindistan")

    print("Soru 10:", sorular[9])
    cevap_10 = input("10.soru için cevabınız:")
    if (cevap_10== dogru_cevaplar[9]):
        print("Tebrikler!")
        puan += 10
    else:
        print("Cevabınız Yanlış.Doğru cevap: Güney Kore")

    print("Testimiz Bitmişitir! Toplamda {} puan aldınız".format(puan))

sor()


