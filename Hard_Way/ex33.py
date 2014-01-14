def populate_list(for_loop, the_list, max_num, step):
	"""Populate a passed in EMPTY list. 'for_loop' tells us whether we want
	to execute the for-loop or the while-loop, both should produce the same output.
	'max_num' is our maximum number, not inclusive.
	'step' is how much we want to increment our numbers by."""
	i = 0
	if not for_loop:
		while i < max_num:
			append_to_list(the_list, i)
			i += step
	else:
		for i in range(0, max_num, step):
			append_to_list(the_list, i)

def append_to_list(the_list, the_num):
			print "At the top i is %d" % the_num
			the_list.append(the_num)
	
			print "Numbers now: ", the_list
			print "At the bottom i is %d" % the_num
			
for_or_while = raw_input("True for for-loop, False for while-loop: ")
the_max_num = int(raw_input("When should I stop counting? (Enter an integer): "))
the_step = int(raw_input("Space between count? (Enter an integer): "))
numbers = []

populate_list(for_or_while, numbers, the_max_num, the_step)

print "The numbers: "

for num in numbers:
	print num