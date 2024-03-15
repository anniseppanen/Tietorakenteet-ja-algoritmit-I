# Piirissä on n leikkijää, jotka on numeroitu 1,2...n. 
# Vuoro kiertää piirissä ja joka toinen leikkijä lähtee pois, kunnes piiri on tyhjä. 
# Tehtäväsi on selvittää järjestys, jossa leikkijät poistuvat. 
# Voit olettaa, että n on välillä 1...100.

def create(n):
    if n == 1:
        return [1]
    
    # Luodaan lista leikkijöistä
    l = list(range(1,n+1))

    # Luodaan lista järjestyksestä, jossa leikkijät poistuvat.
    order = []

    i = 0

    # Käydään listaa läpi, kunnes järjestyslistassa on sama määrä leikijöitä kuin alkuperäisten leikkijöiden määrä
    while(len(order)<n):

        # Jos i on parillinen, siirretään nykyinen leikkijä listan loppuun
        if i%2 == 0:
            l.append(l[i])
            
        # Muuten lisätään leikkijä järjestyslistaan
        else:
            order.append(l[i])
        i += 1
    return order

if __name__ == "__main__":
    print(create(1)) # [1]
    print(create(3)) # [2,1,3]
    print(create(7)) # [2,4,6,1,5,3,7]
    print(create(8)) # [2,4,6,8,3,7,5,1]
    print(create(2))
