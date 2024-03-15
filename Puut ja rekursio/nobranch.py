# Tehtäväsi on selvittää, onko annettu puu haarautumaton eli jokaisella solmulla on enintään yksi lapsi.

class Node:
    def __init__(self, value, children=[]):
        self.value = value
        self.children = children

def check(node):
    if len(node.children) > 1:
        return False
    for child in node.children:
        if check(child) == False:
            return False
    return True

if __name__ == "__main__":
    tree1 = Node(1, [
                Node(2),
                Node(3, [Node(4, [Node(5), Node(6)])]),
                Node(7, [Node(8), Node(9)])
            ])

    tree2 = Node(1, [Node(2, [Node(3, [Node(4)])])])

    print(check(tree1)) # False
    print(check(tree2)) # True