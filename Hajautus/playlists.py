# Annettuna on soittolista, jossa jokaista laulua vastaa tietty kokonaisluku. Tehtäväsi on selvittää, monessako soittolistan 
# osalistassa kaikki laulut ovat eri lauluja. Algoritmin aikavaativuuden tulee olla O(n).

def count(t):
    # Tehdään sanakirja laulujen paikoista
    pos = {}
    # Muuttuja last kuvastaa sitä kohtaa, jossa laulu on viimeeksi nähty
    last = -1
    # Lasketaan muuttujaan c osalistojen määrä
    c = 0
    for i, song in enumerate(t):
        # Jos laulu on jo soittolistassa, vaihdetaan osalistojen aloituskohtaa
        if song in pos:
            last = max(pos[song], last)
        # Tällä kaavalla saadaan kohdasta last alkavien ja kohtaan i loppuvien osalistojen lukumäärä
        c += i-last
        # Lisätään lopuksi vielä laulun sijainti sanakirjaan
        pos[song] = i
    return c

if __name__ == "__main__":
    print(count([1,2,3,4])) # 10
    print(count([1,1,1,1])) # 4
    print(count([5])) # 1
    print(count([1,3,2,3,4,2,4,1,2,1])) # 24
                 