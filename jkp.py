# ================================= #
# JANKENPON (Rock, Paper, Scissors) #
# ================================= #

from random import randint

# Ricardo Nogueira Reis
# 03/03/2019 - 16/03/2019 [DD/MM/YYYY]
# Python Version 3.7.0 (also tested on 3.8.2)
# Version 1.1.0 - 16/07/2021

user_wins = cpu_wins = draw = 0

rps = ['rock', 'paper', 'scissors']
debug_mode = False  # lets the user type debug commands
debug_cmd = ['pls debug', 'cycles']  # Commands during debug mode

choice = ""

while choice != "quit":

    choice = ""
    cpu_choice = "-1"

    # User choice
    while choice != "quit" and choice not in rps:
        choice = input('Rock, paper or scissors?\n>').lower().strip()

        # Enable debug mode by toggle
        if choice == debug_cmd[0]:
            debug_mode = not debug_mode

        elif choice == debug_cmd[1]:
            break

        # Check error
        elif choice != "quit" and choice not in rps and choice != debug_cmd[0] and choice != "quit":
            print("Error: Choose one of the three choices displayed! ")

    if choice == "quit":
        continue

    # CPU choice if debug mode is True
    if not debug_mode:
        cpu_choice = rps[randint(0, 2)]
    elif choice == debug_cmd[1] and debug_mode:
        cycles = -1
        while int(cycles) <= 0:
            try:
                cycles = int(input("How many cycles?\n").strip())

                pc_zero = pc_one = pc_two = 0

                for x in range(cycles):
                    cpu_choice = rps[randint(0, 2)]
                    if cpu_choice == rps[0]:
                        pc_zero += 1
                    elif cpu_choice == rps[1]:
                        pc_one += 1
                    elif cpu_choice == rps[2]:
                        pc_two += 1
                pc_all = pc_zero + pc_one + pc_two
                print(f"rock: {pc_zero} {round((pc_zero/pc_all)*100)}%\n"
                      f"paper: {pc_one} {round((pc_one/pc_all)*100)}%\n"
                      f"scissors: {pc_two} {round((pc_two/pc_all)*100)}%")

            except TypeError:
                print("Error: Number of cycles must be above 0!")
            except ValueError:
                print("Error: Number of cycles must be a NUMBER above 0!")
    else:
        while cpu_choice not in rps:
            cpu_choice = input('CPU -- Rock, paper or scissors?\n>').lower().strip()

            if cpu_choice not in rps:
                print("Error: Choose one of the three choices displayed!")

    if choice == "cycles":
        continue

    print("\n======================================")
    print("               OUTCOME")
    print("--------------------------------------")
    print(f"The computer chose {cpu_choice}")
    print("--------------------------------------")
    print(f"The user chose {choice}")
    print("--------------------------------------")

    # Instead of checking the player's choice and the CPU's individually, the winner is determined by using...
    # the index in rps list so it can check who got the highest index number,
    # where <Rock> is 0 and <Paper> is 1 and so on. Paper (index = 1) beats Rock (index = 0) because 0 < 1
    player_index = rps.index(choice)
    cpu_index = rps.index(cpu_choice)

    # Since <Rock>(0) beats <Scissors>(2) and the index number is used to determined the winner, whoever played rock
    # has their own index number moved to 3 so the highest number wins
    if player_index == 0 and cpu_index == 2:
        player_index = 3
    elif player_index == 2 and cpu_index == 0:
        cpu_index = 3

    if player_index == cpu_index:
        print(f"[{choice}] = {cpu_choice} | ~~DRAW~~")
        draw += 1
    elif player_index > cpu_index:
        print(f"[{choice}] > {cpu_choice} | << USER WON >>")
        user_wins += 1
    elif player_index < cpu_index:
        print(f"[{choice}] < {cpu_choice}  | xX USER LOST Xx")
        cpu_wins += 1

    print("======================================")

    try:
        wins_x = round(user_wins / (user_wins + cpu_wins + draw) * 100)
    except ZeroDivisionError:
        wins_x = 0

    try:
        pc_wins_x = round(cpu_wins / (user_wins + cpu_wins + draw) * 100)
    except ZeroDivisionError:
        pc_wins_x = 0

    try:
        draw_x = round(draw / (user_wins + cpu_wins + draw) * 100)
    except ZeroDivisionError:
        draw_x = 0

    print(f"Wins:{user_wins} ({wins_x}%) | "
          f"Losses: {cpu_wins} ({pc_wins_x}%) | "
          f"Draws: {draw} ({draw_x}%)")
