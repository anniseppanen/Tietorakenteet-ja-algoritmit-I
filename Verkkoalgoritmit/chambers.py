# Annettuna on n x m -ruudukko, joka esittää talon pohjapiirrosta. 
# Jokainen ruutu on joko lattiaa (.) tai seinää (#), ja jokainen reunalla oleva ruutu on seinää.
# Kaksi lattiaruutua kuuluvat samaan huoneeseen, jos ne ovat vierekkäin pysty- tai vaakasuunnassa. Montako huonetta talossa on?
# Voit olettaa, että 1 <= n, m <= 20.

# Tämä luokka etsii syvyyshaun (depth-first-search) avulla verkon komponentit 
# eli solmut, jotka ovat yhteydessä toisiinsa kaaria pitkin
class Components:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in nodes}
        
    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)
        
    def visit(self, node):
        if node in self.components:
            return
        self.components[node] = self.counter

        for next_node in self.graph[node]:
            self.visit(next_node)

    # Aina kun vastaan tulee sellainen solmu, joka ei ole vielä yhteydessä muihin solmuihin, 
    # kasvatetaan counter-muuttujaa yhdellä. Lopputuloksena on sanakirja, jossa kerrotaan
    # mihin komponenttiin mikäkin solmu kuuluu 
    def find_components(self):
        self.counter = 0
        self.components = {}

        for node in self.nodes:
            if node not in self.components:
                self.counter += 1
                self.visit(node)
                
        return self.components
    
def count(r):
    nodes = {}
    edges = []
    node = 1
    # Käydään syötteenä annettu lista läpi merkki kerrallaan
    for i in range(len(r)):
        for j in range(len(r[i])):
            # Jos merkki on piste, ollaan "huoneessa"
            if r[i][j] == ".":
                # Lisätään huoneen paikka listaan nodes
                nodes[(i,j)] = node
                # Jos edellinen merkki on ollut myös piste, lisätään näiden merkkien välille kaari
                if i>0 and r[i-1][j] == ".":
                    edges.append((nodes[(i-1,j)], node))
                if j>0 and r[i][j-1] == ".":
                    edges.append((nodes[(i, j-1)], node))
                node += 1
    
    # Tehdään Components-objekti, johon lisätään edellä löydetyt kaaret
    n = Components(list(range(1, node)))
    for pair in edges:
        n.add_edge(pair[0], pair[1])
    # Lasketaan find_components-metodin avulla eri huoneiden lukumäärät
    return len(set(n.find_components().values()))

if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3