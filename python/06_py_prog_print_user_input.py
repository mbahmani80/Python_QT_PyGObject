#!/usr/bin/env python3
#
# Filename: 06_py_prog_print_user_input.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 12.05.2020

def print_data():
	fname = "Tara"
	lname = "Ahmadi"
	age = 22
	height = 161.7

	print("*********** Input data ***********")
	print(" First Name:  {f} \n Last Name: {l}".format(f=fname, l=lname))
	print(" Age:  {a} \n Height: {h}".format(a=age, h=height))
	print("**********************************\n")
	print(type(fname), "object's memory address",id(fname))
	print(type(lname), "object's memory address",id(lname))
	print(type(age),   "object's memory address",id(age))
	print(type(height),"object's memory address",id(height))
	print("===================================\n")
#-----------------------------------------------------------------------

def print_input_data():
	fname = input("Enter first name: ")
	lname = input("Enter last name: ")
	age = input("Enter Age: ")
	height = input("Height length: ")

	print("*********** Input data ***********")
	print(" First Name:  {f} \n Last Name: {l}".format(f=fname, l=lname))
	print(" Age:  {a} \n Height: {h}".format(a=age, h=height))
	print("**********************************\n")
	print(type(fname))
	print(type(lname))
	print(type(age))
	print(type(height))
	
	
########################################################################

#-----------------------------------------------------------------------

def main():
	print("Calls print_data()")
	print_data()
	print("Calls print_input_data()")
	print_input_data()

#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
