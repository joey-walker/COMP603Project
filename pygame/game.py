# -----------------------------------------------------------------------------
# Dreadnought Khamzor: A prelude to Time and Space
#
# Authors: Joseph Walker, Sarthak Khatiwada, Ori Maci, Deep Patel, Chaskarandeep Singh
#
#	Made using ply http://www.dabeaz.com/ply/
# -----------------------------------------------------------------------------


#Our different token categories
tokens = (
    'MOVE', 'TALK', 'LOOK', 'JOIN', 'WHITESPACE'
    )
		
# Our tokens
t_MOVE			= r'move|run|walk'
t_TALK			= r'talk|speak|chat|tell'
t_LOOK			= r'look|glance'
t_JOIN			= r'to|at|and' # I walked to him
t_WHITESPACE	= r'\s'

#Lexing errors
def t_error(t):
	print("error: bad characters: '%s'" % t.value[0])
	t.lexer.skip(1)

# Example class
class Human(object):
	pass		
		
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
	