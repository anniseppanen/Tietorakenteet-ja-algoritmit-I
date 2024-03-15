# Tehtäväsi on muodostaa luvuista 1 ... n lista, jossa on tasan k inversiota.
# Voit olettaa, että n <= 100 ja k on valittu niin, että ratkaisu on olemassa. 
# Voit muodostaa minkä tahansa kelvollisen listan.
# Toteuta tiedostoon againinv.py funktio create, joka muodostaa listan.

def create(n, k):
    # Luodaan lista, jossa on maksimimäärä inversioita, eli lista, jossa luvut ovat suurimmasta pienimpään
    l = list(reversed(range(1,n+1)))

    # Lasketaan inversioiden määrä, joka listassa tekohetkellä on. Kaava tulee summan 1+2+...+n-1 = n(n-1)/2 kaavasta.
    max_inv = int((n*(n-1))/2)

    # Lasketaan sitten, kuinka monta näistä inversioista tulee poistaa, jotta saadaan haluttu määrä inversioita
    remove_inv = max_inv-k

    index1 = 0
    index2 = 1
    x = len(l)

    # Käydään listaa vasemmalta oikealle, vaihtaen aina kahden vierekkäisen numeron paikkaa. 
    for _ in range(remove_inv):

        # Mikäli päästään listan loppuun, seuraavalla kierroksella ei haluta enää päästä tänne, sillä viimeisenä on jo listan isoin luku
        # eikä sen paikkaa haluta enää muuttaa. Siksi x:stä vähennetään 1 ja lista aloitetaan taas alusta indeksein 0 ja 1.
        if index2 == x:
            x -= 1
            index1 = 0
            index2 = 1
        a = l[index1]
        b = l[index2]
        l[index1] = b
        l[index2] = a
        index1 += 1
        index2 += 1
    return l

if __name__ == "__main__":
    print(create(3, 0)) # [1,2,3]
    print(create(3, 1)) # esim. [1,3,2]
    print(create(3, 2)) # esim. [3,1,2]
    print(create(9, 34))
    print(create(9,10))
    print(create(5,9))
    print(create(10,23))
    print(create(4,6))