#!/usr/bin/python3

from prettytable import PrettyTable
    
x = PrettyTable()
listcolumn = []
listrow = []


for i in range(int(input("how many column do you need?"))):
    print("please enter header" , i+1)
    listcolumn.append(input())
    
x.field_names = listcolumn
print(x)

for i in range(len(listcolumn)):
    print("Please enter " , listcolumn[i])
    listrow.append(input())

x.field_names = listcolumn
x.add_row(listrow)
print(x)