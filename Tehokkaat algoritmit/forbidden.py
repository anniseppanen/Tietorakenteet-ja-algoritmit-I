# Tehtäväsi on laskea, monessako merkkijonon osajonossa ei ole a-merkkiä.
# Algoritmin aikavaativuuden tulee olla O(n).

def count(s):
    n = len(s)
    a = -1
    result = 0
    for i in range(n):
        # Jos ollaan a:n kohdalla menossa, merkataan, että edellinen a on ollut i:ssä
        if s[i] == "a":
            a = i
        else:
            # Lasketaan tulokseen a:sta i:hin olevien osajonojen lukumäärä. Kaava toimii myös, 
            # kun a:ta ei ole vielä tullut, sillä a on alustettu -1:ksi 
            result += i-a
    return result 

if __name__ == "__main__":
    print(count("aaa")) # 0
    print(count("saippuakauppias")) # 23
    print(count("x")) # 1
    print(count("aybabtu")) # 9