#Le module du réseau
#Coté serveur

import socket #Module pour établir la connecxion entre des machines
import select #Module qui permet à plusieurs clients de ce connecter simultanement


"""
Le module 'socket permet d'établir la connexion entre des machines,
   Le contructeur du module est 'socket':
     Pour une connexion avec le protocole 'TCP' il prend deux parametres
        AF_INET : les adresse , (ici les adresses Internet)
        SOCK_STREAM : le type de sokect, 'SOCK_STREAM pour le protocole TCP
        



"""

#Construction du serveur

#Construction du socket coté serveur

#Construction
connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connexion du socket

connexion_principale.bind(("", 12800))

#Faire écouter le socket sur le port avec le nombre de connexion attendu
connexion_principale.listen(5)

connexion_avec_client, infos_connexion = connexion_principale.accept()


#Serveur en dure forme

hote=""
port = 12777

connect_p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect_p.bind((hote, port))
connect_p.listen(5)
print("Le seurveur écoute à présent sur le port {}".format(port))

"""
client, info_c = connect_p.accept()


Le d'une connexion à la fois
message_recu =b""
while message_recu !="fin":
    message_recu= client.recv(1024)
    #Les accent sont déconseillés
    print(message_recu.decode())
    ms=input("> :")
    ms=ms.encode()
    client.send(ms)
    #client.send(b"5/5")

print("Fermeture de la connexion")
client.close()
connect_p.close()
"""

serveur_lance = True
clients_connectes = [] #Va stocker la liste des clients qui sont conectés
print(clients_connectes)

while serveur_lance:
    #On vérifi que de nouveaux clients ne demande pas à se connecter
    #On va donc écouter la connexion principale 'connect_p' en lecture
    #Le tempts d'attente est de 50ms
    connexions_demandees, wlist, xlist = select.select([connect_p], [],[], 10)

    for connexion in connexions_demandees:
        print(clients_connectes)
        connexion_avec_client, infos_client = connexion.accept()
        clients_connectes.append(connexion_avec_client)
        print(clients_connectes)


    #On peut maintenant écouter la liste des clients connectés
    #les client renvoyé par 'select' sont  les clients qui doivent être lus (recv)
    #On attend là encore 50ms maxi
    #On enferme l'appel à select dans un bloc try
    #Si la liste des client connectés est vide on leve une exception

    client_a_lire = []
    print(client_a_lire)
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes, [],[], 0.05)
    except select.error:
        print("Il y a personne")
    else:
        #On parcours la liste des clients à lire
        #print(client_a_lire)

        for client in clients_a_lire:
            #Le client est de type 'socket'
            message_recu = client.recv(1024)
            #Attention aux accents

            message_recu = message_recu.decode()
            print("Reçu {}".format(message_recu))
            ms_en = input(">: ")
            ms_en = ms_en.encode()
            client.send(ms_en)
            client.send(b"5/5")
            if message_recu == "fin":
                serveur_lance = False
print("Fereture de la connexion")
for client in clients_connectes:
    client.close()

connect_p.close()




