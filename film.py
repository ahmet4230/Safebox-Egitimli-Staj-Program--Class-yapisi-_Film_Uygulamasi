class Film:
    def __init__(self, ad, yonetmen, tur):
        self.ad = ad
        self.yonetmen = yonetmen
        self.tur = tur


class FilmListesi:
    def __init__(self, dosya_adi):
        self.dosya_adi = dosya_adi

    def film_ekle(self):
        film_adi = input("Film adını girin: ")
        yonetmen = input("Yönetmen adını girin: ")
        tur = input("Film türünü girin: ")
        film = Film(film_adi,yonetmen,tur)
        with open(self.dosya_adi, "a") as dosya:
            dosya.write(f"{film.ad},{film.yonetmen},{film.tur}\n")
        print(f"Film '{film.ad}' listeye eklendi.")

    def liste_goster(self):
        with open(self.dosya_adi, "r") as dosya:
            filmler = dosya.readlines()
        if not filmler:
            print("Listede herhangi bir film yok.")
        else:
            print("Filmler:")
            for film_str in filmler:
                film_bilgileri = film_str.strip().split(",")
                if len(film_bilgileri) == 3:
                    film = Film(film_bilgileri[0], film_bilgileri[1], film_bilgileri[2])
                    print("Film adı: " + film.ad + ", Yönetmen: " + film.yonetmen + ", Tür: " + film.tur)

# Kullanım örneği
film_listesi = FilmListesi("filmler.txt")

while True:
    print("seçenekler")
    print("1. Film ekle")
    print("2. Film listele")
    print("3. Çıkış yap")
    secim = input("Seçim yapınız: ")

    if secim == "1":
        film_listesi.film_ekle()
    elif secim == "2":
        film_listesi.liste_goster()
        
    elif secim == "3":
            print("çıkış yapılıyor")
            break
                        
        
        
      
    while True: 
        
        devam = input("başka bir işlem yapmak istiyor musunuz ? y / n ")
        
        if devam == "y":
            print("seçenekler")
            print("1. Film ekle")
            print("2. Film listele")
            
            
            
            
            secim = input("Seçim yapınız: ")

            if secim == "1":
                film_listesi.film_ekle()
            elif secim == "2":
                film_listesi.liste_goster()
          
            
            
           

        elif  devam == "n":
            print("çıkış yapılıyor..")
            break
    break
           