# Toteuta luokka QuickList, jossa on seuraavat metodit:
# move(k): siirrä listan k ensimmäistä alkiota listan loppuun
# get(i): ilmoita indeksissä i oleva alkio
# Listan sisältö annetaan konstruktorissa, ja kummankin metodin tulee toimia ajassa O(1).
# Selitys Listan sisältö käyttäytyy koodipohjassa näin:
# [1,2,3,4,5,6,7,8,9,10]
# move(3) -> [4,5,6,7,8,9,10,1,2,3]
# move(3) -> [7,8,9,10,1,2,3,4,5,6]
# move(10) -> [7,8,9,10,1,2,3,4,5,6]
# move(7) -> [4,5,6,7,8,9,10,1,2,3]
# move(5) -> [9,10,1,2,3,4,5,6,7,8]

class QuickList:
    def __init__(self, t):
        self.t = t
        self.start_index = 0

    def move(self, k):
        n = len(self.t)
        # Listaa ei tarvitse "fyysisesti muuttaa", vaan voidaan vain laskea, miten indeksit muuttuvat, JOS niitä siirrettäisiin
        # Koska k voi olla suurempi kuin listan koko ja aloituskohdan tulee kuitenkin aina olla 1:n ja n:n välillä, tulee laskea
        # jakojäännös
        self.start_index = (self.start_index + k) % n

    def get(self, i):
        n = len(self.t)
        index = (self.start_index + i) % n
        return self.t[index]

if __name__ == "__main__":
    q = QuickList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(q.get(4)) # 5
    q.move(3)
    print(q.get(4)) # 8
    q.move(3)
    print(q.get(4)) # 1
    q.move(10)
    print(q.get(4)) # 1
    q.move(7)
    q.move(5)
    print(q.get(0)) # 9
