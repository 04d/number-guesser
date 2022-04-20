import random
import os
import time
not_good_number = []



choice_number_1 = int(input("Veuillez entrer le premier nombre qui sera le nombre de départ : "))
choice_number_2 = int(input("Veuillez entrer le deuxième nombre qui sera le nombre de d'arrivé : "))
random_number = random.randint(choice_number_1, choice_number_2)

def number_check():
    choice_random = int(input(f"Essayer de trouver le nombre, il est entre {choice_number_1} et {choice_number_2} : "))
    if choice_random == random_number:
        print(f"Bien-Joué vous avez trouvé, c'était bien {random_number} !")
        time.sleep(5)
        exit()
    elif choice_random != random_number:
        os.system('cls||clear')
        print(f"Ce n'est pas {choice_random}")
        if choice_random not in not_good_number:
            if choice_random >= choice_number_1 and choice_random <= choice_number_2: 
                not_good_number.append(choice_random)
                not_good_number.sort()
            elif choice_random <= choice_number_1:
                print(f"{choice_random} est en dessous de {choice_number_1}")
            elif choice_random >= choice_number_1:
                print(f"{choice_random} est au dessus de {choice_number_2}")
        print(f"Voici la liste des nombres qui sont faux : {not_good_number} ")
        number_check()

number_check()
