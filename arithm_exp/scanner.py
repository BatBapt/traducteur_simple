#!/usr/bin/python3

def scanner(s):
    """
    Cette fonction va transformer la chaine de caractère passée en paramètre
    en une liste d'unitée lexicale
    """
    assert isinstance(s, str), "Le paramètre n'est pas une chaine de caractère"
    unity_lex = []
    i = 0
    while i < len(s):
        car = s[i]
        if car.isdigit():
            multiple_int = ""
            j = i
            while j < len(s): # On parcourt la chaine s'il y a des nombres > 9
                if s[j].isdigit():
                    multiple_int += s[j]
                else:
                    break
                j += 1
            unity_lex.append(("NOMBRE", multiple_int))
            i = j - 1
        elif car == "(":
            unity_lex.append(("PAR_OUV", car))
        elif car == ")":
            unity_lex.append(("PAR_FER", car))
        elif car in ["*", "/", "+", "-"]:
            unity_lex.append(("OP", car))
        elif car == " ": # cette condition sert à ignorer les espaces
            pass
        i += 1
    return unity_lex
