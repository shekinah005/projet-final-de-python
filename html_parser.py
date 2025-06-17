from html.parser import HTMLParser  # importation du module

class NoeudDOM:    # déclaration d'une classe
    def __init__(self, balise=None, contenu=None, parent=None):   # constructeur
        self.balise = balise  # balise HTML
        self.contenu = contenu  # contenu texte
        self.enfants = []  # liste des enfants
        self.parent = parent  # parent

class AnalyseurHTMLSimple(HTMLParser):  # déclaration d'une classe
    def __init__(self):  # constructeur
        super().__init__()  # appel du constructeur parent
        self.racine = NoeudDOM(balise='document')  # racine du DOM
        self.courant = self.racine  # noeud courant

    def handle_starttag(self, balise, attributs):  # gestion des balises ouvrantes
        noeud = NoeudDOM(balise=balise, parent=self.courant)
        self.courant.enfants.append(noeud)
        self.courant = noeud

    def handle_endtag(self, balise):  # gestion des balises fermantes
        if self.courant.parent:
            self.courant = self.courant.parent

    def handle_data(self, donnees):  # gestion des données textuelles
        donnees = donnees.strip()
        if donnees:
            noeud = NoeudDOM(contenu=donnees, parent=self.courant)
            self.courant.enfants.append(noeud)

    def obtenir_dom(self):  # obtenir le DOM
        return self.racine

def lire_fichier_html(chemin):  # fonction pour lire un fichier HTML
    with open(chemin, "r", encoding="utf-8") as fichier:
        return fichier.read()