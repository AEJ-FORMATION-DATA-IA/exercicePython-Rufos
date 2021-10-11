# Définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
# 1. triez et affichez la liste ; 
# 2. ajoutez l’élément 12 à la liste et affichez la liste ; 
# 3. renversez et affichez la liste ; 
# 4. affichez le nombre d’éléments de la liste ; 
# 5. supprimez l’élément 38 et affichez la liste ; 
# 6. affichez la sous-liste du 2e
# au 3e
# élément ; 
# 7. affichez la sous-liste du début au 2e
# élément ; 
# 8. affichez la sous-liste du 3e
# élément à la fin de la liste ; 
   
    
liste =[17, 38, 10, 25, 72]
#1
liste.sort()
liste

# 2. ajoutez l’élément 12 à la liste et affichez la liste ; 
liste.append(12)
liste
#mon tableau maintenant est : [10, 17, 25, 38, 72, 12]
# 3. renversez et affichez la liste ;
liste.reverse()
liste

#mon tableau maintenant est : [12, 72, 38, 25, 17, 10]

# 4. affichez le nombre d’éléments de la liste ;
len(liste)
# 5. supprimez l’élément 38 et affichez la liste ; 
liste.remove(38)
liste

#mon tableau maintenant est : [12, 72, 25, 17, 10]

# 6. affichez la sous-liste du 2e au 3e element
liste[1:3]

# 8. affichez la sous-liste du 3e
# élément à la fin de la liste ;

liste[2:]