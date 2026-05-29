# # Écrire une fonction rendre_monnaie(pieces, somme) qui prend en paramètre :
# # pieces : Une liste d'entiers positifs représentant les valeurs des pièces disponibles (ex: [1, 2, 5, 10]). 
# # somme : Un entier représentant le montant total à rendre.
# # La fonction doit retourner le nombre minimal de pièces nécessaires pour obtenir exactement cette somme. 
# # Si la somme ne peut pas être atteinte avec les pièces disponibles, la fonction doit retourner -1.

# # Votre algorithme doit trouver la solution optimale, peu importe le système de pièces fourni.

# # --- LA FONCTION A IMPLEMENTER ---
# # from functools import cache

# # def rendre_monnaie(pieces, somme):
# #     def compute(pieces, somme):
# #         if somme == 0:
# #             return 0
# #         pieces_dispo = tuple([p for p in pieces if p <= somme])
# #         values = []
# #         for p in pieces_dispo:
# #             res = compute(pieces_dispo, somme - p)
# #             if res != -1:
# #                 values.append(1 + res)
# #         return min(values) if values else -1
# #     return compute(tuple(pieces), somme)

# # def rendre_monnaie(pieces, somme):
# #     inf = float('inf')
# #     cache = [0] + [inf] * somme
# #     for v in range(1, somme + 1):
# #         pieces_dispo = [p for p in pieces if p <= v]
# #         for p in pieces_dispo:
# #             cache[v] = min(cache[v], 1 + cache[v - p])  
# #     return cache[somme] if cache[somme] != inf else -1

# from functools import cache


# # def rendre_monnaie(pieces, somme):
# #     @cache
# #     def compute(pieces, somme):
# #         if somme == 0:
# #             return 0
# #         if somme in pieces:
# #             return 1
# #         pieces_dispo = tuple([p for p in pieces if p <= somme])
# #         options = []
# #         for p in pieces_dispo:
# #             nb_pieces = compute(pieces_dispo, somme - p)
# #             if nb_pieces != -1:
# #                 options.append(nb_pieces + 1)
# #         return min(options) if options else -1

# #     return compute(tuple(pieces), somme)

# def rendre_monnaie(pieces, somme):
#     inf = float('inf')
#     dp = [0] + [inf] * somme

#     for v in range(1, somme + 1):
#         pieces_dispo = [p for p in pieces if p <= v]
#         for p in pieces_dispo:
#             res = dp[v - p] + 1
#             dp[v] = min(dp[v], res)
#     return dp[somme] if dp[somme] != inf else -1


def rendre_monnaie(pieces, somme):
    pass
    

print("Démarrage des tests...")

# Test 1 : Cas de base
print("Test 1...", rendre_monnaie([1, 2, 5], 0))
assert rendre_monnaie([1, 2, 5], 0) == 0, "Échec Test 1 : Somme 0 doit renvoyer 0 pièce"

# Test 2 : Pièce exacte
print("Test 2...", rendre_monnaie([1, 2, 5], 5))
assert rendre_monnaie([1, 2, 5], 5) == 1, "Échec Test 2 : Somme égale à une pièce doit renvoyer 1"

# Test 3 : Système Euro (Glouton compatible)
print("Test 3...", rendre_monnaie([1, 2, 5, 10], 11))
assert rendre_monnaie([1, 2, 5, 10], 11) == 2, "Échec Test 3 : 11 devrait faire 2 pièces (10+1)"

# Test 4 : Le piège glouton
print("Test 4...", rendre_monnaie([1, 3, 4], 6))
assert rendre_monnaie([1, 3, 4], 6) == 2, "Échec Test 4 : Piège glouton ! 6 doit faire 2 pièces (3+3)"

# Test 5 : Cas impossible
print("Test 5...", rendre_monnaie([2, 5], 3))
assert rendre_monnaie([2, 5], 3) == -1, "Échec Test 5 : Impossible de faire 3 avec des pièces de 2 et 5, doit renvoyer -1"

# Test 6 : Performance (Grand montant)
print("Test 6...", rendre_monnaie([1, 5, 10, 25], 99))
assert rendre_monnaie([1, 5, 10, 25], 99) == 9, "Échec Test 6 : Grand montant erroné"

# Test 7 : Le piège glouton complexe
print("Test 7...", rendre_monnaie([2, 14, 20], 28))
assert rendre_monnaie([2, 14, 20], 28) == 2, "Échec Test 7 : Piège glouton complexe ! 28 doit faire 2 pièces (14+14)"

# Test 8 : Performance extrême (Explosion de l'arbre récursif sans cache)
print("Test 8 (Test de performance)...", rendre_monnaie([1, 2, 5, 10, 20, 50], 320))
assert rendre_monnaie([1, 2, 5, 10, 20, 50], 320) == 7, "Échec Test 8 : Trop lent ou mauvaise réponse"

# Test 9 : Le pire cas pour la récursion (Grand montant et impossible)
print("Test 9 (Test de performance en cas impossible)...", rendre_monnaie([4, 6, 8], 2001))
assert rendre_monnaie([4, 6, 8], 2001) == -1, "Échec Test 9 : Devrait détecter l'impossibilité rapidement"

print("\nTous les tests sont passés avec succès !")


