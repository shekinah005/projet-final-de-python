# Module: html_parser.py
# Analyseur HTML et constructeur d'arborescence DOM

class Node:
    def __init__(self, tag, attributes=None, text='', parent=None):
        self.tag = tag
        self.attributes = attributes if attributes else {}
        self.children = []
        self.text = text.strip()
        self.parent = parent

    def add_child(self, node):
        self.children.append(node)

def parse_html(html):
    import re
    from html import unescape

    stack = []
    root = Node("root")
    current = root
    tag_pattern = re.compile(r"<(/?)([a-zA-Z0-9]+)([^>]*)>")
    pos = 0

    while pos < len(html):
        match = tag_pattern.search(html, pos)
        if not match:
            text = html[pos:].strip()
            if text:
                current.add_child(Node("text", text=unescape(text), parent=current))
            break

        if match.start() > pos:
            text = html[pos:match.start()].strip()
            if text:
                current.add_child(Node("text", text=unescape(text), parent=current))

        is_closing, tag, attr_string = match.groups()
        if is_closing:
            if stack:
                current = stack.pop()
        else:
            attributes = dict(re.findall(r'(\w+)\s*=\s*"([^"]*)"', attr_string))
            new_node = Node(tag.lower(), attributes, parent=current)
            current.add_child(new_node)
            stack.append(current)
            current = new_node
        pos = match.end()
    return root
