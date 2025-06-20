# Module 4 - Inspection

import re  # Importation du module requis

from html_parser import DOMNode, SimpleHTMLParser  # Instruction



def print_all_tags(dom_node, tags=None):  # Définition d'une fonction

    if tags is None:  # Instruction

        tags = set()  # Instruction

    if dom_node.tag:  # Instruction

        tags.add(dom_node.tag)  # Instruction

    for child in dom_node.children:  # Instruction

        print_all_tags(child, tags)  # Instruction

    return tags  # Instruction



def print_dom_tree(node, indent=0):  # Définition d'une fonction

    prefix = '  ' * indent  # Instruction

    if node.tag:  # Instruction

        print(f"{prefix}<{node.tag}>")  # Instruction

    elif node.content:  # Instruction

        print(f"{prefix}{node.content}")  # Instruction

    for child in node.children:  # Instruction

        print_dom_tree(child, indent + 1)  # Instruction



def print_text_by_tag(node, target_tag):  # Définition d'une fonction

    if node.tag == target_tag:  # Instruction

        for child in node.children:  # Instruction

            if child.content:  # Instruction

                print(child.content)  # Instruction

    for child in node.children:  # Instruction

        print_text_by_tag(child, target_tag)  # Instruction



def count_external_links(html):  # Définition d'une fonction

    pattern = r'<a\s+[^>]*href=["\'](http[^"\']+)["\']'  # Instruction

    return len(re.findall(pattern, html))  # Instruction



def display_error_stats(errors, total_tags):  # Définition d'une fonction

    print("\n📊 Statistiques :")  # Instruction

    print(f"- Total de balises : {total_tags}")  # Instruction

    print(f"- Balises incorrectes : {len(errors)}")  # Instruction

    print(f"- Balises correctes : {total_tags - len(errors)}")  # Instruction

    print(f"- Taux d’erreur : {(len(errors) / total_tags * 100):.2f}%")  # Instruction



def highlight_errors(html, errors):  # Définition d'une fonction

    print("\n Erreurs détectées dans le contenu HTML :")  # Instruction

    for pos, msg in errors:  # Instruction

        if pos >= 0:  # Instruction

            snippet = html[max(0, pos - 20):pos + 20]  # Instruction

            print(f"{msg} : ...{snippet}...")  # Instruction

        else:  # Instruction

            print(msg)  # Instruction
