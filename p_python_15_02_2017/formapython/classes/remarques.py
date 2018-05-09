#coding:utf-8


class Personne:
	def __init__(self, nom="Michel", prenom="Excellence"):
		self.nom = nom,
		self.prenom = prenom

		self.parler() #Cela permet de lancer une fonction dès l'instanciation d'un objet de la classe




	def parler(self):
		print("Il parle beaucoup le M en question !")




person1 = Personne() #Cela lancera directement la fonction parler()