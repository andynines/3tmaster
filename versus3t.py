#!/usr/bin/env python3
"""
versus3t.py
play a round against the current bot; it learns from these games as well
"""

import random

import tictactoe
import player

ai_player = player.AI(read_save=True)

if random.randint(0, 1):
	print("Go first")
	game = tictactoe.Game(player.Human(), ai_player)
else:
	print("Go second")
	game = tictactoe.Game(ai_player, player.Human())

if __name__ == "__main__":
	game.play()
	ai_player.freeze()
