#coding:utf-8

"""
    Les opérateur de comparaisons
        == (égale à)
        != (différent de)
        < (strictement inferieur à)
        >(strictement supérieur à)
        <=(inférieur ou égal à)
        >=(supérieur ou égal à )


    Conditions multiples
        and (et)
        or(ou)
        in (dedans)
        not in(pas dedans)
"""

identifiant = "Michel"

mot_passe ="StMichel"

print("Connexion")

user_id = input("Entrez votre identifiant: ")

user_pw = input("Entrez votre mot de passe :")

print("Indentifiant {} pour mdp {}, vous êtes connecté au réseau".format(user_id, user_pw))

if user_pw == mot_passe:
    print("Connexion réussie!")

else:
    print("Vous êtes mal barrés")



if user_id == identifiant and user_pw == mot_passe:
    print("Sa marche alors les deux correspondent")

else:
    print("Les deux ne correspondent pas")