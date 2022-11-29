import requests 
#niz = input("Vnesite iskani niz: ")
#url = "https://www.rtvslo.si/iskalnik?q={}" .format(niz)
#url = "https://www.rtvslo.si"
#print(url)
url = input("Vnesite naslov: ")

def dobi_html(url):
    r = requests.get(url)
    r.text
    #print(r.text)
    req = r.status_code
    if req == 200:
        print(r.text)
    else:
        print("False")

dobi_html(url)
