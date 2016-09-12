from random import randint

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
		tmp = ""
		for i, square in enumerate(b.squares):
			tmp += str(square)
			if (i+1)%10==0:
				print(tmp)
				tmp=""
		print (tmp)

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
	def __repr__(self):
		return "[    ]"

	def totalspace(self):
		return None

#chute
class chute(object):
	def __init__(self, target):
		self.target = target

	def __repr__(self):
		return "[v %s]" %self.target

	def totalspace(self):
		return self.target

#ladder
class ladder(object):
	def __init__(self, target):
		self.target = target

	def __repr__(self):
		return "[^ %s]" %self.target

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
	g=game(2, b)
	p1 = g.players[0]
	g.playthegame()
	