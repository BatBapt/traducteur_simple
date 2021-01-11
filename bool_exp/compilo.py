 #!/usr/bin/python3
import sys
import os
try:
    from parser import parser
    from scanner import scanner
    from codegen import codegen
except ImportError:
    print("Erreur lors de l'import d'un fichier")
    sys.exit(-1)


def main(src):
    try:
        fo = open(src, "r")
        fo.close()
    except IOError:
        print("Le fichier donné n'existe pas.")
        return 0

    with open(src) as file:
        exp = file.read()

    #  On transforme la chaine d'entrée en une liste d'unité lexicale
    ul = scanner(exp)

    #  On convertit cette liste en une liste contenant l'expression postfixé
    postfix = parser(ul)
    if postfix[0]:
        # print("Chaine valide") # A commenter pour la lisibilité lors des test
        # print(postfix[1])

        # On écrit dans un fichier sous forme d'une pile l'expression
        codegen(postfix[1])
        os.chmod("a.out", 0o744)
        return True
    else:
        index_err = exp.index(postfix[1])
        print("Erreur syntaxique à la position {}: {}Il manque une partie "\
        "de l'expression\n".format(index_err, exp[index_err:]))
        return False

if __name__ == "__main__":
    try:
        file = sys.argv[1]
    except:
        print("\nIl manque un paramètre: le fichier contenant l'expression\n")
        sys.exit(-1)
    main(file)
