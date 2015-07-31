# -------------------------------------------------------------------------------------
# Dreadnought Khamzor: A prelude to Space and Time
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

		
# Example class
# Player, should hold onto a inventory(if we want), location of player
class Player(object):
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
#########Rooms###############




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
	
"""nouns should be everything in a room"""


"""Make room object that contains all parts of the room?

noun would need to then be all parts of that room? 
what if we want multiple different parts to a room?

"""

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
	print("statement: %s" % p)

def p_statement_action(p):
	'''action  : MOVE JOIN
			   | TALK JOIN
			   | LOOK JOIN''' #look to
	print("action: %s" % p)
	

def p_statement_def_noun(p):
	'def_noun : DEFINITEART NOUN' #the dog
	print("def_noun: %s" % p)

def p_quit(p):
	'quit : QUIT'
	s = input("Are you sure you want to quit?: ")
	if (s.lower() == "yes"):
		sys.exit()

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
print("hsdhkjgdsk")

while True:
	s = input("Action > ")
	print(s)
	lexer.input(s)
	
	parser.parse(s)

	while True:
		tok = lexer.token()	
		if not tok: 
			break      # No more input
		print(tok)
	
