#Réseau
#Coté client

import socket

"""
La construction du client
 La client qui veut se connecter au serveur se créé de la même façcon qu'un
  serveur avec les parametre du constructeur 'socket'


  


"""


#Construction du socket
connexion_avec_serveur=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Connexion du client au serveur
connexion_avec_serveur.connect(("localhost", 12801))


#Client en dure forme
hoste = "localhost"
port= 12777

connect_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connect_s.connect((hoste, port))

print("La connexion établie avec le serveur sur le port {}".format(port))

message_envoye= b""

while message_envoye != b"fin":
    message_envoye = input("> ")
    message_envoye = message_envoye.encode()
    connect_s.send(message_envoye)
    message_recu = connect_s.recv(1024)
    print(message_recu.decode())

print("Fermeture de la connexion")
connect_s.close()






