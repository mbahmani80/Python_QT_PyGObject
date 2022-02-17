#!/usr/bin/env python3
#
# Filename: 14_py_DataType_set.py
#
# Copyright (C) 2020 Mahdi Bahmani
#
# 18.05.2020

import sys

#-----------------------------------------------------------------------
def main():
	print ("======================================")
	# Making set method1
	set1 = {10,10,10,10,10,11,12,12,"one","two","one"}
	print (set1)
	print(type(set1))
	print(len(set1))
	
	print ("======================================")
	# Making set method2
	list1 = [10,10,10,10,10,11,12,12,"one","two","one"]
	set2 = set(list1)
	print (list1)
	print (set2)
	print(type(set2))
	
	print ("======================================")
	# Check filed
	print("one" in set2)
	print("ten" in set2)
	print("ten" not in set2)
	
	print ("======================================")
	# add/remove filed
	print(set1)
	set1.add(24)
	print(set1)
	set1.remove("one")
	print(set1)
	
	print ("======================================")
	set3 = {'192.168.2.1','192.168.2.2','192.168.2.3','172.20.12.10','172.20.12.21'}
	set4 = {'192.168.2.5','192.168.2.7','192.168.2.3','172.20.12.10','172.20.12.31'}
	print("set3: ", set3)
	print("set4: ", set4)
	print ("======================================")
	# Intersection
	print('# Intersection')
	print(set3.intersection(set4))
	
	print ("======================================")
	# Diffrence
	print("set3: ", set3)
	print("set4: ", set4)
	print('# Diffrence')
	print('set3.difference(set4)')
	print(set3.difference(set4))
	print('set4.difference(set3)')
	print(set4.difference(set3))
	
	print ("======================================")
	# Concat
	print("set3: ", set3)
	print("set4: ", set4)
	set5 = set3.union(set4)
	print(set5)
	
	print ("======================================")
	# Clear
	set1.clear()
	print(set1)
	set2.clear()
	print(set2)
	set3.clear()
	print(set3)
	set4.clear()
	print(set4)
	
#-----------------------------------------------------------------------
if __name__ == "__main__":
  main()
