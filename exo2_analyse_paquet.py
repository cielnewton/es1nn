# Programme principal
while True:
    print("Analyse d'un nouveau paquet réseau :")
    
    # Saisie de l'adresse IP source
    while True:
        ip_source = input("Saisir l'adresse IP source : ")
        octets_source = ip_source.split('.')
        if len(octets_source) == 4:
            valide = True
            for octet in octets_source:
                if not octet.isdigit():
                    valide = False
                    break
                if int(octet) < 0 or int(octet) > 255:
                    valide = False
                    break
            if valide:
                break
        print("Adresse IP source invalide, veuillez réessayer.")
    
    # Saisie de l'adresse IP destination
    while True:
        ip_destination = input("Saisir l'adresse IP destination : ")
        octets_destination = ip_destination.split('.')
        if len(octets_destination) == 4:
            valide = True
            for octet in octets_destination:
                if not octet.isdigit():
                    valide = False
                    break
                if int(octet) < 0 or int(octet) > 255:
                    valide = False
                    break
            if valide:
                break
        print("Adresse IP destination invalide, veuillez réessayer.")
    
    # Saisie du protocole
    protocole = input("Saisir le protocole (TCP, UDP, ICMP, etc.) : ").upper()
    
    # Analyse de sécurité
    ip_source_interne = octets_source[0] == '192' and octets_source[1] == '168'
    ip_destination_interne = octets_destination[0] == '192' and octets_destination[1] == '168'
    
    if ip_source_interne and ip_destination_interne:
        statut_securite = "Sûr (les deux adresses sont internes)"
    else:
        statut_securite = "Potentiellement dangereux (adresse externe détectée)"
    
    # Affichage des résultats
    print("\nAnalyse du paquet :")
    print("Adresse source :", ip_source)
    print("Adresse destination :", ip_destination)
    print("Protocole :", protocole)
    print("Statut de sécurité :", statut_securite)
    
    # Demander si l'utilisateur veut continuer
    continuer = input("\nVoulez-vous analyser un autre paquet ? (oui/non) : ").lower()
    if continuer != 'oui':
        break
