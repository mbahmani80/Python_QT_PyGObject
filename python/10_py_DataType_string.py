#!/usr/bin/env python3
#
# Filename: 10_py_DataType_string.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	mystring = "Knowledge is Power is a True Saying."
	print (mystring)
	
	print ('len(mystring) = ', len(mystring))	
	
	i=0
	while i < len(mystring):
		print(i,mystring[i])
		i += 1
	
	
	#  The indexing of Array start with Zero in Python?
	print (mystring[0])
	print (mystring[1])
	print (mystring[35])
	print (mystring[-1])
	
	print (mystring[10], mystring.index("i"))
	print (mystring.count("i"))
	print (mystring[:])
	print (mystring[1:5])
	print (mystring[::])
	# Print Step 2
	print (mystring[0:5:2])
	# Print Reverse
	print (mystring[::-1])
	
	print ("======================================")
	print (mystring.find("Power"))
	print ("======================================")
	print ("mystring[13]")	
	print (mystring[13])
	
	print ("======================================")
	# The output will be -1 if it couldn't find a pattern.
	print ('mystring.find("Mahdi")')
	print (mystring.find("Mahdi"))
	
	print ("======================================")
	print (mystring.lower())
	print (mystring.upper())
	
	print ("======================================")
	print ('mystring.startswith("K"))')
	print (mystring.startswith("K"))
	
	print ("======================================")	
	print ('mystring.startswith("k")')
	print (mystring.startswith("k"))
	
	print ("======================================")
	print ('mystring.startswith("k")')
	print (mystring.startswith("z"))
	
	print ("======================================")
	print ('mystring.startswith("z")')
	print (mystring.endswith("."))
	
	print ("======================================")
	print ('mystring.endswith("M")')
	print (mystring.endswith("M"))
	
	print ("======================================")
	mystring2 = "    Knowledge   is   Power   "
	print ("mystring2.strip()")
	print (mystring2)
	print (mystring2.strip())
	
	print ("======================================")	
	mystring3 = "***  Knowledge   is   Power ***"
	print (mystring3)
	print (mystring3.strip("*"))
	print (mystring3.replace(" ",""))
	
	print ("======================================")
	mystring4 = "one,two,tree,four,five" 
	print (mystring4)
	# Makes an array from string
	print (mystring4.split(","))
	
	print ("======================================")
	# Insert _ after each character
	print("# Insert _ after each character")
	mystring5 = "one,two,tree,four,five" 
	print (mystring5)
	print ("_".join(mystring5))
	
	print ("======================================")
	# Mix String and Variabes
	print("# Mix String and Variabes %s=string, %d=int, %f=flot")
	age = 23
	hight = 180.23
	name = "Mahdi"
	mystring5 = "Name: %s, Age: %d, hight: %f"
	print (mystring5)
	print (mystring5 % (name,age,hight))
	
	print ("======================================")
	# Slice
	print("# Slice")
	mystring5 ="inet 192.168.2.100  netmask 255.255.255.0  broadcast 192.168.2.255"
	print(mystring5)
	print(mystring5[5:18])
	print(mystring5[5:])
	print(mystring5[:18])
	print(mystring5[-13:-1])
	
	print ("======================================")
	# Mix String
	forename = "Mahdi"
	surname = "Bahmani"
	print (forename + surname )
	print (forename + " " + surname)
	print (forename * 2)
	
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
