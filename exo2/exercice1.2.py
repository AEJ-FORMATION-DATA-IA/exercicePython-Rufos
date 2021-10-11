# Ecrire une fonction qui reçoit un paramètre N et qui nous retourne la liste des nombres 
# impairs compris en 0 et N.
# Exemple : pour N = 10 la fonction nous retourne [1, 3, 5,7,9]
# Indication : utiliser la boucle while
liste_impaire=[]
def nombre_impaire(i):
    while(i>1):
        i-=1
        if(i%2==1):
            liste_impaire.append (print(i))
nombre_impaire(5)