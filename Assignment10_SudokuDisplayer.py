# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:19:44 2020

@author: MADCAT
"""


sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]

for i in sudoku:
    if sudoku.index(i) % 3  == 0:
        print("\n"+ 11 * "- ")
    else:
        print()
    for x in range(len(i)):
       if x in [2 ,5]:
           print(f"{i[x]} |", end = " ")
       else:
           print(i[x], end = " ")
print("\n"+ 11 * "- ")       
        