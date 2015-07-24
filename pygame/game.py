# -----------------------------------------------------------------------------
# Dreadnought Khamzor: A prelude to Time and Space
#
# Authors: Joseph Walker, Sarthak Khatiwada, Ori Maci, Deep Patel, Chaskarandeep Singh
# -----------------------------------------------------------------------------


#Our different token categories
tokens = (
    'MOVE', 'TALK',
    )
		
# Our tokens
t_MOVE		= r'move'


#Lexing errors
def t_error(t):
	print("error: bad characters: '%s'" % t.value[0])
	t.lexer.skip(1)

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
	