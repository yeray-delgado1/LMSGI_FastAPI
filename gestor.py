### Imports ################################################## 
import os   #per neteja la pantalla
import json #per treballar amb fitxers JSON

#Variables ###################################################

#Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json" 

# Llista d'alumnes
def carregar_dades():
    global alumnes
    with open(nom_fitxer, 'r') as f:
        alumnes = json.load(f)

# Cargar dades en començar el programa
carregar_dades()

### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
#   
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    #Netejem la pantalla
    os.system('cls')            
    
    #Mostrem les diferents opcions
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")
    
    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #i retornem l'opció escollida per l'usuari
    return input()

### Programa ################################################

#Fins a l'infinit (i més enllà)
while True:
    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")

            # Recórrer la llista d'alumnes i mostrar l'ID, nom i cognom de cada alumne
            for alumne in alumnes:
                print(f"ID: {alumne['id']} - Nom: {alumne['nom']} {alumne['cognom']}")
            input()
    

        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            # Demanar les dades per a l'alumne + ID automàtic
            id_nou = max([a['id'] for a in alumnes], default=0) + 1
            nom = input("Nom: ")
            cognom = input("Cognom: ")
            dia = int(input("Dia de naixement: "))
            mes = int(input("Mes de naixement: "))
            anyo = int(input("Any de naixement: "))
            email = input("Email: ")
            feina = input("Treballa? (True/False): ") == "False"
            curs = input("Curs: ")
            
            # Crear el diccionari de l'alumne amb les dades introduïdes
            alumnes.append({
                "id": id_nou,
                "nom": nom,
                "cognom": cognom,
                "data": {"dia": dia, "mes": mes, "any": anyo},
                "email": email,
                "feina": feina,
                "curs": curs
            })
            
            input()
    
        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")

        # Solicitar l'ID de l'alumne
            id_alumne = int(input("ID de l'alumne: "))
            
            # Buscar l'alumne per ID
            alumne_trobat = None
            for alumne in alumnes:
                if alumne['id'] == id_alumne:
                    alumne_trobat = alumne
                    break
            
            # Si l'alumne és trobat, mostrem les dades
            if alumne_trobat:
                print(f"ID: {alumne_trobat['id']}")
                print(f"Nom: {alumne_trobat['nom']} {alumne_trobat['cognom']}")
                print(f"Data de naixement: {alumne_trobat['data']['dia']}/{alumne_trobat['data']['mes']}/{alumne_trobat['data']['any']}")
                print(f"Email: {alumne_trobat['email']}")
                print(f"Feina: {'Sí' if alumne_trobat['feina'] else 'No'}")
                print(f"Curs: {alumne_trobat['curs']}")
            else:
                print("Alumne no trobat.")
            
            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")

            # Sol·licitar l'ID de l'alumne a eliminar
            id_esborrar = int(input("ID de l'alumne a esborrar: "))

            # Eliminar l'alumne amb l'ID corresponent
            alumnes[:] = [a for a in alumnes if a['id'] != id_esborrar]
            input()

        # Desar a fitxer ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")
            # Desa la llista d'alumnes al fitxer JSON amb una indentació de 4 espais per facilitar la llegibilitat
            with open(nom_fitxer, "w") as f:
                json.dump(alumnes, f, indent=4)
            print("Dades desades correctament.")
            input()

        # Llegir fitxer ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")
            # Intentar carregar les dades del fitxer JSON
            try:
                with open(nom_fitxer, "r") as f:
                    alumnes = json.load(f)
                print("Dades carregades correctament.")
            except FileNotFoundError:
                # Mostrar un missatge d'error si el fitxer no es troba
                print("No s'ha trobat el fitxer.")
            input()

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")
            break

        #Qualsevol altra cosa #####################   
        case _:
            # Si l'usuari selecciona una opció no vàlida, mostrar un missatge d'error
            print("\nOpció incorrecta\a")            
            input()
