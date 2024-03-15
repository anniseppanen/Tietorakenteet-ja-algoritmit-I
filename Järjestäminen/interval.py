# Annettuna on lista, jossa on n kokonaislukua. Tehtäväsi on poimia listalta mahdollisimman monta kokonaislukua. 
# Ensimmäinen luku saa olla mikä tahansa listan luku. Tämän jälkeen jokaisen seuraavan poimitun luvun tulee olla 
# yhden suurempi kuin edellinen. Montako lukua voit poimia enintään? Algoritmin aikavaativuuden tulee olla O(n \log n).
# Selitys: Listalta [10, 4, 8] voidaan poimia vain yksi luku, sillä minkään kahden luvun erotus ei ole tasan 1. 
# Listalta [7, 6, 1, 8] on mahdollista poimia 3 lukua järjestyksessä 6, 7 ja 8. '

def count(t): 
    t = set(t)
    t = list(t)
    t.sort()
    l = []
    c = 0
    for i in range(1, len(t)):
        if abs(t[i])-abs(t[i-1]) == 1:
            l.append(t[i-1])
            c = max(c, len(l))
        else:
            l = []
    return c+1

if __name__ == "__main__":
    print(count([1, 1, 1, 1])) # 1
    print(count([10, 4, 8])) # 1
    print(count([7, 6, 1, 8])) # 3
    print(count([1, 2, 1, 2, 1, 2])) # 2
    print(count([987654, 12345678, 987653, 999999, 987655])) # 3
    print(count([14, 15, 16, 15, 13])) # 4
