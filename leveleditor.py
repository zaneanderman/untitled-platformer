#!/usr/bin/python3
import pyglet
from pyglet import shapes
from pyglet.window import mouse

screen = pyglet.window.Window(640, 500, "No")
rightbird = pyglet.image.load("sprites/duckright.png")
mode = "platform"
text = pyglet.text.Label("platform", x=0, y=screen.height, font_size=15, anchor_x="left", anchor_y="top")
platforms = {"currentpos":None, "current":None, "old":[]}
[5]

def update(dt):
	pass

@screen.event
def on_mouse_motion(x, y, dx, dy):
	if platforms["currentpos"]:
		if x < platforms["currentpos"][0]:
			platforms["current"].x = x
		else:
			platforms["current"].x = platforms["currentpos"][0]
		if y < platforms["currentpos"][1]:
			platforms["current"].y = y
		else:
			platforms["current"].y = platforms["currentpos"][1]

		platforms["current"].width = abs(platforms["currentpos"][0] - x)
		platforms["current"].height = abs(platforms["currentpos"][1] - y)

@screen.event
def on_mouse_press(x, y, button, modifiers):
	if platforms["current"]:
		platforms["old"].append(platforms["current"])
		platforms["current"] = None
		platforms["currentpos"] = None
	else:
		platforms["current"] = shapes.Rectangle(x,y,0,0,color=(150, 150, 100))
		platforms["currentpos"] = (x,y)

@screen.event
def on_draw():
	screen.clear()
	text.draw()
	if platforms["current"]:
		platforms["current"].draw()
	[platform.draw() for platform in platforms["old"]]


pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()