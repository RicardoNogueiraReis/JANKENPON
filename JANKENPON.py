'''
,---.     |    o                    
|---',---.|__/ .,-.-.,---.,---..   .
|    |   ||  \ || | |,---||    |   |
`    `---'`   ``` ' '`---^`    `---'
====================================
JANKENPON (Pedra, papel, tesoura)
====================================

Ricardo Reis 2019
03/03/2019 - 16/03/2019 [DD/MM/YYYY]
Versão Python 3.7.0
Versão 1.0 JANKENPON
'''

from random import randint
user_wins = 0
pc_wins = 0
empate = 0
debug_mode = 0 # permite usar comandos para debug, 1 - ativado
debug_cmd = ['please debug, alan', 'cycle'] # comandos durante o debug
while True:
    ppt = ['pedra', 'papel', 'tesoura']
    escolha = input('Pedra, papel ou tesoura?\n>').lower()

    # verifica se o modo debug está ativado e se o utilizador está a usar comandos de debug
    if debug_mode == 1 and escolha not in debug_cmd:
        pc = input('PC -- Pedra, papel ou tesoura?\n>').lower()
    else:
        pc = ppt[randint(0, 2)]
    
    if escolha in ppt:
        
        print("\n--------------------------------------")
        print("RESULTADO\n--------------------------------------")
        print(f"Ao computador calhou {pc}")
        print("--------------------------------------")
        print(f"O utlizador escolheu {escolha}")
        print("--------------------------------------")

        # EMPATOU ~
        if escolha == pc:
            print(f"[{escolha}] = {pc} | ~~UTLIZADOR EMPATOU~~")
            empate += 1

        # PEDRA > TESOURA
        elif escolha == ppt[0] and pc == ppt[2]:
            print(f"[{escolha}] > {pc} | «UTLIZADOR GANHOU»")
            user_wins += 1
            
        elif escolha == ppt[2] and pc == ppt[0] :
            print(f"{pc} > [{escolha}] | ※UTLIZADOR PERDEU※")
            pc_wins += 1

        # PAPEL > PEDRA
        elif escolha == ppt[1] and pc == ppt[0]:
            print(f"[{escolha}] > {pc} | «UTLIZADOR GANHOU»")
            user_wins += 1
            
        elif escolha == ppt[0] and pc == ppt[1] :
            print(f"{pc} > [{escolha}] | ※UTLIZADOR PERDEU※")
            pc_wins += 1

        # TESOURA > PAPEL
        elif escolha == ppt[2] and pc == ppt[1]:
            print(f"[{escolha}] > {pc} | «UTLIZADOR GANHOU»")
            user_wins += 1
            
        elif escolha == ppt[1] and pc == ppt[2] :
            print(f"{pc} > [{escolha}] | ※UTLIZADOR PERDEU※")
            pc_wins += 1
        
        print("--------------------------------------")

        wins_x = round(user_wins/(user_wins+pc_wins+empate)*100)
        pc_wins_x = round(pc_wins/(user_wins+pc_wins+empate)*100)
        empate_x = round(empate/(user_wins+pc_wins+empate)*100)
        
        print(f"Vitórias:{user_wins} ({wins_x}%) | Derrotas: {pc_wins} ({pc_wins_x}%) | Empates: {empate} ({empate_x}%)")

    elif escolha == debug_cmd[0]:
        if debug_mode == 0:
            debug_mode = 1
            print("Alright.")
        else:
            debug_mode = 0
            print("Ok.")
    elif escolha == debug_cmd[1] and debug_mode == 1:
        pc_cycles = int(input("How many cycles?\n").lower())
        pc_zero = 0
        pc_one = 0
        pc_two = 0
        for x in range(pc_cycles):
            pc = ppt[randint(0, 2)]
            if pc == ppt[0]:
                pc_zero += 1
            elif pc == ppt[1]:
                pc_one += 1
            elif pc == ppt[2]:
                pc_two += 1
        pc_all = pc_zero + pc_one + pc_two
        print(f"Pedra: {pc_zero} {round((pc_zero/(pc_all))*100)}%\nPapel: {pc_one} {round((pc_one/(pc_all))*100)}%\nTesoura: {pc_two} {round((pc_two/(pc_all))*100)}%")
        
    elif escolha not in ppt:
        print("--------------------------------------\nERRO: Escolha uma das 3 opções abaixo:\n--------------------------------------\n")
