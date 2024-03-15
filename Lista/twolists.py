# Sinulle annetaan kaksi listaa A ja B, jotka molemmat sisältävät luvut 1...n jossain järjestyksessä.
# Tehtäväsi on laskea, moniko luvuista 1...n esiintyy aiemmin listalla A kuin listalla B. 
# Tässä tehtävässä n voi olla suuri ja sinun täytyy keksiä tehokas algoritmi. Algoritmin aikavaativuuden 
# tulee olla O(n). Selitys: Ensimmäisessä testissä luvut 2, 3 ja 4 esiintyvät listalla A aiemmin kuin listalla B.

def count(a, b):
    n = len(a)

    # Luodaan sanakirjat, joihin tulee tieto siitä, missä kohtaa mikäkin luku on
    a_indexes = {}
    b_indexes = {}
    c = 0

    # Lisätään luvut ja niiden indeksit sanakirjoihin
    for i in range(n):
        a_indexes[a[i]] = i
        b_indexes[b[i]] = i
    
    for i in range(n):

        # Jos luvun indeksi on a-sanakirjassa pienempi kuin b-sanakirjassa, silloin se esiintyy aikaisemmin listalla a kuin b
        if a_indexes[b[i]] < b_indexes[b[i]]:
            c += 1
    return c

if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5