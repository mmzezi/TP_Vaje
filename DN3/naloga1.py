test_emso = "0104986505555"

def emso_leta_preracun(self):
    emso = str(input('Vnesite EMŠO: \n'))
    #print(test_emso)
    datum_str = emso[4:7]
    datum = int(datum_str)
    #print(datum)
    #print(datum_str)
    if datum_str[0] == "9":
        letnica = 1000 + datum
    else:
        letnica = 2000 + datum
    #print(letnica)
    letnica_int = int(letnica)
    print('Vaša starost je', 2022 - letnica_int)
        

emso_leta_preracun(test_emso)
