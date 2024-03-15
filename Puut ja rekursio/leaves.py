# Tehtäväsi on laskea, montako lehteä annetussa puussa on. Puun solmu on lehti, jos sillä ei ole yhtään lasta.

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
    def __repr__(self):
        return str(self.value) 
    
def count(node):
    # Jos solmulla ei ole lapsia, se on lehti, jolloin lehtien summaan lisätään 1
    if not node.children:
        return 1
    leaves = 0
    for child in node.children:
        # Lasketaan rekursion avulla lehtien lukumäärä
        leaves += count(child)
    return leaves
    

if __name__ == "__main__":
    tree = Node(1, [
               Node(2),
               Node(3, [Node(4, [Node(5), Node(6)])]),
               Node(7, [Node(8), Node(9)])
           ])

    print(count(tree)) # 5