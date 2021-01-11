#!/usr/bin/python3

def scanner(s):
    """
    Cette fonction va transformer la chaine de caractère passée en paramètre
    en une liste d'unitée lexicale
    Les valeurs de i (indice de parcours de boucle) sont incrémentés
    différement en fonction de la condition et de la taille de la valeur lue
    """
    unity_lex = []
    i = 0
    while i < len(s):
        car = s[i]
        if car in ["V", "F"]:
            if car == "V":
                unity_lex.append(("BOOL", "VRAI"))
            else:
                unity_lex.append(("BOOL", "FAUX"))
            i += 4
        elif car == "(":
            unity_lex.append(("PAR_OUV", car))
            i += 1
        elif car == ")":
            unity_lex.append(("PAR_FER", car))
            i += 1
        elif car in ["O", "E", "N"]:
            if car == "O":
                unity_lex.append(("CONDI", "OU"))
                i += 2
            elif car == "E":
                unity_lex.append(("CONDI", "ET"))
                i += 2
            else:
                unity_lex.append(("CONDI", "NON"))
                i += 3
        elif car == " ": # cette condition sert à ignorer les espaces
            pass
        i += 1
    return unity_lex
