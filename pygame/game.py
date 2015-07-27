# -----------------------------------------------------------------------------
# Dreadnought Khamzor: A prelude to Time and Space
#
# Authors: Joseph Walker, Sarthak Khatiwada, Ori Maci, Deep Patel, Chaskarandeep Singh
#
#	Made using ply http://www.dabeaz.com/ply/
# -----------------------------------------------------------------------------

import sys

# Example class
class Human(object):
	pass
	
#Our different token categories
tokens = (
    'MOVE', 'TALK', 'LOOK', 'JOIN', 'WHITESPACE', 'QUIT', 'INV'
    )
		
# Our tokens
t_MOVE			= r'move|run|walk'
t_TALK			= r'talk|speak|chat|tell'
t_LOOK			= r'look|glance'
t_JOIN			= r'to|at|and' # I walked to him
t_WHITESPACE	= r'\s'
t_INV			= r'inventory' #do we want this?

#and what of Nouns? 

def t_QUIT(t):
	r'quit'
	s = input("Are you sure you want to quit?: ")
	if (s == "yes" or s == "y" or s == "Yes"):
		sys.exit()

#Lexing errors
def t_error(t):
	print("error: bad characters: '%s'" % t.value[0])
	t.lexer.skip(1)

#parsing
	""" Parsing?

def p_statement_action(p):
	'''action : MOVE JOIN NOUN
			  | TALK JOIN NOUN
			  | LOOK JOIN NOUN
	
"""

def p_error(p):
	raise TypeError("Wasn't able to parse: %r" % (p.value,))


#Main	
import ply.lex as lex
lexer = lex.lex()

import ply.yacc as yacc
#yacc.yacc()

s = input("Action > ")
lexer.input(s)

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
	