import re

class TagValidator:
    """
    Moteur de validation des balises HTML.

    Ce validateur vérifie :
    1. La correcte fermeture et le chevauchement des balises.
    2. L'orthographe des noms de balises par rapport à une liste connue.
    3. L'omission ou la malformation des chevrons (< et >).
    4. Identifie la première erreur et sa position.

    Les algorithmes de validation sont basés sur des piles (pour le matching de balises)
    et la comparaison de chaînes/expressions régulières.
    """

    def __init__(self, known_tags=None):
        """
        Initialise le validateur avec une liste de balises HTML connues et valides.

        Args:
            known_tags (list, optional): Une liste de chaînes représentant les noms de balises HTML valides.
                                         Si non fourni, une liste par défaut des balises courantes est utilisée.
        """
        if known_tags is None:
            # Liste par défaut des balises HTML connues et valides (en minuscules)
            self.known_tags = set([
                "html", "head", "body", "title", "meta", "link", "script", "style",
                "div", "p", "span", "a", "img", "br", "hr", "input", "button",
                "form", "label", "select", "option", "textarea", "table", "tr",
                "td", "th", "thead", "tbody", "tfoot", "ul", "ol", "li", "h1",
                "h2", "h3", "h4", "h5", "h6", "header", "footer", "nav", "section",
                "article", "aside", "main", "figure", "figcaption", "video", "audio",
                "source", "track", "iframe", "embed", "object", "canvas", "svg",
                "details", "summary", "dialog", "datalist", "keygen", "meter",
                "output", "progress", "rp", "rt", "ruby", "time", "var", "wbr",
                "b", "i", "em", "strong", "small", "mark", "del", "ins", "sub",
                "sup", "code", "pre", "blockquote", "q", "cite", "abbr", "address",
                "bdo", "bdi", "dfn", "kbd", "samp", "data", "time", "track"
            ])
        else:
            self.known_tags = set(tag.lower() for tag in known_tags)

    def validate(self, html_string):
        """
        Valide une chaîne HTML pour les erreurs de balises.

        Args:
            html_string (str): La chaîne HTML à valider.

        Returns:
            tuple: (est_valide, message_erreur, position_erreur)
                   - est_valide (bool): True si la chaîne est valide, False sinon.
                   - message_erreur (str): Message décrivant la première erreur trouvée.
                                           "Aucune erreur détectée." si valide.
                   - position_erreur (int): L'index de début de la première erreur dans la chaîne.
                                            -1 si aucune erreur.
        """
        stack = []  # Pile pour vérifier la correspondance des balises ouvrantes/fermantes

        # --- 1. Détection de l'omission de chevrons ou de balises mal formées ---
        # Ce motif capture les chaînes qui commencent par '<' mais n'ont pas de '>' correspondant,
        # ou celles qui se terminent par '>' mais n'ont pas de '<' correspondant,
        # indiquant une balise potentiellement mal formée ou incomplète.
        # Il cherche aussi des noms de balises connus qui ne sont pas correctement encapsulés.
        malformed_chevron_pattern = re.compile(
            r'(<[a-zA-Z0-9_:-]+[^>]*$)|'  # Ex: "<div", "<p attr="val"
            r'(^[^<]*[a-zA-Z0-9_:-]+>)'   # Ex: "div>", "p attr="val">"
        )
        
        # Vérifier si la chaîne HTML contient des fragments de balises mal formées
        for match in malformed_chevron_pattern.finditer(html_string):
            # Une correspondance trouvée signifie qu'un chevron est manquant ou mal placé.
            return False, "Omission de chevron détectée ou balise mal formée.", match.start()

        # --- 2. Vérification de la correcte fermeture des balises et de l'orthographe ---
        # Ce motif robuste capture toutes les balises HTML valides:
        # - `<` début de balise
        # - `!?` optionnel pour doctype `<!DOCTYPE html>` ou commentaires `<!-- -->` (que nous ignorons ici)
        # - `/?` capture si c'est une balise fermante (ex: `/div`)
        # - `([a-zA-Z0-9_:-]+)` capture le nom de la balise (ex: `div`, `p`, `my-component`)
        # - `([^>]*)` capture les attributs optionnels
        # - `>` fin de balise
        tag_pattern = re.compile(r'<\s*!?(/?)([a-zA-Z0-9_:-]+)([^>]*)>')

        # Itérer sur toutes les correspondances de balises trouvées dans la chaîne HTML
        for match in tag_pattern.finditer(html_string):
            full_tag = match.group(0)         # La balise complète (ex: `<div>`, `</div>`, `<br/>`)
            is_closing_tag = match.group(1) == '/' # True si c'est une balise fermante (ex: `</`)
            tag_name = match.group(2).lower() # Le nom de la balise (converti en minuscules pour la validation)
            attributes = match.group(3)       # Les attributs éventuels de la balise

            # Valider l'orthographe des noms de balises
            if tag_name not in self.known_tags:
                return False, f"Nom de balise '{tag_name}' inconnu ou mal orthographié.", match.start()

            # Gérer les balises auto-fermantes (ex: `<br/>`, `<img src="..." />`)
            # Si une balise n'est pas une balise fermante ET contient `/>` à la fin de ses attributs,
            # elle est considérée comme auto-fermante et ne nécessite pas de correspondance dans la pile.
            if not is_closing_tag and attributes.strip().endswith('/'):
                continue # Passer à la balise suivante, elle est auto-fermante et ne modifie pas la pile.

            # Vérifier la correcte fermeture et le chevauchement des balises
            if not is_closing_tag:
                # Si c'est une balise ouvrante, l'ajouter à la pile avec sa position.
                stack.append((tag_name, match.start()))
            else:
                # Si c'est une balise fermante
                if not stack:
                    # S'il n'y a pas de balise ouvrante dans la pile, cette balise fermante est en excès.
                    return False, f"Balise fermante '{tag_name}' sans balise ouvrante correspondante.", match.start()

                last_open_tag, last_open_pos = stack[-1] # Récupérer la dernière balise ouvrante
                if last_open_tag == tag_name:
                    # Si la balise fermante correspond à la dernière balise ouvrante, la retirer de la pile.
                    stack.pop()
                else:
                    # Sinon, il y a un chevauchement ou une balise fermante incorrecte.
                    # Détecte la première erreur de chevauchement ou de fermeture.
                    error_message = (
                        f"Balise fermante '{tag_name}' à la position {match.start()} "
                        f"ne correspond pas à la balise ouvrante la plus récente '{last_open_tag}' "
                        f"à la position {last_open_pos} (chevauchement ou balise incorrecte)."
                    )
                    return False, error_message, match.start()

        # --- 3. Vérification des balises ouvrantes non fermées à la fin de la chaîne ---
        # Si la pile n'est pas vide à la fin, cela signifie qu'il y a des balises ouvrantes non fermées.
        if stack:
            last_open_tag, last_open_pos = stack[-1]
            return False, f"Balise ouvrante '{last_open_tag}' non fermée.", last_open_pos

        # Si aucune erreur n'a été trouvée, la chaîne est valide.
        return True, "Aucune erreur détectée.", -1

