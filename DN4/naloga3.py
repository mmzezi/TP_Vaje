import requests 
niz = input("Vnesite iskani niz: ")
url = "https://www.rtvslo.si/iskalnik?q={}" .format(niz)
#url = "https://www.rtvslo.si"
#print(url)

def dobi_html(url):
    r = requests.get(url)
    r.text
    print(r.text)
dobi_html(url)
