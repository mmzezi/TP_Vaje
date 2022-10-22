d = {
    "mačka": "Micka",
    "pes": "Fido",
    "volk": "Rex",
    "medved": "Žan",
    "slon": "Jan",
    "žirafa": "Helga",
    "lev": "Gašper",
    "tiger": "Anže",
    "papagaj": "Črt",
    "ribica": "Elena",
    "krokodil": "Kasper",
    "zajec": "Lars",
    "kamela": "Manca" 
}
'''
for values in d.values():
    if 'r' in values.lower():
        print(values)
'''
for key, value in d.items(): #dict.items vsebuje vse kar je v slovarju, zato se lahko sprehodimo po ključih in vredostih
    if 'r' in value.lower(): #R ali r je isto če je vse lowercase
        print(key)
