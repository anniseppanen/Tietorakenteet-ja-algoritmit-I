# Annettuna lista, jossa on n kokonaislukua. Tehtäväsi on etsiä suurin etäisyys kahden saman luvun välillä. 
# Etäisyys tarkoittaa indeksien erotusta. Algoritmin aikavaativuuden tulee olla O(n).

def find(t):
    pos = {}
    dist = 0
    for i in range(len(t)):
        pos[t[i]] = i
    for i in range(len(t)):
        dist = max(dist, pos[t[i]]-i)
    return dist

if __name__ == "__main__":
    print(find([1,2,1,1,2])) # 3
    print(find([1,2,3,4])) # 0
    print(find([1,1,1,1,1])) # 4
    print(find([1,1,2,3,4])) # 1
    print(find([1,5,1,5,1])) # 4