import requests
from bs4 import BeautifulSoup as bs
import csv
#Öncelikle bu iki modülü kuruyoruz

while True:
#Programın bizim isteğimizle kapanıp açılması için while döngüsü kuruyoruz

    r = input("Görselleri içeren sitenin URL'ini girin. Çıkmak için E tuşua basın : ")
    if r == "E":
        print("Sistemden Çıkılıyor")
        break
    r = requests.get(r)
# request.get ile kullanıcıdan
#alınan url nin html dosyasını çağırıyoruz
    soup = bs(r.content, 'html.parser')
#bu kod ile düzzenli hale getiriyoruz
#html dosyası içerisinde "img" classını arıyoruz#
    liste = []
    for photo in soup.find_all("img"):
        if photo != "None":
            photos = photo.get("src")
            source = str(photos)
            liste.append(source)
            a= str(liste)
            print(photos)
            f = open("görselIndirmeLınkleri.txt", "w", newline="\n")
            f.write(a)
            f.close()
#Oluşturduğumuz for döngüsü ile bu classın içindeki "src" adı altında linkleri
#photo.get ile çekiyoruz çektiğimiz bu linkleri str formatına dönüştürüp bi listenin
#içine atıyoruz daha sonra bu listeyi de py kodunu çalıştırdığımız dizinde bir metin belgesi açarak oraya kaydediyoruz

    if r == "E":
        print("Sistemden Çıkılıyor")
        break
