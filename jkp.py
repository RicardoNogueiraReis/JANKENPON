'''
====================================
JANKENPON (Rock, Paper, Scissors)
====================================

Ricardo Reis 2019
03/03/2019 - 16/03/2019 [DD/MM/YYYY]
Python Version 3.7.0
Version 1.0 JANKENPON
'''
 
from random import randint
user_wins = 0
pc_wins = 0
draw = 0
debug_mode = 0 # lets the user type debug commands, 1 - ON
debug_cmd = ['please debug, alan', 'cycles'] # Commands during debug mode
while True:
    rps = ['rock', 'paper', 'scissors']
    choice = input('Rock, paper or scissors?\n>').lower()

    # Checks if debug mode is ON and if the user is using corresponding commands
    if debug_mode == 1 and choice not in debug_cmd and choice in rps:
        pc = input('PC -- rock, paper or scissors?\n>').lower()
    else:
        pc = rps[randint(0, 2)]
    
    if choice in rps and pc in rps:
        
        print("\n--------------------------------------")
        print("OUTCOME\n--------------------------------------")
        print(f"The computer chose {pc}")
        print("--------------------------------------")
        print(f"The user chose {choice}")
        print("--------------------------------------")

        # DRAW ~
        if choice == pc:
            print(f"[{choice}] = {pc} | ~~DRAW~~")
            draw += 1

        # rock > scissors
        elif choice == rps[0] and pc == rps[2]:
            print(f"[{choice}] > {pc} | «USER WON»")
            user_wins += 1
            
        elif choice == rps[2] and pc == rps[0] :
            print(f"{pc} > [{choice}] | ※USER LOST※")
            pc_wins += 1

        # paper > rock
        elif choice == rps[1] and pc == rps[0]:
            print(f"[{choice}] > {pc} | «USER WON»")
            user_wins += 1
            
        elif choice == rps[0] and pc == rps[1] :
            print(f"{pc} > [{choice}] | ※USER LOST※")
            pc_wins += 1

        # scissors > paper
        elif choice == rps[2] and pc == rps[1]:
            print(f"[{choice}] > {pc} | «USER WON»")
            user_wins += 1
            
        elif choice == rps[1] and pc == rps[2] :
            print(f"{pc} > [{choice}] | ※USER LOST※")
            pc_wins += 1
        
        print("--------------------------------------")

        wins_x = round(user_wins/(user_wins+pc_wins+draw)*100)
        pc_wins_x = round(pc_wins/(user_wins+pc_wins+draw)*100)
        draw_x = round(draw/(user_wins+pc_wins+draw)*100)
        
        print(f"Wins:{user_wins} ({wins_x}%) | Losses: {pc_wins} ({pc_wins_x}%) | Draws: {draw} ({draw_x}%)")

    # Checks if debug mode is being activated
    elif choice == debug_cmd[0]:
        if debug_mode == 0:
            debug_mode = 1
            print("Alright.")
        else:
            debug_mode = 0
            print("Ok.")

    # DEBUG MODE ONLY Checks if user typed "cycles"
    # Checks how many times the computer "chose" what
    
    elif choice == debug_cmd[1] and debug_mode == 1:
        pc_cycles = int(input("How many cycles?\n").lower())
        pc_zero = 0
        pc_one = 0
        pc_two = 0
        for x in range(pc_cycles):
            pc = rps[randint(0, 2)]
            if pc == rps[0]:
                pc_zero += 1
            elif pc == rps[1]:
                pc_one += 1
            elif pc == rps[2]:
                pc_two += 1
        pc_all = pc_zero + pc_one + pc_two
        print(f"rock: {pc_zero} {round((pc_zero/(pc_all))*100)}%\npaper: {pc_one} {round((pc_one/(pc_all))*100)}%\nscissors: {pc_two} {round((pc_two/(pc_all))*100)}%")
    
    elif choice =='quit':
        break

    # If both the user and/or computer
    elif choice not in rps or pc not in rps:
        print("--------------------------------------\nERROR: Choose one the 3 options below:\n--------------------------------------\n")
