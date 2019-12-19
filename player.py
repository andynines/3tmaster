
import abc
import collections
import random

class Player(metaclass=abc.ABCMeta):

	def __init__(self):
		self.wins = 0
		self.draws = 0

	@abc.abstractmethod
	def get_mvpos(self, gs):
		pass

	@abc.abstractmethod
	def on_win(self, gs):
		pass

	@abc.abstractmethod
	def on_draw(self, gs):
		pass

	@abc.abstractmethod
	def on_lose(self, gs):
		pass

class Human(Player):

	def __init__(self):
		super().__init__()

	def get_mvpos(self, gs):
		print(gs.board)
		avail = [str(o//3 + 1) + ',' + str((o%3) + 1) for o in gs.options]
		while True:
			inp = input(' '.join(avail) + ": ")
			if inp in avail:
				break
		return 3*(int(inp[0])-1) + int(inp[2])-1

	def on_win(self, gs):
		self.wins += 1
		print(gs.board)
		print("Victory")

	def on_draw(self, gs):
		self.draws += 1
		print(gs.board)
		print("Draw")

	def on_lose(self, gs):
		print(gs.board)
		print("Defeat")

class AI(Player):

	memnode = collections.namedtuple("STMemoryNode", ["board", "choice"])
	save_file = "3tmind.dat"

	def __init__(self, read_save=False):
		super().__init__()
		self.ltmem = {}
		self.stmem = []
		if read_save:
			with open(AI.save_file, 'r') as f:
				while True:
					byte = f.read(1)
					if byte == "":
						break
					board = byte + f.read(8)
					options = []
					while True:
						byte = f.read(1)
						if byte == ':':
							break
						options.append(int(byte))
					self.ltmem[board] = options
				
	def get_mvpos(self, gs):
		if gs.board not in self.ltmem:
			self.ltmem[gs.board] = gs.options
		mvpos = random.choice(self.ltmem[gs.board])
		self.stmem.append(AI.memnode(gs.board, mvpos))
		return mvpos

	def on_win(self, gs):
		self.wins += 1
		self.stmem = []

	def on_draw(self, gs):
		self.draws += 1
		self.stmem = []

	def on_lose(self, gs):
		while True:
			lastmem = self.stmem[-1]
			self.ltmem[lastmem.board].remove(lastmem.choice)
			if not self.ltmem[lastmem.board]:
				del self.ltmem[lastmem.board]
				self.stmem = self.stmem[:-1]
				if len(self.stmem) == 0:
					return
				else:
					continue
			break
		self.stmem = []

	def freeze(self):
		with open(AI.save_file, 'w') as f:
			for board, options in self.ltmem.items():
				f.write(board + "".join([str(o) for o in options]) + ':')

class Dullard(Player):

	def __init__(self):
		super().__init__()

	def get_mvpos(self, gs):
		return random.choice(gs.options)

	def on_win(self, gs):
		self.wins += 1

	def on_draw(self, gs):
		self.draws += 1

	def on_lose(self, gs):
		pass
