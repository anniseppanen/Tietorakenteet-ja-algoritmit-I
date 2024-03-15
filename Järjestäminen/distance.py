# Listalla on n kokonaislukua väliltä 1...k. Listalle halutaan lisätä uusi kokonaisluku väliltä 1...k, 
# jonka etäisyys lähimpään listalla valmiiksi olevaan lukuun on mahdollisimman suuri. Mikä on tämä etäisyys?
# Algoritmin aikavaativuuden tulee olla O(n \log n). Selitys: Ensimmäisessä tapauksessa vastaus on 3, koska 
# listalle voidaan lisätä luku 5 tai 6, jolloin etäisyys on 3 (lukuun 2 tai 9). Ei ole mahdollista lisätä lukua niin, 
# että etäisyys olisi 4 tai enemmän.
import math

def find(t, k):
    dist = 0
    # Alustetaan luku aluksi ykköseksi, koska se on pienin luku, joka on mahdollista lisätä listaan
    # ja koska lista on järjestetty, voidaan etäisyyden tarkistaminen aloittaa ykkösestä
    number = 1
    t.sort()
    for i in range(len(t)):
        # Lasketaan etäisyys seuraavaan listalla olevaan lukuun
        dist = max(dist, t[i]-number)
        # Jos iteroinnissa ei olla vielä listan lopussa, tarkistetaan luvun etäisyys seuraavaan lukuun
        if i<len(t)-1:
            number = t[i]+math.ceil(abs(t[i+1]-t[i])/2)
        # Jos ollaan listan lopussa, tarkistetaan vielä, että voiko luvun lisätä listan loppuun siten, että etäisyys on suurin
        else:
            number = t[i]+(k-t[i])/2
    dist = max(dist, k-t[-1])
    return dist

if __name__ == "__main__":
    print(find([1, 2, 9], 11)) # 3
    print(find([2, 1, 3], 3)) # 0
    print(find([7, 4, 10, 4], 10)) # 3
    print(find([15, 2, 6, 4, 18], 20)) # 4
    print(find([41222388, 392676742, 307110407, 775934683, 25076911], 809136843)) # 191628970
    print(find([14, 15, 6, 2, 7, 14], 15)) # 3
    print(find([2, 11, 9, 10, 10], 15)) # 4 
    print(find([22, 21, 19, 5, 17, 10, 12, 26], 30)) # 4
