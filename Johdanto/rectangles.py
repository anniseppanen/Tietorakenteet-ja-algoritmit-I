# Tasossa on kolme suorakulmiota, joiden sivut ovat vaaka- ja pystyakselien suuntaisia. 
# Tehtäväsi on laskea sen alueen pinta-ala, jota peittää vähintään yksi annetuista suorakulmioista.
# Voit olettaa, että kaikki koordinaatit ovat kokonaislukuja välillä -10^9 ... 10^9.
# Huomaa, että on liian hidasta käydä läpi kaikki pisteet suorakulmioiden alueelta, 
# vaan sinun tulee keksiä tehokkaampi matemaattinen ratkaisu.
# Toteuta funktio area(rec1, rec2, rec3), joka antaa kysytyn pinta-alan. 
# Funktiolle annetaan kolme tuplea, joista jokainen määrittelee yhden suorakulmion. 
# Jokaisessa tuplessa on neljä kokonaislukua x_1, y_1, x_2 ja y_2: suorakulmion vasen ylänurkka on (x_1,y_1) 
# ja oikea alanurkka on (x_2,y_2).

def area(rec1, rec2, rec3):

    # Laskee yhden suorakulmion pinta-alan
    def rectangle_area(rec):
        if rec[2]-rec[0] > 0 and rec[1]-rec[3] > 0:
            return (rec[2]-rec[0])*(rec[1]-rec[3])
        else:
            return 0
    
    # Laskee kahden suorakulmion pinta-alojen leikkauksen pinta-alan
    def overlap(rec1,rec2):
        left_x = max(rec1[0],rec2[0])
        right_x = min(rec1[2],rec2[2])
        upper_y = min(rec1[1],rec2[1])
        lower_y = max(rec1[3],rec2[3])
        return (left_x,upper_y,right_x,lower_y)
    
    # Lasketaan ensin kaikkien suorakulmioiden oma pinta-ala
    rec1_area = rectangle_area(rec1)
    rec2_area = rectangle_area(rec2)
    rec3_area = rectangle_area(rec3)

    # Lasketaan nyt kaikki mahdolliset kahden suorakulmion leikkauksen pinta-alat
    rec1_rec2_overlap = rectangle_area(overlap(rec1,rec2))
    rec1_rec3_overlap = rectangle_area(overlap(rec1,rec3))
    rec2_rec3_overlap = rectangle_area(overlap(rec2,rec3))

    # Lopuksi lasketaan vielä leikkaus, jossa kaikki ovat päällekkäin, jotta se tulee laskettua kuitenkin yhden kerran
    rec1_rec2_rec3_overlap = rectangle_area(overlap(overlap(rec1,rec2), rec3))
    total_area = rec1_area+rec2_area+rec3_area-rec1_rec2_overlap-rec1_rec3_overlap-rec2_rec3_overlap+rec1_rec2_rec3_overlap
    return total_area


if __name__ == "__main__":
    rec1 = (-1,1,1,-1)
    rec2 = (0,3,2,0)
    rec3 = (0,2,3,-2)
    print(area(rec1,rec2,rec3)) # 16
    rec1 = [1,2,3,0]
    rec2 = [-3,2,1,-3]
    rec3 = [-2,-2,2,-3]
    print(area(rec1,rec2,rec3)) #25