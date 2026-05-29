import re

tag_pattern = r'<(.+?)>'
def CheckDOM(strParam: str):
    copy = strParam
    open = []
    error = None
    while True:
        m = re.search(tag_pattern, copy)
        if not m:
            if open:
                return False
            break
        if '/' in m.group(1):
            if not open or open[-1] != m.group(1)[1:]:
                if error:
                    return False
                if open:
                    error = open[-1]
                    open.pop()
                else:
                    return False
            else:
                open.pop()
        else:
            open.append(m.group(1))
        copy = copy[m.span()[1]:]
    return error or True

# --- Cas de succès (True) ---
# Chaîne vide (pas de balise, donc techniquement valide)
assert CheckDOM("") is True

# Uniquement du texte brut
assert CheckDOM("hello world sans balises") is True

# Plusieurs blocs valides consécutifs
assert CheckDOM("<div></div><p><span></span></p>") is True

# Balises imbriquées profondément
assert CheckDOM("<html><body><div><ul><li>texte</li></ul></div></body></html>") is True


# --- Cas d'erreur unique (Doit retourner le nom de la balise attendue) ---
# Oubli de fermer la balise parente à la toute fin
assert CheckDOM("<div><p>hello</p>") is False

# Inversion de fermeture (ferme 'p' au lieu de 'b', 'b' devient l'erreur car 'p' ne correspond pas à l'élément au sommet de la pile)
assert CheckDOM("<div><b>hello</b><p>world</b></div>") == "p"

# Balise ouvrante orpheline au milieu du texte
assert CheckDOM("<h1>title</h1><span>content") is False


# --- Cas d'échec total (False) ---
# Plus d'une seule erreur (ici, 'i' est mal fermé, puis 'b' est mal fermé)
assert CheckDOM("<div><i>hello</b><p>world</strong></div>") is False

# Balise fermante orpheline au début (la pile 'open' est vide, donc renvoie False immédiatement)
assert CheckDOM("</b><div></div>") is False

# Balise fermante sans aucune balise ouvrante correspondante à la fin
assert CheckDOM("<div>hello</div></strong>") is False

# Inversion flagrante de hiérarchie imbriquée (fermeture croisée)
assert CheckDOM("<div><span></div></span>") is False


print("Tous les nouveaux tests ont également été validés !")