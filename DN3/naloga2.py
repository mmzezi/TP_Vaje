data = {"prices": [41970, 40721, 41197, 41137, 43033],

       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

def najvecja_vrednost(data):
    max_vrednost1 = max(list(data.values())[0])
    max_vrednost2 = max(list(data.values())[1])
    #bejsikli samo za vsak ključ najdeš max vrednost, pač daš [0] pa [1] da poveš za kerga
    #max_vrednost = max(data.values())
    #max_vrednost = max(max_vrednost)
    print(max_vrednost1, max_vrednost2)

najvecja_vrednost(data)
