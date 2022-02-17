#!/usr/bin/env python3
#
# Filename:	12_py_DataType_bool.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	
	print ("======================================")
	#Boolian
	# And
	print((1==1) and (2==2))
	print((1==1) and (2==3))
	print((1==2) and (2==3))
	
	print ("======================================")
	# Or
	print((1==1) or (2==2))
	print((1==1) or (2==3))
	print((1==2) or (2==3))
	
	print ("======================================")
	# bool
	print(bool(2))
	print(bool(0))
	print(bool(0.0))
	print(bool("Mahdi"))
	print(bool(""))
	
	
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
