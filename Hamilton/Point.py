class Point:
	def __init__(self,x,y):
		self.x = float(x)
		self.y = float(y)
	def __str__(self):
		return "(%s, %s)" % (self.x, self.y)
