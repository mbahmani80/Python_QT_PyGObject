#!/usr/bin/env python3
#
# Filename: 08_py_prog_validate_input_data.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 12.05.2020


from datetime import datetime

#-----------------------------------------------------------------------

def print_input_data():
	fname = input("Enter first name: ")
	lname = input("Enter last name: ")
	age = input("Enter Age: ")
	birthdate = input('Enter the date in mm/dd/yyyy format: ')
	
	print("*********** Input data ***********")
	print(" First Name:  {f} \n Last Name: {l}  \n Age: {a}".format(f=fname, l=lname, a=age))
	print(" Birthdate:  {d} \n ".format(d=birthdate))
	print("**********************************\n")
########################################################################

#-----------------------------------------------------------------------

def print_validate_input_data():
	fname = input("Enter first name: ")
	lname = input("Enter last name: ")
	age_input = input("Enter Age: ")
	birthdate1 = input('Enter the date in mm/dd/yyyy format: ')
		
	try:
		birthdate=datetime.strptime(birthdate1, '%m/%d/%Y')
		print('The date {} is valid.'.format(birthdate))
		try:
			age = int(age_input)
			print("*********** Input data ***********")
			print(" First Name:  {f} ".format(f=fname))
			print(" Last Name: {l}  ".format(l=lname))
			print(" Age: {a}".format(a=age))
			print(" Birthdate:  {d} \n ".format(d=birthdate))
			print("**********************************")
			print ("type of input ", type(fname))
			print ("type of input ", type(lname))
			print ("type of input ", type(age))
			print ("type of input ", type(birthdate))
		except ValueError:
			print("Error ...!")
			print("The Age is not valid, please try again.\n")
	except ValueError:
		print('The date {} is invalid'.format(birthdate1))
########################################################################

#-----------------------------------------------------------------------
def main():
	print_input_data()
	print_validate_input_data()

#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
