import os
from donnees import *

os.chdir(os.getcwd())
class bateau :
    def __init__(self,taille, tabSuggestions, premiereCase):
        premiereCase = tuple(premiereCase)
        self.coordonnees = [premiereCase]
        monCul = 1 # Une case est deja donnée par l'utilisateur
        while monCul != taille:
            i = 1
            msg = str()
            for element in tabSuggestions :
                msg += '{}) {}\n'.format(i, element)
                i += 1
            choix = input(msg)
            choix = int(choix)
            NouvelleCase = tabSuggestions[choix-1]
            self.coordonnees.append(NouvelleCase)
            print('Jusqu\'a present vos cases sont : {}'.format(self.coordonnees))
            tabSuggestions = suggestion(NouvelleCase[0],NouvelleCase[1])
            monCul += 1
        def __repr__(self):
            msg = 'Votre bateau est aux coodonnées :\n'
            for element in self.coordonnees:
                msg+='{},\n'.format(element)
            return '{}'.format(msg)
                
    
def suggestion(lettre, nbr):
    suggestions = []
    nbr = int(nbr)
    indice = alphabet[lettre]
    if indice == 1:
        for key, value in alphabet.items():
            if value == indice +1:
                tup = [key, nbr]
                tup = tuple(tup)
                suggestions.append(tup) # Le tuple contient la lettre str et le nombre int. Ils sont envoyés dans les suggestions ! (pour C2 la def renvoie B2/D2)
    elif indice > 1 and indice < 10:
        for key, value in alphabet.items():
            if value == indice -1:
                tup = [key, nbr]
                tup = tuple(tup)
                suggestions.append(tup)
            elif value == indice +1:
                tup = [key,nbr]
                tup = tuple(tup)
                suggestions.append(tup)
    elif indice == 10:
        for key, value in alphabet.items():
            if value == indice -1:
                tup = [key, nbr]
                tup = tuple(tup)
                suggestions.append(tup)

    if nbr == 1:
        nbr += 1
        tup = [lettre, nbr]
        tup = tuple(tup)
        nbr -= 1
        suggestions.append(tup)
        
    elif nbr > 1 and nbr < 10:
        nbr += 1
        tup = [lettre, nbr]
        tup = tuple(tup)
        nbr -= 1
        suggestions.append(tup)
        tup = []
        nbr -= 1
        tup = [lettre, nbr]
        tup = tuple(tup)
        nbr +=1
        suggestions.append(tup)
    elif nbr == 10:
        nbr -= 1
        tup = [lettre, nbr]
        tup = tuple(tup)
        nbr +=1
        suggestions.append(tup)
    return suggestions
        
        
