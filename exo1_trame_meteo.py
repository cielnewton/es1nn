trame_meteo = "$METEO,32.5C,55%,1013hpa,Clair"


if trame_meteo.count(",") != 4:
    print("Format non valide : il faut 5 éléments dans la trame")
else:
    tab_meteo = trame_meteo.split(",")

    valide = True

    if tab_meteo[0] != "$METEO":
        print("La trame doit commencer par $METEO")
        valide = False

    if not tab_meteo[1].endswith("C"):
        print("Valeur ou format de la température incorrect (suffixe 'C' attendu)")
        valide = False
    else:
        try:
            temp = float(tab_meteo[1][:-1])
            if not (-30 <= temp <= 48):
                print("Température hors limites (-30 à 48 °C)")
                valide = False
        except:
            print("Température invalide : valeur numérique attendue")
            valide = False

    if not tab_meteo[2].endswith("%"):
        print("Valeur ou format de l'humidité incorrect (suffixe '%' attendu)")
        valide = False
    else:
        try:
            hum = int(tab_meteo[2][:-1])
            if not (0 <= hum <= 100):
                print("Humidité hors limites (0 à 100 %)")
                valide = False
        except:
            print("Humidité invalide : entier attendu")
            valide = False

    pres_str = tab_meteo[3]
    if not pres_str.lower().endswith("hpa"):
        print("Valeur ou format de la pression incorrect (suffixe 'hPa' attendu)")
        valide = False
    else:
        try:
            pres = int(pres_str[:-3])  
            if not (800 <= pres <= 1100):
                print("Pression hors limites (800 à 1100 hPa)")
                valide = False
        except:
            print("Pression invalide : entier attendu")
            valide = False

    # Affichage final
    if valide:
        print(f"La température {temp:.1f} °C")
        print(f"L'humidité {hum} %")
        print(f"La pression {pres} hPa")
       
