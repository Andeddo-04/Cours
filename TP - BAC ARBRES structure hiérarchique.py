import bisect

class ArbreHuffman:
    def __init__(self, lettre, nbocc, g=None, d=None):
        self.lettre = lettre
        self.nbocc = nbocc
        self.gauche = g
        self.droite = d

    def est_feuille(self) -> bool:
        return self.gauche == None and self.droit == None # A completer
    
    def __lt__(self, other):
    # un arbre A est strictement inférieur à un arbre B
    # si le nombre d'occurrences indiqué dans A est
    # strictement **supérieur** à celui de B
        return self.nbocc > other.nbocc
    
# ******************************************************************************************************************
# ******************************************************************************************************************

def parcours(arbre, chemin_en_cours, dico):
    
    if arbre is None:
        return "Arbre vide !"
    
    if arbre.est_feuille():
        dico[arbre.lettre] = chemin_en_cours
    
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        parcours(arbre.droit, chemin_en_cours + [1], dico) # A completer

        
def fusionne(gauche, droite) -> ArbreHuffman:
    nbocc_total = self.g + self.d
    return ArbreHuffman(None, nbocc_total, gauche, droite)


def compt_occurrences(texte: str) -> dict:
    """
    Renvoie un dictionnaire avec chaque caractère du texte comme clé et le nombre d'apparition de ce
    caractère dans le texte en valeur
    
    >>> compte_occurences("AABCECA")
    {"A":3, "B" :1, "C":2, "E":1}
    """
    
    occ = dict()
    
    for car in texte:
        if car not in occ:
            ...
            occ[car] = occ[car] + 1
    return ...


def construit_liste_arbres(texte: str) -> list:
    """ Renvoie une liste d'arbres de Huffman, chacun réduit à une feuille """
    dic_occurrences = compt_occurrences(texte)
    liste_arbres = []
    
    for lettre, occ in dic_occurrences.items():
        liste_arbres.append(ArbreHuffman(lettre, occ))
    
    return liste_arbres


def codage_huffman(texte: str) -> dict:
    """ Codage de Huffman optimal à partir d'un texte
    >>> codage_huffman("AAAABBBBBCCD")
    {'A': [0, 0], 'C': [0, 1, 0], 'D': [0, 1, 1], 'B': [1]}"""
    
    liste_arbres = construit_liste_arbres(texte)
    # Tri par nombres d'occurrences décroissants
    liste_arbres.sort()
    
    while len(liste_arbres) > 1:# Tant que tous les arbres n'ont pas été fusionnés
        
        droite = liste_arbres.pop()# Les deux plus petits nombres d'occurrences sont à la fin de la liste
        gauche = liste_arbres.pop()
        new_arbre = fusionne(gauche, droite)
        bisect.insort(liste_arbres, new_arbre)# Le module bisect permet d'insérer le nouvel arbre dans
                                              # la liste, de manière à ce que la liste reste triée
    
    arbre_huffman = liste_arbres.pop()# Il ne reste plus qu'un arbre dans la liste, c'est notre arbre de Huffman
    dico = {}# Parcours de l'arbre pour relever les codes
    parcours(arbre_huffman, [], dico)
    return dico

# ******************************************************************************************************************
# ******************************************************************************************************************

# Script principal
with open("texte.txt") as f:
    texte = f.read()
print(codage_huffman(texte))