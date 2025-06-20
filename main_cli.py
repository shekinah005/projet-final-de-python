#Module 5
import os
def main_menu():
    print("== Menu Principal ==")
    print("1. Charger")
    print("2. Afficher le contenu du fichier")
    print("3. Sauvegader les modifications dans un nouveau fichier")
    print("4. Quitter")
def load_file():
    file_url = input("Entrez l'url du fichier à charger:")
    if os.path.isfile(file_url):
        with open(file_url, 'r') as file:
            content = file.read()
            print("Fichier chargé avec succès.")
            return content
    else:
        print("Le fichier n'existe pas, veillez réessayez.")
        return None

def display_content(content):
    if content is not None:
        print("\n=== Contentu du fichier ===")
        print(content)
    else:
        print("Aucun contenu à afficher.")
    
def save_file(content):
    if content is not None:
        new_file_url = input("Entrez le nom du nouveau fichier pour sauvegader les modifications:")
        with open(new_file_url, "w") as file:
            file.write(content)
            print("Modification sauvegardée dans",new_file_url)
    else:
        print("Aucun contenu à saugarder.")

def main():
    content = None
    while True:
        main_menu()
        choix = input("Choisissez une option:")
        if choix == "1":
            content =  load_file()
        elif choix == "2":
            display_content(content)
        elif choix == "3":
            save_file(content) 
        elif choix == "4": 
            print("Aurevoir!")
            break
        else:
            print("Option invalide, veillez réesayez>.")
if __name__ == "__main__":
    main() 












