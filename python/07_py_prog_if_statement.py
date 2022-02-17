#!/usr/bin/python3
#
# Filename: 07_py_prog_if_statement.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 12.05.2020
#
# python2: raw_input()
# python3: input()

#-----------------------------------------------------------------------

def if_statement_example ():
	my_number = int(input('Enter an integer: '))
	if (my_number == 0):
		print ("The number is zero.\n")
	if (my_number > 0):
		print ("The number is positive.\n")
	if (my_number < 0):
		print ("The number is negative.\n")
	if not my_number == 50:
		print('the value of my_number different from 50')
########################################################################

#-----------------------------------------------------------------------

def if_else_statement_example():
	my_number = int(input('Enter a number: '))
	if (my_number > 0):
		print ("The number is positive.\n")
	else:
		print ("The number is zero or negative.\n")


########################################################################

#-----------------------------------------------------------------------

def nested_if_else_statement_example():
	number = 33
	guess = int(input('Enter an integer: '))
	if guess == number:
		print ('Congratulations, you gueesed it.')
	elif guess < number:
		print ('No, it is a little higher than that.')
	else:
		print ('No, it is a little lower than that.')
	print ('Done')



########################################################################

#-----------------------------------------------------------------------
def the_and_operator_if_statement():
	q1 = input('Is the weather cold? y/n: ')
	x = True if q1 == "y" else False
	q2 = input('Are you happy? y/n: ')
	y = True if q2 == "y" else False
	#The validation will be True only if all the expressions generate a value True
	if x and y:
	    print('Both x and y are True')
	else:
	    print('x is False or y is False or both x and y are False')
########################################################################

#-----------------------------------------------------------------------

def the_in_operator_if_statement():
	fcolor = input('What is your favorite color? : ')
	#create a list
	colorlist = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'pink', 'silver', 'gold', 'beige', 'brown', 'grey', 'black', 'white']
	
	# in operator is used to replace various expressions that use the or operator
	if fcolor in colorlist:
		print(fcolor + ': Your color is in list')
	
	#Alternate if statement with or operator
	if fcolor == 'red' or fcolor == 'brown' or fcolor == 'black':
		print(fcolor + ' your color is warm')
	
########################################################################

#-----------------------------------------------------------------------

def main():
	print ("Calls if_statement_example ();\n")
	if_statement_example ()
    
	print ("**********************************\n")
    
	print ("Calls if_else_statement_example();\n")
	if_else_statement_example()
    
	print ("**********************************\n")
    
	print  ("Calls nested_if_else_statement_example();\n")
	nested_if_else_statement_example()
    
	print ("**********************************\n")

	print  ("Calls the_and_operator_if_statement();\n")
	the_and_operator_if_statement()
    
	print ("**********************************\n")
	
	print  ("Calls the_in_operator_if_statement();\n")
	the_in_operator_if_statement()
    
	print ("**********************************\n")

#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
