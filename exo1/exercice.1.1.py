# Exercice 1.1
# Ecrire une fonction qui calcule l'indice de masse corporelle (IMC) d'un adulte et qui en donne 
# l'interprétation (corpulence normale, surpoids...).
# Par exemple :
#  Votre taille en cm = 170
#  Votre masse en kg = 68.5
#  IMC = 23.70 kg/m²
#  Interprétation : corpulence normale


def indice_de_masse_corporelle(taille,masse):
   
    IMC=masse/taille**2
    if(IMC>=20):
        print("Votre IMC est : ",IMC," kg/m² vous avez une corpulence normale \n Prenez soins de votre corps")
    elif(IMC>=35) :
         print("Votre IMC est : ",IMC," kg/m² vous avez une corpulence anormale, vous etes en surpoids \n Prenez soins de votre corps")

    else:
        print("Votre IMC est : ",IMC," kg/m² vous avez une corpulence anormale, vous etes chétif \n Prenez soins de votre corps")
        
indice_de_masse_corporelle(1.7, 68.5)