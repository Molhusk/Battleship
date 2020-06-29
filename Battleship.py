import os
from donnees import *
from fonction import *

os.chdir(os.getcwd())
#os.chdir('C:/Users/jason/Desktop/Python/BattleShip')



caseOk = False

#définition du bateau à placer
choixBateau = input('Quel Bateau Voulez vous placer ? (Tapez le chiffre associé): \n\
1)Porte-Avion (5 cases)\n\
2)Croiseur (4 cases)\n\
3)Sous-Marin (3 cases)\n\
4)Eclaireur (3 cases)\n\
5)Torpilleur (2 cases)\n')

print('Vous avez choisi de placer {}'.format(nomFlotte[choixBateau]))

choisi = nomFlotte[choixBateau] 

for key, value in flotte.items():
    if choisi == key:
        print('Le bateau mesure {} cases'.format(value))
        tailleBateau = value

#définition du choix de la premiere case
while caseOk == False:
    choixCase = input('Veuillez entrer une case sous la forme Lettre Chiffre\n')

    try :
        len(choixCase) <= 3
    except :
        print('Vous ne pouvez pas entrer autant de caractères. Merci de réessayer')
        continue
    choixCase = choixCase.lower()

    if " " in choixCase:
        caseSplit = choixCase.split(' ')
        choixCase = caseSplit[0] + caseSplit[1]

    if choixCase[0].isalpha() != True:
        raise ValueError('La case doit être entrée sous la forme Lettre Numero par expl : A1')
    try :
        int(choixCase[1])
    except :
        print('La case doit être entrée sous la forme Lettre Numero par expl : A1')
        continue
    # tester que les valeurs fassent bien partie de l'intervalle A-J/1-10
    indice = alphabet[choixCase[0]]
    if indice  not in alphabet.values():
        raise KeyError('La lettre ne fait pas partie du jeu !')
    caseOk = True

Lettre = choixCase[0]
Nombre = choixCase[1]

tab = suggestion(Lettre, Nombre)

bateau1 = bateau(tailleBateau, tab, choixCase)
#accés aux coordonnées de l'objet via NomBateau.coordonnees
            
    
    
    
