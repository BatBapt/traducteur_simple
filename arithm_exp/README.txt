###### Grammaire du traducteur pour les expression arithmétiques ######

Grammaire élémentaire:

T = {0,1,2,3,4,5,6,7,8,9}
N = {expr}
S = expr
P = expr -> expr + terme
          | expr - terme
          | 0 | 1 | ... | 9

Supprimer l'associativité à gauche:

expr -> expr + terme
    |   expr - terme
    |   terme
terme -> terme * facteur
    |   terme / facteur
    |   facteur
facteur -> chiffre
    |   ( expr )
chiffre -> 0|1|..|9

Supprime la récursivité à gauche:

expr -> terme reste1
reste1 -> +terme reste1  # {empiler ("+")}
    |   -terme reste1   # {empiler ("-")}
    |   E   # E = vide
terme -> facteur reste2
reste2 -> *facteur reste2 # {empiler ('*')}
    |   /facteur reste2 # {empiler ('/')}
    |   E   # E = vide
facteur -> chiffre
    | (expr)

terme -> 0|1..|9 {empiler(terme)}


###### Les différentes fonction/fichier du programme ######

Pour mieux expliquer le fonctionnement du programme, nous allons utiliser la chaîne suivante : 1+2*3 (qui donne 7)

scanner.py :
Ce fichier contient l’unique fonction  ‘scanner’.
Cette fonction attend en paramètre une chaîne de caractère : la chaîne d’expression à évaluer. Cette fonction va traiter la chaîne, en renvoyant une liste de l’expression lexical du paramètre.
- Avec la chaîne décrite ci-dessus, cette fonction va nous renvoyer :
[(‘NOMBRE’, ‘1’), (‘OP’, ‘+’), (‘NOMBRE’, ‘2’), (‘OP’, ‘*’), (‘NOMBRE’, 3’)]

parser.py:
Ce fichier contient la fonction principale 'parser'.
Cette fonction prends en paramètre une liste d'unité lexicale de la chaîne à
traduire et renvoie le tuple (True, op_postfix) si tout s’est déroulé correctement, ou le tuple (False, pc) si une erreur dans la chaîne est rencontré. La variable ‘op_postfix’ étant l’évaluation postfixéé (ou écriture polonaise inversée) de la chaîne. Cette fonction fait appelle aux autres fonctions, la première étant la fonction 'exp' qui elle même va appeler toutes les autres fonction (en fonction de la chaîne initiale)
- Résultat de la fonction parser avec la liste au dessus :
(True, ['1', '2', '3', '*', '+'])

codegen.py :
Ce fichier contient uniquement la fonction ‘codegen’.
Cette fonction reçoit en paramètre une liste de l’expression postfixé de la chaîne initiale. Cette est uniquement exécutée si la fonction ‘parser’ décrite ci-dessus renvoie True.
Cette fonction va se charger de créer un fichier ‘a.out’ qui va contenir la version Python de la chaine à évaluer, sous forme d’une pile.
- En exécutant cette fonction, le fichier ‘a.out’ va contenir le programme suivant :

#!/usr/bin/python3

t1 = 1
t2 = 2
t3 = 3
t2 = t2 * t3
t1 = t1 + t2
print(t1)


compilo.py :
Ce fichier est l’entrée de toute le programme. Cette fonction va appeler toutes les autres, ainsi que les modules natifs python : ‘sys’ et ‘os’. Ces modules vont nous permettent de manipuler le fichier ‘a.out’ ou encore de récupérer en entrée une expression.
Cette fonction prends en paramètre un chemin d’accès à un fichier contenant l’expression arithmétique à évaluer (dans notre programme c’est le fichier ‘exp.txt’)
Dedans, elle va d’abord vérifier que le fichier existe, puis elle va appeler la fonction scanner, puis parser, puis (si et seulement si parser renvoie ‘True’) elle va appeler la fonction codegen.
Grâce au module os et à la ligne ‘os.chmod(‘’a.out’’, 0o744)’, on donne des droits d’exécution au fichier ‘a.out’ pour pouvoir le lancer depuis un terminal avec la ligne ‘./a.out’ ce qui nous renvoit bien : 7


###### Les fichiers/fonction de test du programme ######

Le programme contient 4 fichier python test utilisant le module natif python : unittest. Chaque fichier de test est nommée en suivant la règle ‘test_NomDuFichierATester.py’. Ils commencent tous par ‘test’ afin que tous soit rangé au même endroit.
Dans chacun des fichier, une classe est crée en suivant la règle TestNomDuFichierATester. Cette classe va hérité de la classe TestCase du module.
La première méthode de chaque classe est la méthode ‘setUp’ qui va permettre d’initialiser différentes variable nécessaire aux autres méthodes de la classe (pour éviter d’avoir à écrire les mêmes choses, parfois un peu verbeux)

- Prenons le fichier ‘test_codegen.py’.

La classe crée est TestCodegen.
Sa méthode setUp contient :
    • une variable d’une expression postfixée sous forme d’une liste
    • une variable contenant le dernier élément de la chaîne
    • une variable contenant le premier élément de la chaîne

Les autres méthodes sont, successivement :
    • Une méthode qui test si l’expression postfixée est bien sous forme d’une liste
    • Comme c’est une expression postfixée, le dernier élément est forcément un opérateur binaire. Cette méthode test si le dernier élément en est bien un
    • Pareil, comme c’est une expression postfixée, le premier élément est forcément un nombre. Cette méthode le test

Pour exécuter ce fichier test en particulier, on peut tout simplement écrire dans un terminal la ligne suivante :
python3 test_codegen.py -v

L’option -v (verbose) affiche chaque nom de test passé.
Sans cette option, un point ‘.’ est affiché pour chaque test passé.

Pour exécuter tout les tests de tout les fichiers en une seule fois, on peut lancer la commande :
python3 -m unittest -v

L’option -m permet d’appeler un module spécifique, ici unittest.