# Exemple d'utilisation:
if __name__ == "__main__":
    validator = TagValidator()

    test_cases = [
        ("<div><p>Texte</p></div>", True),
        ("<div><p>Texte</div>", False), # Manque </p>, chevauchement
        ("<div><p>Texte</P></div>", False), # Mauvaise casse (mais le validator convertit en minuscule pour comparaison)
        ("<div>Texte", False), # Balise ouvrante non fermée
        ("div>Texte</div>", False), # Omission de chevron au début
        ("<div", False), # Omission de chevron à la fin
        ("<h1>Titre</h2>", False), # Chevauchement
        ("<span>texte", False), # Non fermé
        ("<br><p>test</p>", True), # <br> est auto-fermé
        ("<!DOCTYPE html><html><body><h1>Titre</h1></body></html>", True), # Avec doctype
        ("<div><img src='...'/></div>", True), # Auto-fermante correcte
        ("<baliseInconnue>texte</baliseInconnue>", False), # Balise inconnue
        ("<div><script>alert('Hello');</script></div>", True), # Balise avec script
        ("<div><p>text</span></p></div>", False), # Balise fermante incorrecte / chevauchement
        ("Ceci est du texte pur.", True), # Aucun tag, donc valide.
        ("<div class=test", False), # Omission de chevron
        ("Hello world <tag>", False), # Tag inconnu et potentiellement malformé
        ("<div><p>Hello</div></p>", False), # Mauvais ordre de fermeture
        ("<div><span><p>Text</p></span></div>", True),
        ("<div><span><p>Text</span></div></p>", False), # chevauchement
        ("<div><span><p>Text</p></div></span>", False), # chevauchement
    ]

    print("--- Tests de Validation des Balises ---")
    for i, (html, expected_validity) in enumerate(test_cases):
        is_valid, message, position = validator.validate(html)
        status = "VALIDE" if is_valid else "INVALIDE"
        print(f"\nTest {i+1}:")
        print(f"Chaîne: '{html}'")
        print(f"Résultat: {status} (Attendu: {'VALIDE' if expected_validity else 'INVALIDE'})")
        print(f"Message: {message}")
        if position != -1:
            print(f"Position de l'erreur: {position}")
            print(f"Extrait: '{html[position:position+20]}...'") # Afficher un extrait autour de l'erreur
        
        if is_valid != expected_validity:
            print("!!! ÉCHEC DU TEST !!!")
