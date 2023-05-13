import urllib.parse
import requests

api_url_MF = "https://www.mapquestapi.com/directions/v2/route?"
llave = "VhNGCvNpZAX4AtwWORnRW1GBaQfTO9cO"

while True:
    comienzo = input("Cuidad de Origen o comienzo: ")
    if comienzo == "salir" or comienzo == "s":
        break
    final = input("Cuidad de Destino o final: ")
    if final == "salir" or final == "s":
        break
    
    url = api_url_MF + urllib.parse.urlencode({"key": llave, "from":comienzo, "to":final})
    print("URL: " + (url))
    mast_datos = requests.get(url).json()
    mast_estatus = mast_datos["info"]["statuscode"]
    
    if mast_estatus == 0:
        print("Estado de la API: " + str(mast_estatus) + " = Una llamada de ruta exitosa.\n")
        print("=============================================")
        print("Como llegar desde " + (comienzo) + " hasta " + (final))
        print("tiempo de viaje:   " + (mast_datos["route"]["formattedTime"]))
        print("Kilometros:      " + str("{:.2f}".format((mast_datos["route"]["distance"])*1.61)))
        print("=============================================")
        for each in mast_datos["route"]["legs"][0]["maneuvers"]:
         print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")