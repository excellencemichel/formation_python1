#-*-coding:utf-8-*-



class Fonction:
    def __init__(self):
        pass



    def creer_famille(self, famille):
        self.famille = famille


    def creer_fils(self, fils):
        self.fils = fils
        self.famille += ":{}".format(self.fils)


    def list_fils(self):
        print(self.fils)



    def donner_nom(self, nom):
        self.nom = nom


    def donner_prenom(self, prenom):
        self.prenom = prenom





        
