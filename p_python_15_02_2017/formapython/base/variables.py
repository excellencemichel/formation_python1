#coding:utf-8



"""
Nommage des variable :
    doit imperativement commencer par une lettre ou un underscore(_)
    ne pas contenir de caractères spéciaux comme des accents
    peut quand-même contenir des underscores


Type standards
    entier numerique (int)
    nombre à virgule ou flottant (float)
    chaine de caractère (str)
    boolean (bool)

"""


agePersonne = 22 #Type int
prixHT = 12.3 # Type float

solution1 = "Une chaine de caractère" # str
solution2 = "400" # str

continuer_partie = True # bool

# hexadecimal = 03c89fa # les hexadecimal ne sont pas gérés par defaut

print(type(agePersonne))
print(type(prixHT))
print(type(solution1))
print(type(solution2))
print(type(continuer_partie))


print("La liquidité varie entre {} et {}, du coup on peut alors faire au prix de {} € ".format(agePersonne, agePersonne+2, prixHT) )


"""
La fonction qui permet de faire saisir à l'utuilisateur
'input'

Cette fonction renvoi ce qui a été saisi
donc pour recupérer ce qui a été saisi il faut la stocker dans
une variable
"""

input("Saisissez votre nom : ")
"""
    Ici après la saisie rien ne passe parce que justement
    on a pas stocké la réponse dans une variable
"""

votreNom = input("Saisissez votre nom : ")

print("Ahh d'accord votre nom est {} ! Je prend bonne note".format(votreNom))


"""
    Transformation des variable
        cela se fait tout simplement utilisant les type de variable
"""


prixHT = input("Entrez le prix hors taxe M {} :".format(votreNom))

prixHT = int(prixHT) #Transformation du type str que input envoi en nombre
                     #Mais cela n'est possible si les donnée sont des chiffres

prixTTC = prixHT + (prixHT * 20 / 100)

print("Donc le prix TTC est alors {}".format(prixTTC))
