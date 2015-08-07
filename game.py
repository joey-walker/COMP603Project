# -------------------------------------------------------------------------------------
# Dreadnought Kamzhor: A prelude to Space and Time
#
# Authors: Joseph Walker, Sarthak Khatiwada, Ori Maci, Deep Patel, Chaskarandeep Singh
#
#	Made using ply http://www.dabeaz.com/ply/
# -------------------------------------------------------------------------------------

import sys

#which area are we in?
from enum import Enum
class Areas(Enum):
		area1 = 1
		area2 = 2

# Example class
# Player, should hold onto a inventory(if we want), location of player
class Player(object):
	points = 0
	name = None
	def __init__(self,current_location):
		self.current_location = current_location
	def set_name(self,name):
		self.name = name

"""
Room -> The areas of the map, should contain connectors to other rooms, 
text of objects in room, functions determining state of room/interactivity,
Should contain the state of the room determining player progress in the area, eg.
until player completes puzzle, connector remains locked.
"""
#########Our Rooms##########
import textwrap
def introductorymessage():
	print (textwrap.dedent("""\
	
							Dreadnought Kamzhor: A prelude to Space and Time
							
							by: Joseph Walker, Sarthak Khatiwada, Ori Maci, Deep Patel, 
							    and Chaskarandeep Singh
							
							COMP603 Project
							____________________________________________________________
							
							
							You awaken to the sound of thunder.  
							
							Your eyes open up, your alarm clock replays an audio clip of thunder 
							from a terrestrial planet.
														
							You motion your hand over the floating night stand and the room brightens
							allowing you to finally see.
							
							You then proceed to punch the alarm clock in order to turn it off, as is 
							typical in the far distant future.
							
							You are a lieutenant on board the vessel Dreadnought Kamzhor, 
							you are scheduled to meet your captain on the bridge in a short while.
							
							Yet first you must first survive the perils that is leaving your room.
							
							You can talk at things, move to things, or look at things.

							"""))


def room1(p):
	#print(p[0])	
	if(p[1].lower()=="look"):
		if(p[2].lower() == "room"):
			print("You examine your room, it is a nice room; it contains a door which operates as an obvious exit.\nA computer's with its screen alight is waiting for user input.")
		elif(p[2].lower() == "alarm"):
			print("wow")
		elif(p[2].lower() == "door"):
			print("You examine the door.\nIts a monolithic sort of thing, as are all doors on Dreadnought Kamzhor.")
		elif(p[2].lower() == "computer"):
			print("wowcomp")
		elif(p[2].lower() == "joey"):
			print("Stop breaking the fourth wall.")
		else: 
			print("You don't see %s in the room." % p[2])
			
	if(p[1].lower()=="move"):
		if(p[2].lower() == "room"):
			print("You are already in the room")
		elif(p[2].lower() == "alarm"):
			print("There is no point in moving to your alarm, now follow the damn script.")
		elif(p[2].lower() == "door"):
			print("wowdoor")
		elif(p[2].lower() == "computer"):
			print("wowcomp")
		elif(p[2].lower() == "joey"):
			player.points -= 10
			print("You cannot move the narrator, as hard as you try.  You lose ten points.\nPoint count: %s" % player.points)
		else: 
			print("You can't move to %s." % p[2])
	
	if(p[1].lower()=="talk"):
		if(p[2].lower() == "room"):
			print("You talk to the room,\nunfortunately this isn't a fancy room with a built in AI.\nSo it does not respond.\nYou ponder receiving medical help for your apparent schizophrenia.")
		elif(p[2].lower() == "alarm"):
			print("You speak to the alarm, chatting of lofty philosophical ideas,\nit stares back at you in awkward silence.")
		elif(p[2].lower() == "door"):
			if player.name is None:
				print("You try speaking to the door, but the moment you open mouth it screeches at you:\n\"ERROR, OLD NAME LOST FOR WHATEVER REASON.\nINPUT NEW NAME AT YOUR COMPUTER TERMINAL\"\n")
			else:
				print("The door screeches once again as you try to speak:\n \"NAME CONFIRMED, YOU MAY PROCEED LIEUTENANT %s\"" % player.name)
		elif(p[2].lower() == "computer"):
			print("wowcomp")
		elif(p[2].lower() == "joey"):
			print("Stop talking to me.")
		else: 
			print("You can't talk to %s."% p[2])
			
			
def room2(p):
	print("\nUnfortunately you woke up too late,\nand the moment you stepped outside of your door,\na tall robot shot you in the face.")
	print("\n\nThe End.")
	sys.exit()

############################


#Dictionary declaration to be used as a switch case
room_functions = {Areas.area1 : room1,
Areas.area2 : room2
}
	
#Our different token categories
tokens = (
    'MOVE', 'TALK', 'LOOK', 'JOIN', 'QUIT', 'INV', 'DEFINITEART', 'WHITESPACE', 'NOUN'
    )
		
# Our tokens
t_MOVE			= r'(?i)move|run|walk'
t_TALK			= r'(?i)talk|speak|chat|tell|look'
t_LOOK			= r'(?i)look|glance'
t_JOIN			= r'(?i)to|at|and'
t_INV			= r'(?i)inventory' 
t_NOUN			= r'(?i)[a-z]+' # must be last in the list, but before function definitions

def t_WHITESPACE(t):
	r'\s+'
#	t.lexer.skip(1)

def t_DEFINITEART(t):
	r'(?i)the'
	return t

def t_QUIT(t):
	r'(?i)quit'
	return t

#Lexing errors
def t_error(t):
	print("error: bad characters: '%s'" % t.value[0])
	t.lexer.skip(1)

#parsing

def p_statement(p):
	'''statement : action def_noun
			     | action NOUN
				 | quit'''
				 
	if(p[1].lower() == "quit"):
		s = input("Are you sure you want to quit?: ")
		if (s.lower() == "yes"):
			sys.exit()
		else:
			return

	p[0] = p[1] + " " + p[2]
	room_functions[player.current_location](p)

def p_statement_action(p):
	'''action  : MOVE JOIN
			   | TALK JOIN
			   | LOOK JOIN''' 
	p[0] = p[1]

def p_statement_def_noun(p):
	'def_noun : DEFINITEART NOUN' #the dog
	p[0] = p[2]

def p_quit(p):
	'quit : QUIT'
	p[0] = p[1]

def p_error(p):
	print("I didn't understand the instruction")
#	print("error with %s" % p)
#	raise TypeError("Wasn't able to parse: %r" % (p.value,)) <- doesn't work


#Initialize player for starting the game
def init_player():
	return Player(Areas.area1)

#Main	
import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
parser = yacc.yacc()
"""
import logging
log = logging.getLogger() """

## Start Game instructions
player = init_player()
introductorymessage()


### How to do switch case

#player.current_location = Areas.area2

#room_functions[player.current_location]()

###

while True:
	s = input("Action > ")
	#lexer.input(s)
	
	parser.parse(s)

	while True:
		tok = lexer.token()	
		if not tok: 
			break      # No more input
		print(tok)
	
