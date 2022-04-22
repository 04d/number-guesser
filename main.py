import random
import os
import time
not_good_number = []


# replay function, qui vous demandera si vous voulez rejouer une fois que vous aurez trouvé le nombre.
def replay_game(): 
    yes_or_no = str(input("Voulez vous rejouer ? [ Y / N ]: "))
    if yes_or_no == "y" or "Y" in yes_or_no: # vérifie si le input de la [LIGNE 25] contient y, ou Y.
        not_good_number.clear()
        os.system('cls||clear')
        menu_number()
    elif yes_or_no == "n" or "N" in yes_or_no: # vérifie si le input de la [LIGNE 25] contient n, ou Y.
        exit()
    else: 
        replay_game()


# la fonction menu_number, c'est ici que vous allez choisir vos deux nombres.
def menu_number():
    global choice_number_1
    global choice_number_2
    global random_number
    choice_number_1 = int(input("Veuillez entrer le premier nombre qui sera le nombre de départ : "))
    choice_number_2 = int(input("Veuillez entrer le deuxième nombre qui sera le nombre de d'arrivé : "))
    if choice_number_2 <= choice_number_1: # vérifie que le second nombre est supérieur au premier.
        os.system('cls||clear')
        print("Vérifiez bien que votre second nombre est supérieur au premier !")
        menu_number()
    else:
        random_number = random.randint(choice_number_1, choice_number_2)
        number_check()

# la fonction number_check, cette fonction sert à checker les égaliters des nombres.
def number_check():
    choice_random = int(input(f"Essayer de trouver le nombre, il est entre {choice_number_1} et {choice_number_2} : "))
    if choice_random == random_number: # si le nombre que vous avez écrit [LIGNEZ 39] est égal au nombre aléatoire.
        print(f"Bien-Joué vous avez trouvé, c'était bien {random_number} !")
        time.sleep(5)
        replay_game() 
    elif choice_random != random_number: # si le nombre que vous écrivez n'est pas égal au nombre aléatoire.
        os.system('cls||clear')
        print(f"Ce n'est pas {choice_random}")
        if choice_random not in not_good_number: # vérifier si le nombre que vous avez écrit [LIGNE 39] n'est pas dans la liste, pour ne pas mettre deux fois le même nombre dans la liste.
            if choice_random >= choice_number_1 and choice_random <= choice_number_2: # vérifie si le nombre que vous entrez [LIGNE 39] est plus petit que le premier nombre et plus grand que le deuxième.
                not_good_number.append(choice_random) # ajoute les nombres qui ne sont pas le nombre aléatoire dans la liste.
                not_good_number.sort() # range les nombres de la liste de façon croissante.
            elif choice_random <= choice_number_1: # vérifie si le nombre que vous avez entré [LIGNE 39] est plus petit que le premier nombre que vous avez entré [LIGNE 25].
                print(f"{choice_random} est en dessous de {choice_number_1}")
            elif choice_random >= choice_number_2: # vérifie si le nombre que vous avez entré [LIGNE 39] est plus grand que le deuxième nombre que vous avez entré [LIGNE 26].
                print(f"{choice_random} est au dessus de {choice_number_2}")
        print(f"Voici la liste des nombres qui sont faux : {not_good_number} ")
        number_check()

menu_number() # c'est cette fonction qui va faire marcher toutes les autres, sans cette ligne le code ne marchera pas.
