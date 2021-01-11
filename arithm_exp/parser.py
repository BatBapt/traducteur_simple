#!/usr/bin/python3


def reste1():
    global pc, op_postfix
    if pc < len(ch):
        if ch[pc][0] == "OP":
            if ch[pc][1] == "+":
                pc += 1
                if terme():
                    op_postfix.append("+")
                    return reste1()

            elif ch[pc][1] == "-":
                pc += 1
                if terme():
                    op_postfix.append("-")
                    return reste1()
            else:
                return True
        else:
            return True
    else:
        return True

def reste2():
    global pc, op_postfix
    if pc < len(ch):
        if ch[pc][0] == "OP":
            if ch[pc][1] == "*":
                pc += 1
                if terme():
                    op_postfix.append("*")
                    return reste2()
            elif ch[pc][1] == "/":
                pc += 1
                if terme():
                    op_postfix.append("/")
                    return reste2()
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
    global pc, op_postfix

    try:
        cc = ch[pc]
    except IndexError:
        # Si on dépasse la taille de la chaine, c'est qu'il y a une erreur
        return False

    if cc[0] == "PAR_OUV":
        if reconnaitre(cc[1]) and exp() and reconnaitre(")"):
            return True

    elif cc[1].isdigit():
        op_postfix.append(cc[1])
        pc += 1
        return True
    else:
        error()
        return False


def error():
    """
    Fonction errerur qui affiche le caractère d'où provient l'erreur
    """
    if not ch[pc][1].isdigit():
        print("Erreur au niveau du caractère '{}' à la position {}".format(ch[pc][1], pc))


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
    return False, pc


def debug(s):
    """
    Fonction de déboggage (au lieu de faire plein de print partout)
    """
    print(s)
    print(s, pc, ch[pc])


def parser(ul):
    """
    Fonction principale qui va transformer une liste d'unité lexicale
    en écriture postfixée
    """
    assert isinstance(ul, list), "Le paramètre n'est pas une liste"
    global op_postfix, pc, ch
    op_postfix = []
    pc = 0
    ch = ul
    return exp()
