Voici l'énoncé officiel et les exemples de tests pour le défi **CheckDOM** (Odoo / Coderbyte) :

---

## Énoncé du problème

Créez une fonction `CheckDOM(strParam)` qui lit le paramètre `strParam` fourni, lequel est une chaîne de caractères contenant des éléments HTML et du texte brut.

Les seuls éléments HTML utilisés dans ce défi sont : `<b>`, `<i>`, `<em>`, `<div>`, et `<p>`.

Votre programme doit gérer **3 cas spécifiques** :

1. **La chaîne est correcte :** Si la séquence d'éléments HTML est correctement imbriquée, le programme doit retourner la chaîne de caractères `"true"`.
2. **La chaîne est presque correcte :** Si en modifiant **un seul et unique tag** (balise) la séquence devient correcte, le programme doit retourner le **nom** du premier tag à modifier (sans les chevrons `< >`).
* *Note :* Modifier un tag signifie changer son type (ex: transformer un `<div>` en `<b>`). Cela n'inclut pas l'ajout ou la suppression d'un tag, ni la transformation d'une balise ouvrante en balise fermante (ou inversement).


3. **La chaîne est incorrecte :** Si la chaîne nécessite de modifier plus d'un élément pour devenir correcte (ou si l'ordre des balises ouvrantes/fermantes est totalement incohérent), votre programme doit retourner la chaîne de caractères `"false"`.

---

## Exemples de tests

* **Exemple 1**
* **Input :** `"<div><b><p>hello world</p></b></div>"`
* **Output :** `true`
* **Raison :** L'HTML est parfaitement et correctement imbriqué.


* **Exemple 2**
* **Input :** `"<div><i>hello</i>world</b>"`
* **Output :** `"div"`
* **Raison :** Si le premier élément `<div>` était remplacé par un `<b>`, la chaîne deviendrait `<b><i>hello</i>world</b>`, ce qui est correctement imbriqué.


* **Exemple 3**
* **Input :** `"</div><p></p><div>"`
* **Output :** `false`
* **Raison :** L'ordre des balises ouvrantes et fermantes n'est pas respecté du tout. Modifier une seule balise ne suffit pas à rendre l'ensemble correct.


* **Exemple 4**
* **Input :** `"<em></em><em></em><p></b>"`
* **Output :** `"p"`
* **Raison :** Les deux blocs `<em></em>` sont corrects. À la fin, si on remplace `<p>` par `<b>`, la séquence devient correcte.


* **Exemple 5**
* **Input :** `"<div><p></p><b><p></div>"`
* **Output :** `false`
* **Raison :** Plus d'une modification est nécessaire pour équilibrer la structure.