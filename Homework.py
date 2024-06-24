# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 11:48:42 2024

@author: user
"""
# i=0
# while i <10:
#     i +=1
#     print(i)
    
# print("程式執行完畢")
# total = 0
# for i in range(1,100,2):   
#     total +=i
#     i +=i
# print("奇數和:",total)

# seven = 0
# for row in range(7,100,7):
#     seven +=row
#     # print(row)
#     row += row
# print("7的加總總合為:",seven)

# five = []
# for item in range(5,100,5):
#     if item %5 ==0 and item %15 ==0:
#         five.append(item)
# print("可以同時被5,15整除的數字為:",five)

three = 0
seven = 0
five=[]
for i in range(0,100):
    if i % 7 ==0:
        seven += i
    if i % 2 != 0:
        three +=i
    if i % 5 ==0 and i %15 ==0:
        five.append(i)
        print(i)
print("7的加總總合為:",seven)
print("奇數和:",three)
print("可以同時被5和15整除的數字為:",five)
        