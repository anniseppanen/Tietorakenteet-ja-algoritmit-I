# Annettuna on osakkeen hinta n päivän ajalta. Tehtäväsi on selvittää, mikä olisi ollut suurin mahdollinen tuotto, 
# jos olisit voinut ostaa ja myydä osakkeen enintään kahdesti. Sinulla saa olla hallussasi kerrallaan enintään yksi osake. 
# Lisäksi jos ostat osakkeen toisen kerran, välissä täytyy olla ainakin yksi päivä, jolloin sinulla ei ollut osaketta.
# Algoritmin aikavaativuuden tulee olla O(n). Selitys: Kun hinnat ovat [1,5,2,1,5], tuotto 8 saadaan toistamalla kahdesti 
# osto ja myynti hintaan 1 ja 5. Kun hinnat ovat [1,5,1,5], tämä ei ole mahdollista, koska myynnin ja oston välissä tulee olla 
# ainakin yksi päivä. Silloin voit saada vain tuoton 4 ostamalla ja myymällä osakkeen kerran

def find(t):
    if not t:
        return 0

    n = len(t)
    max_profit_1, max_profit_2 = 0, 0
    min_price_1, min_price_2 = t[0], t[0]
    max_profit = 0

    for i in range(1, n):
        # Selvitetään maksimituotto ja minimihinta i:hin mennessä
        max_profit_1 = max(max_profit_1, t[i] - min_price_1)
        min_price_1 = min(min_price_1, t[i])

        # Jos listaa on vielä tarpeeksi jäljellä, selvitetään maksimituotto ja minimihinta i+2 mennessä, 
        # eli silloin, kun oston ja myynnin välissä on yksi päivä
        if i+2 < n:
            max_profit_2 = max(max_profit_2, t[i+2] - min_price_2)
            min_price_2 = min(min_price_2, t[i+2] - max_profit_1)
        
        # Lopuksi selvitetään suurin näistä tuotoista ja palautetaan se
        max_profit = max(max_profit, max_profit_1, max_profit_2)
    return max_profit
    
 
if __name__ == "__main__":
    print(find([1,5,2,1,5])) # 8
    print(find([1,5,1,5])) # 4
    print(find([1,2,3,4,5])) # 4
    print(find([5,4,3,2,1])) # 0
    print(find([4,2,5,8,7,6,1,2,5,1])) # 10
    print(find([4, 3, 1, 3, 5, 1, 4])) # 5

