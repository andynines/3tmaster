"""
tictactoe.py
Tic-tac-toe game engine
"""

import collections

class BoardStr(str):

	def __str__(self):
		# render board as 3x3 grid for terminal output
		return '\n'.join([self[:3], self[3:6], self[6:9]])

class Game:

	default_space = '-'
	player_syms = ('X', 'O')
	gamestate = collections.namedtuple("GameState", ["board", "options"]) # passed to players for decision making
	
	def __init__(self, player1, player2):
		self.players = (player1, player2)

	def reset(self):
		self.pn = 0
		self.board = BoardStr(Game.default_space * 9)

	def get_availpos(self):
		# return list of string indexes of all empty spaces
		avail = []
		for i, c in enumerate(self.board):
			if c == Game.default_space:
				avail.append(i)
		return avail

	def has_winner(self, mvpos, psym):
		# check for wins based on most recent spot a symbol was placed
		return (
			all([self.board[i]==psym for i in range(mvpos//3*3, 3*(mvpos//3 + 1))]) or # check relevant row
			all([self.board[i]==psym for i in range(mvpos%3, (mvpos%3)+9, 3)]) or # check relevant column
			all([self.board[i]==psym for i in [0, 4, 8]]) or # check diagonal
			all([self.board[i]==psym for i in [2, 4, 6]]) # check anti-diagonal
		)
		
	def play(self):
		self.reset()
		mvpos = 0
		while True:
			gs = Game.gamestate(self.board, self.get_availpos())
			if self.has_winner(mvpos, Game.player_syms[not self.pn]): # win check
				self.players[not self.pn].on_win(gs)
				self.players[self.pn].on_lose(gs)
				break
			elif len(gs.options) == 0: # draw check
				self.players[0].on_draw(gs)
				self.players[1].on_draw(gs)
				break
			mvpos = self.players[self.pn].get_mvpos(gs)
			self.board = BoardStr( # modify board string with new move
				self.board[:mvpos] + Game.player_syms[self.pn] + (self.board[mvpos+1:] if mvpos < 8 else "")
			)
			self.pn = not self.pn
