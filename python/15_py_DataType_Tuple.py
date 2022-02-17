#!/usr/bin/env python3
#
# Filename: 15_py_DataType_Tuple.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	print ("======================================")
	# Tuple
	print('# Tuple')
	list1_tuple1 = ()
	print(type(list1_tuple1))
	
	print ("======================================")
	list1_tuple1 = (1,"one",1.1)
	print (list1_tuple1)
	
	# 'tuple' object does not support item assignment (immutable)
	print (list1_tuple1[2])
	list1_tuple1[2] = "two"
	
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
