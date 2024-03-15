# Toteuta luokka Mex, jossa on seuraava metodi:
# add(x): lisää kokonaisluku x listalle ja palauta listan mex-luku
# Listan mex-luku on pienin epänegatiivinen kokonaisluku, jota ei esiinny listalla. Esimerkiksi listan [2,0,3,4,2] mex-luku on 1.
# Metodin add tulee toimia keskimäärin ajassa O(1). Voit olettaa, että jokainen lisätty luku on epänegatiivinen.
class Mex:
    def __init__(self):
        self.numbers = set()
        self.mex = 0
        
    def add(self, x):
        self.numbers.add(x)
        if self.mex in self.numbers:
            while self.mex in self.numbers:
                self.mex += 1
            
        return self.mex
        

if __name__ == "__main__":
    m = Mex()
    print(m.add(4)) # 0 
    print(m.add(0)) # 1
    print(m.add(4)) # 1
    print(m.add(2)) # 1
    print(m.add(1)) # 3
    print(m.add(4)) # 3
    print(m.add(1)) # 3

    m = Mex()
    print(m.add(1)) # 0
    print(m.add(3)) # 0
    print(m.add(4)) # 0
    print(m.add(0)) # 2
    print(m.add(5)) # 2
    print(m.add(2)) # 6

    m = Mex()
    print(m.add(1)) # 0
    print(m.add(0)) # 2
    print(m.add(0)) # 2
    print(m.add(1)) # 2
    print(m.add(2)) # 3
    print(m.add(2)) # 3
    print(m.add(2)) # 3
    print(m.add(1)) # 3
    print(m.add(2)) # 3
    print(m.add(1)) # 3


    m = Mex()
    print(m.add(0)) # 1
    print(m.add(0)) # 1
    print(m.add(0)) # 1
    print(m.add(0)) # 1
    print(m.add(1)) # 2
    print(m.add(0)) # 2
    print(m.add(1)) # 2
    print(m.add(1)) # 2
    print(m.add(0)) # 2
    print(m.add(1)) # 2"""


    