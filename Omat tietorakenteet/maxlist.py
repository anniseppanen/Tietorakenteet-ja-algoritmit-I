# Toteuta luokka MaxList, jossa on seuraavat metodit:
# add(x): lisää luku x listalle
# max(): ilmoita listan suurin luku (tai None jos lista on tyhjä)
# Kummankin metodin tulee toimia ajassa O(1).

class MaxList:
    def __init__(self):
        self.maxList = []
        self.maxValue = None

    def add(self, x):
        self.maxList.append(x)
        if self.maxValue == None or x > self.maxValue:
            self.maxValue = x

    def max(self):
        return self.maxValue

if __name__ == "__main__":
    m = MaxList()
    print(m.max()) # None
    m.add(1)
    m.add(2)
    m.add(3)
    print(m.max()) # 3
    m.add(8)
    m.add(5)
    print(m.max()) # 8