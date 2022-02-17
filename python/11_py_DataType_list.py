#!/usr/bin/env python3
#
# Filename: 11_py_DataType_list.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	
	print ("======================================")
	# List
	print('# List')
	list1 = []
	print(type(list1))
	
	print ("======================================")
	# Define a list with variables and show its items.
	print('# Define a list with variables and show its items.')
	print('list2 = ["one","two","tree","four","five"]')
	list2 = ["one","two","tree","four","five"]
	print(len(list2))
	print(list2[0])
	print(list2[0:3])
	print(list2[:3])
	print(list2[4:])
	print(list2[-3:-1])
	print(list2)
	list2[2]=3
	print(list2)
	
	print ("======================================")
	print('list2[0] = "eins"')
	list2[0] = "eins"
	print(list2)
	
	print ("======================================")
	print('list2.append("six")')
	list2.append("six")
	print(list2)
	
	print ("======================================")
	print('list2.insert(2,"drei")')
	list2.insert(2,"drei")
	print(list2)
	
	print ("======================================")
	print(list2[4])
	print('del (list2[4])')
	del (list2[4])
	print(list2)
	
	print ("======================================")
	print(list2.pop(3))
	print(list2)
	
	print ("======================================")
	print(list2.remove("two"))
	
	print ("======================================")
	print('list3=[1,2,3,4,5]')
	list3=[1,2,3,4,5]
	print(max(list3))
	print(min(list3))
	
	print ("======================================")
	# Extendy list temporery
	print('# Extendy list temporery')
	print(list2+list3)
	# Exetend list Permanently
	print('# Exetend list Permanently')
	list2.extend(list3)
	print(list2)
	
	print ("======================================")
	list2.append(5)
	print (list2)
	print(list2.count(5))
	
		
	print ("======================================")
	# Sort temporery
	print('# Sort temporery')
	print('list4=[12,0,-1, 100,-5,15.12]')
	list4=[12,0,-1, 100,-5,15.12]
	print(sorted(list4))
	print(list4)
	# Reverse temporery
	print('# Reverse temporery')
	print(sorted(list4, reverse=True))
	print(list4)
	
	print ("======================================")
	# Sort permanent
	print('# Sort permanent')
	print('list4=[12,0,-1, 100,-5,15.12]')
	list4=[12,0,-1, 100,-5,15.12]
	print(list4)
	list4.sort()
	print(list4)
	
	print ("======================================")
	print('# Reverse permanent')
	# Reverse permanent
	print(list4)
	list4.reverse();
	print(list4)
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
