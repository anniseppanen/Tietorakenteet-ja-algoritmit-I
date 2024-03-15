# Sinulle annetaan tiedot ravintolan saapuvista ja lähtevistä asiakkaista samaan tapaan kuin kurssin materiaalissa.
# Tehtäväsi on selvittää, mikä oli pisin aika, jolloin ravintola oli tyhjänä jonkun asiakkaan lähtemisen ja toisen asiakkaan saapumisen välissä.
# Algoritmin aikavaativuuden tulee olla O(n \log n).

def find(a, d):
    events = []
    # Lisätään listaan saapumis- ja lähtöajat tupleina
    for time in a:
        events.append((time,1))
    for time in d:
        events.append((time,2))
    # Järjestetään ajat
    events.sort()
    # c pitää yllä ihmisiä, jotka ovat ravintolassa
    c = 0
    result = 0
    # last pitää yllä, edellisen tapahtuman
    last = events[0]
    for event in events:
        # Jos ravintolaan tulee ihminen, kasvatetaan laskuria c yhdellä
        if event[1] == 1:
            c += 1
        # Jos ravintolasta lähtee ihminen, vähennetään laskurista c yksi
        if event[1] == 2:
            c -= 1
        # Jos ravintolassa ei ole ketään, lasketaan aika, minkä ravintola on ollut tyhjänä
        if c == 1 and event[1] == 1 and last[1] == 2:
            result = max(result, event[0]-last[0])
        last = event
    return result

if __name__ == "__main__":
    print(find([1, 6], [2, 9])) # 4
    print(find([1, 2, 3], [2, 3, 4])) # 0
    print(find([1, 4, 6, 8], [5, 5, 9, 9])) # 1
    print(find([1, 10**9], [2, 10**9+1])) # 999999998  
    print(find([9, 6, 10, 3, 7, 6, 7, 4, 6, 7],[14, 10, 15, 5, 12, 8, 12, 9, 6, 12])) # 0