# Exercice 1.2
# Ecrire une fonction qui reçoit la note au bac et qui affiche la mention correspondante.
# Par exemple :
#  Note au bac (sur 20) : 13.5
# o Bac avec mention Assez Bien
#  Note au bac (sur 20) : 10.9
# o Bac avec mention Passable
#  Note au bac (sur 20) : 4
# o Recalé


def m_bac():
    note=""
    while note=="":
        note=int(input("Entrez la note obtenue "))
    if note<10:
        print("Recalé")
    elif note==10 & note<13:
        print("Bac avec mention passable")
    elif note==13 & note<14:
        print("Bac avec mention Assez Bien")
    else:
        print("Bac avec mention Execellent")
        return note
m_bac()