import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "KGiHwy7jwbMbq37spv8dyMTkyQAjhr9J"


while True:
    orig = input("Ciudad de Origen: ")
    if orig == "salir" or orig == "s":
        break
    dest = input("Destino: ")
    if dest == "salir" or dest == "s":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest}) 
    json_data = requests.get(url).json()
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("API Estado: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direccion desde " + (orig) + " to " + (dest))
        print("Duracion del viaje:   " + (json_data["route"]["formattedTime"]))
        print("Kilometros totales:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Combustible usado (Ltr): 30.42")
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
