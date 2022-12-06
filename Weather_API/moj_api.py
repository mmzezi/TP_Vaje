import requests

url = "https://api.rtvslo.si"

print("Vnesite mesto (Nova Gorica, Koper, Kranj, Jesenice, Ljubljana, Postojna, Trbovlje, Novo mesto, Krško, Celje, Maribor, Murska Sobota, Bovec, Videm, Celovec, Gradec, Zagreb, Reka, Slovenj Gradec, Jageršek, all)")

vreme = input("Mesto: ")


def get_api_data(url_path):
    # ustvarimo GET klic na API
    response = requests.get(f"{url}{url_path}", params={"client_id": "8c5205a95060a482f0fc96b9162d9e3f", "location": vreme})
    # podatke vrnjene v JSON formatu pretvorimo v Python slovar
    return response.json()



vreme_data = get_api_data(f"/weather/getArso")
print(f"****** Podatki za {vreme} ******")
#print(vreme_data)
current_vreme = vreme_data["response"]["forecast24h"][0]["timeline"][0]["clouds_shortText"] #tele ničle so potrebne da greš po seznamu
current_temp = vreme_data["response"]["forecast24h"][0]["timeline"][0]["tnsyn"]
print(f"Trenutno vreme je {current_vreme}, {current_temp}°C")