#!/usr/bin/python3

def codegen(postfix):
    """
    Cette fonction prends en paramètre une liste, puis va écrire dans un fichier
    cette expression en l'évaluant sous forme d'une pile
    """
    with open("a.out", "w") as file:
        i = 1
        cpt_t = 0
        file.write("#!/usr/bin/python3\n\n")
        for elem in postfix:
            if elem in ['VRAI', 'FAUX']:
                if elem == "VRAI":
                    boolean = "True"
                else:
                    boolean = "False"
                file.write("t{} = {}\n".format(i, boolean))
                cpt_t += 1
                i += 1
            elif elem in ["OU", "ET"]:
                if elem == "OU":
                    file.write("t{} = t{} or t{}\n".format(cpt_t-1, cpt_t-1, cpt_t))
                elif elem == "ET":
                    file.write("t{} = t{} and t{}\n".format(cpt_t-1, cpt_t-1, cpt_t))

                cpt_t -= 1
                i -= 1

            elif elem == "NON":
                file.write("t{} = not t{}\n".format(cpt_t, cpt_t))

        file.write("print(t{})".format(cpt_t))
