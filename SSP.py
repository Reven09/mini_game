Madeby=Mohammed Ahmed

import random

Player_win = 0
Cpu_win = 0
tie_score = 0

while True:
    print("Entscheide deine Hand")
    print("1 für Stein")
    print("2 für Schere")
    print("3 für Papier")

    Player_choice = input()
    #nachfrage für eine Valide entscheidung
    pos_choice = ["1", "2", "3"]
    if Player_choice not in pos_choice:
        print("Bitte versuchen sie nochmal")
        continue

    
    if Player_choice == "1":
        Player_choice = "Stein"
    elif Player_choice == "2":
        Player_choice = "Schere"
    else:
        Player_choice = "Papier"

    print("Du hast dich für", Player_choice, "entschieden")



    Cpu_choice = random.choice(["Stein", "Schere", "Papier"])
    print("Computer hat sich für", Cpu_choice, "entschieden")


    ##winner
    if Player_choice == "Stein" and Cpu_choice == "Papier":
        print("Du hast Verloren")
        Cpu_win += 1
    elif Player_choice == "Stein" and Cpu_choice == "Schere":
        print("Du hast Gewonnen")
        Player_win += 1
    elif Player_choice == "Papier" and Cpu_choice == "Schere":
        print("Du hast Verloren")
        Cpu_win += 1
    elif Player_choice == "Papier" and Cpu_choice == "Stein":
        print("Du hast Gewonnen")
        Player_win += 1
    elif Player_choice == "Schere" and Cpu_choice == "Papier":
        print("Du hast Gewonnen")
        Player_win += 1
    elif Player_choice == "Schere" and Cpu_choice == "Stein":
        print("Du hast Verloren")
        Cpu_win += 1
    else:
        print("Unentschieden")
        tie_score += 1
    print("Score")
    print("Du hast", Player_win, "mal Gewonnen")
    print("Du hast", Cpu_win, "mal Verloren")
    print("Du hast", tie_score, "mal Unentschieden")

    ##Noch eine runde?
    play_again = input("Nochmal spielen anworte mit j oder n")
    if play_again.lower() != "j":
        break
print("Du hast", Player_win, "mal Gewonnen")
print("Du hast", Cpu_win, "mal Verloren")
print("Du hast", tie_score, "mal Unentschieden")
print("Danke fürs Spielen") 
