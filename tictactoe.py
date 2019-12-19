
import collections

class BoardStr(str):

	def __str__(self):
		return '\n'.join([self[:3], self[3:6], self[6:9]])

class Game:

	default_space = '-'
	player_syms = ('X', 'O')
	gamestate = collections.namedtuple("GameState", ["board", "options"])
	
	def __init__(self, player1, player2):
		self.players = (player1, player2)

	def reset(self):
		self.pn = 0
		self.board = BoardStr(Game.default_space * 9)

	def get_availpos(self):
		avail = []
		for i, c in enumerate(self.board):
			if c == Game.default_space:
				avail.append(i)
		return avail

	def has_winner(self, mvpos, psym):
		return (
			all([self.board[i]==psym for i in range(mvpos//3*3, 3*(mvpos//3 + 1))]) or # check row
			all([self.board[i]==psym for i in range(mvpos%3, (mvpos%3)+9, 3)]) or # check column
			all([self.board[i]==psym for i in [0, 4, 8]]) or # check diagonal
			all([self.board[i]==psym for i in [2, 4, 6]]) # check anti-diagonal
		)
		
	def play(self):
		self.reset()
		mvpos = 0
		while True:
			gs = Game.gamestate(self.board, self.get_availpos())
			if self.has_winner(mvpos, Game.player_syms[not self.pn]):
				self.players[not self.pn].on_win(gs)
				self.players[self.pn].on_lose(gs)
				break
			elif len(gs.options) == 0:
				self.players[0].on_draw(gs)
				self.players[1].on_draw(gs)
				break
			mvpos = self.players[self.pn].get_mvpos(gs)
			self.board = BoardStr(
				self.board[:mvpos] + Game.player_syms[self.pn] + (self.board[mvpos+1:] if mvpos < 8 else "")
			)
			self.pn = not self.pn
