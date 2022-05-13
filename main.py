import random
import os
import time
not_good_number = []


def replay_game(): 
    yes_or_no = str(input("Voulez vous rejouer ? [ Y / N ]: "))
    if yes_or_no.lower() == "y":
        not_good_number.clear()
        os.system('cls||clear')
        menu_number()
    elif yes_or_no.lower() == "n":
        
        exit()
    else: 
        replay_game()


def menu_number():
    global choice_number_1
    global choice_number_2
    global random_number
    choice_number_1 = int(input("Veuillez entrer le premier nombre qui sera le nombre de départ : "))
    choice_number_2 = int(input("Veuillez entrer le deuxième nombre qui sera le nombre de d'arrivé : "))
    if choice_number_2 <= choice_number_1: 
        os.system('cls||clear')
        print("Vérifiez bien que votre second nombre est supérieur au premier !")
        menu_number()
    else:
        random_number = random.randint(choice_number_1, choice_number_2)
        number_check()


def number_check():
    choice_random = int(input(f"Essayer de trouver le nombre, il est entre {choice_number_1} et {choice_number_2} : "))
    if choice_random == random_number: 
        print(f"Bien-Joué vous avez trouvé, c'était bien {random_number} !")
        time.sleep(5)
        replay_game() 
    elif choice_random != random_number: 
        os.system('cls||clear')
        print(f"Ce n'est pas {choice_random}")
        if choice_random not in not_good_number: 
            if choice_random >= choice_number_1 and choice_random <= choice_number_2: 
                not_good_number.append(choice_random) 
                not_good_number.sort()
            if choice_random < random_number:
                print("C'est plus haut !")
            elif choice_random > random_number:
                print("C'est plus bas !")
            elif choice_random <= choice_number_1: 
                print(f"{choice_random} est en dessous de {choice_number_1}")
            elif choice_random >= choice_number_2: 
                print(f"{choice_random} est au dessus de {choice_number_2}")
        print(f"Voici la liste des nombres qui sont faux : {not_good_number} ")
        number_check()

menu_number()
