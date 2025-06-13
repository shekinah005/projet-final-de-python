#Module 5
import os # Importe le module os pour manipuler les fichiers et les chemins.
def main_menu(): # Définition de la fonction qui affiche le menu principale.
    print("== Menu Principal ==") # Affiche un titre pour le menu.
    print("1. Charger") # Option pour charger un fichier.
    print("2. Afficher le contenu du fichier") # Option pour afficher le contenu du fichier charge.
    print("3. Sauvegarder les modifications dans un nouveau fichier") # Option pour enregistrer un fichier modifié.
    print("4. Abandonner") # Option pour quitter le programme.
def load_file():  # Définition de la fonction qui charge un fichier.
    file_url = input("Entrez l'URL du fichier à charger: ") # Demande à l'utilisateur d'entrer le chemin du fichier.
    if os.path.isfile(file_url): # vérifie si le fichier existe sur le systéme.
        with open(file_url, 'r') as lime: # Ouvre le fichier en mode lecture.
            content = lime.read() # Lit le contenu du fichier.
            print("Fichier chargé avec succès.") # Affiche un message de succés.
            return contenu  # Renvoie le contenu du fichier.
    else:  # Si le fichier n'existe pas :
        print("Le fichier n'existe pas, veillez réessayez.")  # Affiche un message d'erreure.
        return None  # Renvoie None pour indiquer l'échec du chargement.

def display_content(contenu): # Définition de la fonction qui affiche le contenu du fichier.
    if content is not None:  # Vérifie si le contenu est valide (non valide).
        print("\n=== Contenu du fichier ===\n")  # Affiche une ligne de séparation avant le contenu.
        print(contenu)  # Affiche le contenu du fichier.
    else: # Si le fichier n'a pas été chargé correctement :
        print("Aucun contenu à afficher.") #  Affiche un messqge d'erreur.
    
def save_file(contenu): # Définition de la fonction save_fille qui prend un argument 'contenu'
    if contenu is not None: # Vérifie si 'contenu' n'est pas None (donc qu'un fichier a bien été chargé)
        new_file_url = input("Entrez le nom du nouveau fichier pour sauvegader les modifications:") # Demande à l'utilisateur d'entrer le nom du nouveau fichier
        with open(new_file_url, "w") as file:  # Ouvre le fichier en monde écriture ("w")
            file.write(contenu) # Ecrit le contenu récupéré précédemment dans le nouveau fichier
            print("Modification sauvegardée dans",new_file_url) # Affiche un message confirmation l'enregistrement des modifications
    else:  # si 'contenu' est None (aucun fichier n'a été chargé)
        print("Aucun contenu à saugarder.")  # Informe l'utilisateur qu'il n'y a rien à enregistrer

def main(): # Définition de la fonction principale du programme.
    content = None  # Initialise la variable 'content' à None, qui servira à stocker le contenu du fichier chargé.
    while True: # Démarre une boucle infinie pour permetre l'interaction contenue avec l'utilisateur.
        main_menu()  # Appelle la fonction 'main_menu' qui affiche les options du programme.
        choix = input("Choisissez une option:")  #   Demande à l'utilisateur d'entrer un choix parmi les options disponibles.
        if choix == "1": # Vérifie si l'utilisateur a choisi l'option 1.
            content =  load_file() #      Appelle la fonction 'load_file' pour charger un fichier et stocke son contenu dans 'content'.
        elif choix == "2": # Vérifie si l'utilisateur a choisi l'option 2.
            display_content(contenu)  # Appelle la fonction 'display'_content' pour afficher le contenu du fichier.
        elif choix == "3": # Vérifie si l'utilisateur a choisi l'option 3.
            save_file(contenu) # Appelle la fonction 'save_fille' pour enregistrer le contenu dans un nouveau fichier.
        elif choix == "4":  # Vérifie si l'utilisateur a choisi l'option 4.
            print("Aurevoir!")  # Affiche un message dev sortie.
            break  #  Temine la boucle et met fin au programme.
        else: # si le programme doit afficher un message et quiter la boucle.
            print("Option invalide, veillez réesayez>.") # Informe l'utilisateur que l'entrée n'est pas reconnue et qu'il doit essayer une option valide
if __name__ == "__main__": # Vérifie si le script est exécuté directement (et non importé comme module)
    main() # Appelle la fonction principale 'main()' pour démarrer le programme








