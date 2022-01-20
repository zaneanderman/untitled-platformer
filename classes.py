#!/usr/bin/python3
from pyglet import shapes
class Platform():
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.sprite = shapes.Rectangle(x, y, width, height, color=(150, 150, 100))
	def collidingwith(self, rect):
		if (self.x + self.width > rect.x and
			self.x < rect.x + rect.width and
			self.y + self.height > rect.y and
			self.y < rect.y + rect.height):  
			return True
		return False

class Level():
	def __init__(self, leveltext):
		self.platforms = []
		self.exit = (0,0)
		self.start = (0,0)
		self.generate(leveltext)
	def generate(self, leveltext):
		for chunk in leveltext.split(":"):
			if chunk[0] == "p":
				nums = chunk[1:].split(",")
				self.platforms.append(Platform(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])))
			elif chunk[0] == "e":
				self.exit = tuple(int(i) for i in chunk[1:].split(","))
			elif chunk[0] == "s":
				self.start = tuple(int(i) for i in chunk[1:].split(","))

