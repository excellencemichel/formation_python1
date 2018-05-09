"""
La définition des propriété des attributs en python
"""

class Perso:
    """ Class permettant d'identifier une personne par:
    son nom,
    son prenom,
    son age
    son lieu de residence
    """

    def __init__(self, nom,prenom):
        """ Constructeur de la classe
        """
        self.nom=nom
        self.prenom =prenom
        self.age = 22
        self._rsi ="N'Zaly"

    """ Ici sont définis l'accesseur et le mutateur de l'attribut _rsi
    """

    #Accesseur
    def _get_rsi(self):
        """Methode qui sera appelée quand on souhate accéder à l'attribut
        '_rsi' c'est l'accesseur' cette méthode n'a pas besion d'un paramtre
        puisqu'il ne returne l'attribut qu'on veut acceder
        """
        print("On veut acceder à l'attribut '_rsi'")
        return self._rsi #C'est qu'on retourne l'att

    #Mutateur
    def _set_rsi(self,n_rsi):
        """Méthode qui sera appeler quand on souhaite modifier la valeur de l'att
        '_rsi' c'est donc la méth qu'on appelle 'mutateur', elle prend en parametre
        le nouvel objet qu'on donnera à l'att comme nouvelle valeur
        """
        print("Attention veut modifier l'att '{}', donc {} demenage à {}".format(self._rsi,self.prenom,n_rsi))
        self._rsi =n_rsi

    def _del_rsi(self):
        print("Attention cette action supprimera l'attribut {}".format(self._rsi))
        del self._rsi
    rsi = property(_get_rsi,_set_rsi,_del_rsi)

