from random import randint
from math import floor, ceil, sqrt, log10

#game
class game(object):
	def __init__(self, playnum, gboard):
		self.playnum = playnum
		self.gboard = gboard
		self.players=[]
		for i in range(playnum):
			p = player(i, gboard)
			self.players.append(p)
	def playtheplayer(self, p):
		p.playdice()
		if p.haswon():
			print ("Player %s won the game mothafuckaaaa." %p.id)
			return True
		else:
			for player in g.players:
				print(player)
			print ()
			return False
	def playtheround(self):
		for player in self.players:
			res = self.playtheplayer(player)
			if res == True:
				return True
		return False
	def playthegame(self):
		iswinrar = False
		while not iswinrar:
			iswinrar = self.playtheround()

#board
class board(object):
	def __init__(self):
		self.squares = [
		  ladder(38), space(), space(), ladder(14), space(), space(), space(), space(), ladder(31), space(), 
		  space(), space(), space(), space(), space(), chute(6), space(), space(), space(), space(), 
		  ladder(42), space(), space(), space(), space(), space(), space(), ladder(84), space(), space(), 
		  space(), space(), space(), space(), space(), ladder(44), space(), space(), space(), space(), 
		  space(), space(), space(), space(), space(), space(), space(), chute(26), chute(11), space(), 
		  ladder(67), space(), space(), space(), space(), chute(53), space(), space(), space(), space(), 
		  space(), chute(19), space(), chute(60), space(), space(), space(), space(), space(), space(), 
		  ladder(91), space(), space(), space(), space(), space(), space(), space(), space(), ladder(100),
		  space(), space(), space(), space(), space(), space(), chute(24), space(), space(), space(), 
		  space(), space(), chute(73), space(), chute(75), space(), space(), chute(78), space(), space(), 
		 ]

	def printboard(self):
		#result = log10(input) calculates 10**result = input.
		#log10 is the inverse of raising 10 to a power of a number.
		#Floor rounds down to whole number; Ceil rounds up to whole number
		#Sqrt is square root. Helps build a square board

		#int spaces is the number of decimal places
		#to write the largest space number
		intspaces = floor(log10(len(self.squares)+1))+1
		board_side = ceil(sqrt(len(b.squares)))
		#The code %% outputs literal %. Format code %d is preferred for
		#numbers. Format code %04d will print 18 as '0018' by padding
		#with 0s to be at least 4 characters.
		#%%0%dd will format to replace the %% with % and the %d with a
		#number, resulting in a string like "%05d". This format string
		#can be used to pad out all space numbers to the same width
		#string.
		formatcode = "%%0%dd"%intspaces
		#separator is the string that splits the rows. For rows that
		#have a space that moves into the above row, the section of
		#the separator over that cell will be ^ instead of -.
		separator = "-"*((intspaces+5)*board_side + 1)
		cell_width = intspaces+5

		#The board is calculated from the bottom up, so we can not print
		#each row as we calculate it. Each row will be prepended to this
		#variable and printed at the end.
		fullboard = ""
		#Each cell is 2 lines on the termina: line 1 is the cell number,
		#line 2 is extra data like if it is a chute/ladder, and target.
		rowpt1, rowpt2 ="|", "|"
		#The direction the row is filled in has to change each row.
		dir_right = True

		print(separator)
		for i, square in enumerate(b.squares):
			if isinstance(square, space):
				target = " "*intspaces
			else:
				target = formatcode%square.target

			cell_pt1 = "  " + formatcode%(i+1) + "  "
			cell_pt2 = " " + square.symbol + " " + target + " "
			border = "|" if (i+1)%board_side==0 else ">" if dir_right else "<"
			if dir_right:
				rowpt1 += cell_pt1 + border
				rowpt2 += cell_pt2 + border
			else:
				rowpt1 = border + cell_pt1 + rowpt1
				rowpt2 = border + cell_pt2 + rowpt2

			if (i+1)%board_side==0:
				fullboard = rowpt1 + "\n" + rowpt2 + "\n" +\
					    separator  + "\n" + fullboard
				rowpt1, rowpt2 = "|", "|"
				dir_right = not dir_right
				if i+1 is len(b.squares):
					#Do not put ^^^ on top separator
					separator = "-"*((intspaces+5)*board_side + 1)
				elif dir_right:
					separator = "^"*cell_width + "-"*(cell_width*(board_side-1) + 1)
				else:
					separator = "-"*(cell_width*(board_side-1) + 1) + "^"*cell_width

		print (fullboard)

#player
class player(object):
	def __init__(self, playerid, pboard):
		self.spot = 0
		self.id = (playerid+1)
		self.pboard = pboard

	def __repr__(self):
		return "Player %s is on space %s" %(self.id, self.spot)

	def playdice(self):
		print ("Player %s: Hit enter to roll" %self.id, end="")
		input()
		playdice = randint(1,6)
		print ("Player %s has rolled a %s" %(self.id, playdice))
		newspace = (self.spot+playdice)
		if newspace >= len(self.pboard.squares):
			newspace = len(self.pboard.squares)
		spaceinfo = self.pboard.squares[newspace-1]
		if spaceinfo.totalspace() is not None:
			newspace = spaceinfo.totalspace()
			print ("Player %s has hit a %s to space %s!" %(self.id, type(spaceinfo).__name__, newspace))
		self.spot=newspace

	def haswon(self):
		return self.spot == len(self.pboard.squares)

#space
class space(object):
	symbol = " "
	def __repr__(self):
		return "[    ]"

	def totalspace(self):
		return None

#chute
class chute(object):
	symbol = "v"
	def __init__(self, target):
		self.target = target

	def __repr__(self):
		return "[%s %s]" %(self.symbol, self.target)

	def totalspace(self):
		return self.target

#ladder
class ladder(object):
	symbol = "^"
	def __init__(self, target):
		self.target = target

	def __repr__(self):
		return "[%s %s]" %(self.symbol, self.target)

	def totalspace(self):
		return self.target

if __name__=="__main__":
	b=board()
	b.printboard()
	while True:
		try:
			playersnum = int(input("How many players this time? "))
		except ValueError:
			print("Why would you do that?  Enter a number, douche canoe.")
			continue

		if playersnum < 1:
			print("Sorry, purple doesn't fit enough elephants, and you're bad at numbers.  Try again.")
		else:
			break
	g=game(playersnum, b)
	g.playthegame()
