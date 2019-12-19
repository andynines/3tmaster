#!/usr/bin/env python3

import tictactoe
import player

game = tictactoe.Game(player.HumanPlayer(), player.AIPlayer(read_save=True))

if __name__ == "__main__":
	game.play()
	game.players[1].freeze()
