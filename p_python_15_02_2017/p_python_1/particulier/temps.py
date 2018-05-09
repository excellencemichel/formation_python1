#Le temps
import time # module pour controle du temps
import datetime # pour le contrôle 
"""
Le module 'time' sert tà gérer le temps
Avec les différentes fonctions on a:
  'time()' : donne le temps de 1970 à la date actuelle
  'localtime()' : renvoie la date actuelle
     -la date renvoyer par 'localtime() est un objet qui a les éléments suivants
       tm_year : année
       tm_mon : numéro du mois (1 à 12)
       tm_mday : numéro du jour du mois (1 à 31)
       
       tm_hour : heure du jour (0 à 23)
       tm_min : nombre de minutes (0 à 59)
       tm_sec : nombre de seconde

       tm_wday : numéro du jour de la semaine(0 à 6, lundi=0)
       tm_yday: numéro du jour de l'année (1 à 366)
       tm_isdst : nombre de changement d'heure en local par rapport au GMT

    -On peut recupérer le timestamp dans le resultat renvoyer par 'localtime()'
    avec la 'mktime' si on stoke le reultat de localtime dans une varible pour
    lui appliquer la fonction

___________________________
On peut également utiliser le méthode 'sleep()' du module 'time' pour mettre
en pause l'exécution d'un programme en passant en parametre de la méthode le
temps désiré pour mettre en pause l'exécusion du programme

________________
Pour formater la date pour qu'elle s'affiche de la façon dont nous
souhaitons on utilise la fonctio 'strftime' ,
cette fonction  prend en parametre :
  -la chaine de formatade 
  -le temps qu'on  cherche à formater, si ce parametre n'est pas donné, python
    prend par défaut la date et l'heure actuelle

  Voici les #tes forme de chaine de formatage :
  %A : Nom du jour
  %B : Nom du mois
  %d : jour du mois
  %H : Heure (de 00 à 23)
  %M : Minute (entre 00 et 59)
  %S :Seconde (entre 00 et 59)
  %Y : Année

 Pour afficher tout le temps on peut faire :
 %A %B %d %H %M %S %Y

 A noter toute autre lettre après ces caractères figureront dans les resultats


 ________________________
 Pour plus de précision de dans le controle du temps et de la date, le module
 'datetime' propose des classes pouvant permettre une precision dans la
 recherche du temps
 Comme :
   -la classe 'date' qui ne s'occupe que de la date
     le constructeur de la classe 'date' prend dans l'odre :
       -la date,
       -le mois,
       -le jour
    cette classe a des méthodee permettant d'aboutir à des choses concrètes
     On a :
      -today() : pour la date d'aujourd'hui
      -fromtimestamp() : date provenant d'un temps qu'on lui passe en parametre

    -la classe 'time' permet le controle des heures indéppendemment des dates
      Le constructeur de la classe 'time' prend les parametre optionnels
        hour : heure
        minute : minute
        second : seconde
        microsecond : microseconde
        tzinfo : information du fuseau horraire
        
      Tous ces ont pour valeur zéro (0) par défaut,
       donc si rien n'est à la classe 'time' à son instanciation elle envoi
          00 : heure
          00 : minute
          00: seconde
          00: microseconde
          None: Fuseau horaire

Pour représenter à la fois la date et l'heure avec le module 'datetime' on
utilise la classe 'datetime' du même module 'datetime'

  Puisque cette classe fait le travail de datetime.date et celui de datetime.time
  son constructeur prend donc :
    -Tous les 2 parametres de datetime.date :
        date
        mois
        jour
    -Tous les 5 paramètre optionels de datetime.time :
    hour :heure
    minute :minute
    second : seconde
    microsecond : microsecond
    tzinfo :fuseau horraire


 Cette classe 'datetime' possèede les méthode:
     now() : pour connaître la date d'aujourd'hui
     formtimestamp(param) : Formater une date et une heure  
 




"""

maintenant = time.time() #Contient la date de 1970 à maintenant
print(maintenant)

time.sleep(1) # on prend un petit repos pour qu'il est un peu de temps entre
             #les deux appels à time() , vu que Dieu merci la machine est
             #ça s'exécute rapidement
#d'ailleurs pratiquement 1secondes

apres = time.time() #Contient la date de 1970 à après
print(apres)

print(apres > maintenant) #Doit donner True car apres est superieur à maintenant

entre= apres - maintenant # stocks le temps écoulé entre l'appel à time() au
                       #niveau de 'maintenant' jusqu'à son appel au niveau de apres
print(entre)



#Essay de la méthode sleep du module time

def voir(pa):
    if pa==5:
        time.sleep(12) #On demande si condition est vérifiée on prend un repos de 12 seconde
        print("Un bon repos c'est normal")

    print("Pas de repos cette fois ci")


#Utilisation du formatage du temps

print(time.strftime("%AA le %d %B l'an %Y à %Hh: %Mmn : %Ss")) #Pour le contrôle de tous
                        #fortage possible du temps, pour besion on peut choisir
                        #ce qu'on a besion de dans


#__________________________________
#Utilisation du module datetime

print(datetime.date(2011,8,31)) #Affiche la date qu'on lui a fourni

print(datetime.date.today())#Affiche la date d'aujourd'hui
    
actu = time.time()
print(datetime.date.fromtimestamp(actu)) #Permet d'utiliser les deux modules

#La classe 'time' du module 'datetime' sert à contrôler les l'heure independemment de la date
heure = int(time.strftime("%H")) #Capte l'heure actuelle
minute = int(time.strftime("%M")) #Capte la minute actuelle
seconde=int(time.strftime("%S")) #Capte la seconde actuelle

r_date =datetime.time(heure, minute, seconde) #On passe heures récupérées par la
                                    #du module 'time' à la classe 'time' du
                                   #du module 'datetime' pour un meilleur contrôle
                                #des dates
print(r_date)

print(datetime.time(12,33,40)) #Affiche les date passées entre parametres

print(datetime.time()) #Doit donner 00:00:00


#_______________________________
#Utilisatio de la classe 'datetime' du module 'datetime'

print(datetime.datetime.now()) #Affiche complètement la date actuelle avec 3 pa
                   #metre de date et les 4 1er parametre de time
date_heure_f =time.time() # Un timestamp

print("Il est exactement ",datetime.datetime.fromtimestamp(date_heure_f))

print(datetime.datetime(2011,8,31)) #Le constructeur de la class prend
#obligatoirement les parametres de 'datetime.date' si les parametre optionnels
#de 'datetime.tme' ne sont pas passés il sont remplacés par zéro (0) valeur par
#défaut

