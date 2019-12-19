#!/usr/bin/env python3
"""
train3t.py
train the current bot; pass a number of training rounds on the command line
"""

import sys

import player
import tictactoe

trainer = player.Dullard()
champion = player.AI(read_save=True)

game_turn1 = tictactoe.Game(champion, trainer)
game_turn2 = tictactoe.Game(trainer, champion)

if __name__ == "__main__":
	for _ in range(int(sys.argv[1])):
		# every round, play a game as X and a game as O
		game_turn1.play()
		game_turn2.play()
	total_games = champion.wins + trainer.wins + trainer.draws
	print("Victory rate: %.2f%%" % (champion.wins / total_games * 100))
	print("Draw rate: %.2f%%" % (champion.draws / total_games * 100))
	champion.freeze()
