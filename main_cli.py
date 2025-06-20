# === main_cli.py ===

# Importation des modules nécessaires
# Note : Ces modules doivent exister dans le même dossier ou être installés.
import os  # Pour la gestion des fichiers

# Simulations de modules externes avec des fonctions de base
# Ces blocs servent uniquement à éviter les erreurs lors de l'exécution du Module 5 seul.
# Dans un projet complet, ces modules contiendraient des logiques plus avancées.

# --- Simulation du module tag_validator ---
class tag_validator:
    @staticmethod
    def valider_balises(html_content):
        # Simule une vérification de balises : retourne une liste vide si pas d'erreur
        if "<html>" in html_content and "</html>" in html_content:
            return []  # Pas d'erreur
        else:
            return ["Erreur : balise <html> manquante ou non fermée"]

# --- Simulation du module content_editor ---
class content_editor:
    @staticmethod
    def correction_auto(html_content):
        # Simule une correction simple en ajoutant une balise fermante si manquante
        if "</html>" not in html_content:
            html_content += "</html>"
        return html_content

    @staticmethod
    def modifier_contenu(html_content):
        # Simule une modification manuelle : ajoute un commentaire
        return html_content + "\n<!-- Contenu modifié par l'utilisateur -->"

# --- Simulation du module inspector ---
class inspector:
    @staticmethod
    def afficher_arborescence(html_content):
        print("\n[Arborescence simulée] Contenu détecté :")
        print(html_content[:100], "...")  # Affiche les 100 premiers caractères

    @staticmethod
    def afficher_statistiques(html_content):
        print("\n[Statistiques simulées]")
        print("Longueur du contenu HTML :", len(html_content))
        print("Nombre de balises <a> :", html_content.count("<a"))

# Fonction principale du programme
def main():
    print("=== VALIDATEUR HTML - CLI ===")  # Titre du programme

    # Demande à l'utilisateur de fournir le chemin d'un fichier HTML
    filename = input("Entrez le chemin du fichier HTML à analyser : ")

    # Vérifie que le fichier existe
    if not os.path.exists(filename):
        print("Fichier introuvable.")
        return  # Quitte le programme si le fichier est introuvable

    # Ouvre et lit le contenu du fichier HTML
    with open(filename, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Boucle de menu principal
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Valider les balises HTML")
        print("2. Corriger automatiquement les erreurs")
        print("3. Modifier le contenu manuellement")
        print("4. Afficher les erreurs et statistiques")
        print("5. Sauvegarder le fichier corrigé")
        print("0. Quitter")

        choix = input("Votre choix : ")  # Récupère le choix de l'utilisateur

        if choix == '1':
            # Appelle la fonction de validation des balises
            erreurs = tag_validator.valider_balises(html_content)
            if erreurs:
                print("Erreurs détectées :")
                for erreur in erreurs:
                    print(erreur)
            else:
                print("Aucune erreur détectée.")

        elif choix == '2':
            # Appelle la fonction de correction automatique
            html_content = content_editor.correction_auto(html_content)
            print("Correction automatique effectuée.")

        elif choix == '3':
            # Appelle la fonction de modification manuelle
            html_content = content_editor.modifier_contenu(html_content)
            print("Modification manuelle appliquée.")

        elif choix == '4':
            # Affiche l'arborescence et les statistiques
            inspector.afficher_arborescence(html_content)
            inspector.afficher_statistiques(html_content)

        elif choix == '5':
            # Demande un nom pour le nouveau fichier corrigé
            new_filename = input("Entrez le nom du fichier de sortie : ")
            with open(new_filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print("Fichier sauvegardé sous :", new_filename)

        elif choix == '0':
            # Quitte le programme
            print("Merci d’avoir utilisé le validateur HTML.")
            break

        else:
            print("Choix invalide. Réessayez.")

# Lancement de la fonction principale si le fichier est exécuté directement
if __name__ == "__main__":
    main()














