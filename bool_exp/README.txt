###### Grammaire du traducteur pour les expression arithmétiques ######

Grammaire élémentaire :

T = {VRAI, FAUX, OU, ET, NON}
N = {expr}
s = expr
P = expr → expr OU expr
	   | expr ET expr
	   | NON expr
	   | (expr)

Gramme modifié :

exp -> exp OU terme
     | terme

terme -> terme ET facteur
     | facteur

facteur -> NON facteur
     | ( exp )
     | bool

bool -> Vrai | Faux


###### Les différentes fonction/fichier du programme ######

Pour mieux expliquer le fonctionnement du programme, nous allons utiliser la chaîne suivante : ‘VRAI OU NON VRAI ET FAUX’

scanner.py :
Ce fichier contient l’unique fonction  ‘scanner’.
Cette fonction attend en paramètre une chaîne de caractère : la chaîne d’expression à évaluer. Cette fonction va traiter la chaîne, en renvoyant une liste de l’expression lexical du paramètre.
- Avec la chaîne décrite ci-dessus, cette fonction va nous renvoyer :
[('BOOL', 'VRAI'), ('CONDI', 'OU'), ('CONDI', 'NON'), ('BOOL', 'VRAI'), ('CONDI', 'ET'), ('BOOL', 'FAUX')]

parser.py:
Ce fichier contient la fonction principale 'parser'.
Cette fonction prends en paramètre une liste d'unité lexicale de la chaîne à
traduire et renvoie le tuple (True, op_postfix) si tout s’est déroulé correctement, ou le tuple (False, err) si une erreur dans la chaîne est rencontré. La variable ‘op_postfix’ étant l’évaluation postfixée (ou écriture polonaise inversée) de la chaîne. Cette fonction fait appelle aux autres fonctions, la première étant la fonction 'exp' qui elle même va appeler toutes les autres fonction (en fonction de la chaîne initiale)
- Résultat de la fonction parser avec la liste au dessus :
(True, ['VRAI', 'VRAI', 'NON', 'FAUX', 'ET', 'OU'])

codegen.py :
Ce fichier contient uniquement la fonction ‘codegen’.
Cette fonction reçoit en paramètre une liste de l’expression postfixé de la chaîne initiale. Cette est uniquement exécutée si la fonction ‘parser’ décrite ci-dessus renvoie True.
Cette fonction va se charger de créer un fichier ‘a.out’ qui va contenir la version Python de la chaine à évaluer, sous forme d’une pile.
- En exécutant cette fonction, le fichier ‘a.out’ va contenir le programme suivant :


#!/usr/bin/python3

t1 = True
t2 = True
t2 = not t2
t3 = False
t2 = t2 and t3
t1 = t1 or t2
print(t1)


compilo.py :
Ce fichier est l’entrée de toute le programme. Cette fonction va appeler toutes les autres, ainsi que les modules natifs python : ‘sys’ et ‘os’. Ces modules vont nous permettent de manipuler le fichier ‘a.out’ ou encore de récupérer en entrée une expression.
Cette fonction prends en paramètre un chemin d’accès à un fichier contenant l’expression arithmétique à évaluer (dans notre programme c’est le fichier ‘exp.txt’)
Dedans, elle va d’abord vérifier que le fichier existe, puis elle va appeler la fonction scanner, puis parser, puis (si et seulement si parser renvoie ‘True’) elle va appeler la fonction codegen.
Grâce au module os et à la ligne ‘os.chmod(‘’a.out’’, 0o744)’, on donne des droits d’exécution au fichier ‘a.out’ pour pouvoir le lancer depuis un terminal avec la ligne ‘./a.out’ ce qui nous renvoit bien : True


###### Les fichiers/fonction de test du programme ######

Le programme contient 4 fichier python test utilisant le module natif python : unittest. Chaque fichier de test est nommée en suivant la règle ‘test_NomDuFichierATester.py’. Ils commencent tous par ‘test’ afin que tous soit rangé au même endroit.
Dans chacun des fichier, une classe est crée en suivant la règle TestNomDuFichierATester. Cette classe va hérité de la classe TestCase du module.
La première méthode de chaque classe est la méthode ‘setUp’ qui va permettre d’initialiser différentes variable nécessaire aux autres méthodes de la classe (pour éviter d’avoir à écrire les mêmes choses, parfois un peu verbeux)

Prenons le fichier ‘test_scanner.py’.

La classe crée est TestScanner.
Sa méthode setUp contient :
    • une variable de type string, qui est la chaine booléenne à évaluer
    • une variable de type liste sous la forme d’une liste d’expression lexicale de ce que doit renvoyer la fonction scanner avec la première variable


Les autres méthodes sont, successivement :
    • Une méthode qui test si l’expression qui doit être scannée est bien une chaîne de caractère.
    • Une méthode qui test si la valeur de retour de la fonction est bien une liste
    • La dernière méthode test si, en passant en paramètre à la fonction scanner, la liste de retour est bien égale à la deuxième variable initialisée dans la méthode setUp


Pour exécuter ce fichier test en particulier, on peut tout simplement écrire dans un terminal la ligne suivante :
python3 test_scanner.py -v

L’option -v (verbose) affiche chaque nom de test passé.
Sans cette option, un point ‘.’ est affiché pour chaque test passé.

Pour exécuter tout les tests de tout les fichiers en une seule fois, on peut lancer la commande :
python3 -m unittest -v

L’option -m permet d’appeler un module spécifique, ici unittest.
