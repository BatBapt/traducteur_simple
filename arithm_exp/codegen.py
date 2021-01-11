#!/usr/bin/python3


def codegen(postfix):
    """
    Cette fonction prends en paramètre une liste, puis va écrire dans un fichier
    cette expression en l'évaluant sous forme d'une pile
    """
    assert isinstance(postfix, list), "Le paramètre n'est pas une liste"
    with open("a.out", "w") as file:
        i = 1
        cpt_t = 0
        file.write("#!/usr/bin/python3\n\n")
        for elem in postfix:
            if elem.isdigit():
                cpt_t += 1
                file.write("t{} = {}\n".format(i, elem))
                i += 1
            else:
                file.write("t{} = t{} {} t{}\n".format(cpt_t-1, cpt_t-1, elem, cpt_t))
                cpt_t -= 1
                i -= 1


        file.write("print(t{})".format(cpt_t))
