#!/usr/bin/python3


def reste1():
    global pc, op_postfix, err
    if pc < len(ch):
        if ch[pc][0] == "CONDI":
            if ch[pc][1] == "OU":
                pc += 1
                if terme():
                    op_postfix.append("OU")
                    return reste1()
                else:
                    err = "OU"
                    return False
            else:
                return False
        else:
            return True
    else:
        return True

def reste2():
    global pc, op_postfix, err
    if pc < len(ch):
        if ch[pc][0] == "CONDI":
            if ch[pc][1] == "ET":
                pc += 1
                if terme():
                    op_postfix.append("ET")
                    return reste2()
                else:
                    err = "ET"
                    return False
            else:
                return True
        else:
            return True
    else:
        return True


def terme():
    if facteur():
        if reste2():
            return True
    return False

def facteur():
    global pc, op_postfix, err
    try:
        cc = ch[pc]
    except IndexError:
        return False
    if cc[0] == "CONDI":
        if cc[1] == "NON":
            pc += 1
            if facteur():
                op_postfix.append(cc[1])
                return True
            else:
                err = "NON"

    elif cc[0] == "PAR_OUV":
        if reconnaitre(cc[1]) and exp() and reconnaitre(")"):
            return True
    elif cc[1] in ["VRAI", "FAUX"]:
        op_postfix.append(ch[pc][1])
        pc += 1
        return True
    else:
        error()
        return False


def error():
    """
    Fonction errerur qui affiche le caractère d'où provient l'erreur
    """
    print(ch)
    # print("Erreur au caractère '{}' à la position {}".format(ch[pc], pc))

def reconnaitre(car):
    global pc
    if car == ch[pc][1]:
        pc += 1
        return True
    else:
        return False


def exp():
    if terme():
        if reste1():
             # On retourne op_postfix pour pouvoir
             # l'utiliser dans la suite du programme
            return True, op_postfix
    return False, err

def debug(s):
    """
    Fonction de déboggage (au lieu de faire plein de print partout)
    """

    print(s, pc, ch[pc])


def parser(ul):
    """
    Fonction principale qui va transformer une liste d'unitées lexicale
    en écriture postfixée
    """
    assert isinstance(ul, list), "Le paramètre n'est pas une liste"
    global op_postfix, pc, ch, err
    err = ""
    op_postfix = []
    pc = 0
    ch = ul
    return exp()
