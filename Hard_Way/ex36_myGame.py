### A Zork-like Game by Nate Fuller

def do_something():
	return raw_input("> ")

inventory = []

def add_to_inventory(thing_to_add):
	inventory.append(thing_to_add)
	
def start():
	print "You're in a white room. There are two doors."
	print "One is on your left, the other on your right."
	doSomething = do_something()
	if "left" in doSomething:
		left_from_start()
	elif "right" in doSomething:
		right_from_start()
	elif "secret" in doSomething:
		secret_from_start()
	else:
		print "You can't do that."
		start()

def left_from_start():
	tunnel_corridor("start")

def right_from_start():
	den(False)

def secret_from_start():
	trap_door()

def tunnel_corridor(where_from):
	if where_from == "start":
		print "You are at the beginning of a tunnel."

def den(has_rope):
	print """You are now in the den.
To your left is a window, but wherever you are is too high up on a mountain 
to simply jump from the window unscathed. You must need a rope to scale down 
the side of the mountain. To your right is a book case with a few books on it. 
Nothing interesting though. Next to the window is a desk."""
	if(inventory.count("Pen") == 0):
		print "On the desk is a pen."
	doSomething = do_something()
	print doSomething
	print "You have the rope.", has_rope	
	if has_rope and doSomething == "window":
		window()
	elif not has_rope and doSomething == "window":
		print "You do not have a rope to scale down the mountain."
		den(has_rope)
	elif "desk" in doSomething:
		print "What do you want to do with the desk?"
		do_to_desk = do_something()
		print do_to_desk
		if ("search" in do_to_desk or "drawer" in do_to_desk) and not has_rope:
			print "You found a rope in the drawer! You decide to take it!"
			has_rope = True
			add_to_inventory("Rope")
		elif ("search" in do_to_desk or "drawer" in do_to_desk) and has_rope:
			print "The drawer is empty because you already took the rope."
		elif "take pen" or "pen" in do_to_desk:
			print "You took the pen from the desk!"
			add_to_inventory("Pen")
		else:
			print "You can't do that."
	elif "book case" in doSomething:
		print "There's nothing really interesting about any of the books."
	elif "inventory" in doSomething:
		print_inventory()
	else:
		print "You can't do that."
	den(has_rope)

def trap_door():
	print """A trap door opens and you begin sliding down a chute. You pick
up speed until you see an opening in the distance. You fly out 
of the opening into a shallow pond. There is a shore ahead."""

def window():
	print """You open the window."""

def print_inventory():
	print inventory
	
start()