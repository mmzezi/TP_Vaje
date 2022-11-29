import requests 
#niz = input("Vnesite iskani niz: ")
#url = "https://www.rtvslo.si/iskalnik?q={}" .format(niz)
#url = "https://www.rtvslo.si"
#print(url)
url = input("Vnesite naslov: ")

def get_api_data(url):
    r = requests.get(url)
    r.text
    #print(r.text)
    req = r.status_code
    if req == 200:
        print("200 OK")
    else:
        print("200 false")
    json = r.json()
    print(json)

get_api_data(url)
