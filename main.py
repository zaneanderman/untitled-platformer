#!/usr/bin/python3
import pyglet
from pyglet import shapes
import random
screen = pyglet.window.Window(640, 500, "No")
leftbird = pyglet.image.load("sprites/duckleft.png")
rightbird = pyglet.image.load("sprites/duckright.png")
from levels import levels
import classes
from classes import Level, Platform

keys = pyglet.window.key.KeyStateHandler()
screen.push_handlers(keys)
gravity = 0.5
friction = 0.1

class Player(pyglet.sprite.Sprite):
	def __init__(self, *args, **kwargs):
		super(Player, self).__init__(*args, **kwargs)
		self.vy = 0
		self.vx = 0
		self.attackcooldown = 0
		self.onground = False
		self.direction = "right"
		self.timeshit = 0

global player, currentlevel
controls = {"left":pyglet.window.key.LEFT, "up":pyglet.window.key.UP, "right":pyglet.window.key.RIGHT}
player = Player(rightbird, 0, 0)
currentlevel = None

def loadlevel(levelnum):
	global currentlevel, player
	currentlevel = levels[levelnum]
	player.x = currentlevel.start[0]
	player.y = currentlevel.start[1]

loadlevel(1)
print(currentlevel)

def update(dt):
	player.y += player.vy
	player.onground = False
	isfalling = (player.vy < 0)
	for platform in currentlevel.platforms:
		if platform.collidingwith(player):
			if isfalling:
				player.y = platform.y + platform.height
				player.onground = True
				player.doublejump = True
				player.vy = 0
			else:
				player.y = platform.y - player.height
				player.vy = 0

	player.x += player.vx
	ismovingleft = (player.vx < 0)
	for platform in currentlevel.platforms:
		if platform.collidingwith(player):
			if ismovingleft:
				player.x = platform.x + platform.width
				player.vx = 0
			else:
				player.x = platform.x - player.width
				player.vx = 0

	if keys[controls["up"]] and player.onground:
		player.vy = 10
	
	if keys[controls["left"]] and not keys[controls["right"]]:
		player.direction = "left"
		player.image = leftbird
		if player.vx > -4:
			player.vx -= 0.2
	
	if keys[controls["right"]] and not keys[controls["left"]]:
		player.direction = "right"
		player.image = rightbird
		if player.vx < 4:
			player.vx += 0.2

	player.vy -= gravity
	if player.vx > 0:
		player.vx = max(0, player.vx - friction)
	elif player.vx < 0:
		player.vx = min(0, player.vx + friction)
@screen.event
def on_draw():
	screen.clear()
	for platform in currentlevel.platforms:
		platform.sprite.draw()
	player.draw()

pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()
