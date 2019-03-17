# JanKenPon

> Ricardo Reis
> 
> 3 March 2019
> 
> Python 3.7.0

Simple rock, paper, scissors game using python's random module to output the opponent's choice. 

Commands
----------

1.Start the script:

    python jkp.py

2.Choose either rock, paper or scissors:

    Rock, paper or scissors?
	>Rock
Output (If the computer randomly chooses scissors):

	--------------------------------------
	OUTCOME
	--------------------------------------
	The computer chose scissors
	--------------------------------------
	The user chose rock
	--------------------------------------
	[rock] > scissors | «USER WON»
	--------------------------------------
	Wins:1 (100%) | Losses: 0 (0%) | Draws: 0 (0%)
	
Debug commands
----------
Commands used to test this script

1.Activate/deactivate debug mode:

	>please debug, alan
It will output a confirmation message when debug mode is active:
	
	Rock, paper or scissors?
	>please debug, alan
	Alright

2.After the user has made their choice, the script now asks the user to input the computer's choice:

	Rock, paper or scissors?
	>rock
Output:

	PC -- rock, paper or scissors?
	>
3.Besides this, during debug mode, the user can input how many cycles they want to, to show a counter on how many times the computer chose a particular choice:

	Rock, paper or scissors?
	>Cycles
Output:

	How many cycles?
	>90
	rock: 33 37%
	paper: 28 31%
	scissors: 29 32%

What I've learned
----------

- Lists in python
- The "Random" Python module