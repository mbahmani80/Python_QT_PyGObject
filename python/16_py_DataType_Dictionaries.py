#!/usr/bin/env python3
#
# Filename: 16_py_DataType_Dictionaries.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	print ("======================================")
	# Dictionaries
	print('# Dictionaries')
	person = {}
	print(type(person))
	
	print ("======================================")
	person = {
		"forename": "Johnny",
		"surname": "Depp",
		"age": "57",
		"country":	"USA",
		"nationality":"American",
		"movies": ["City of Lies","Pirates of the Caribbean","Alice in Wonderland","Hotel"],
		"physical_attrs": {
			"height": 180,
			"weight": 75
		}
	}
	print(person.keys())
	print ("======================================")
	print(person.values())
	print ("======================================")
	print(person["forename"])
	print(person["surname"])
	print(person["age"])
	print(person["country"])
	print(person["nationality"])
	print ("======================================")
	print(person["movies"])
	print(person["movies"][2])
	print ("======================================")
	print(person["physical_attrs"])
	print(person["physical_attrs"]["weight"])
	
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
