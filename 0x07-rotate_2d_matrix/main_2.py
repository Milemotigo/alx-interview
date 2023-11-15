#!/usr/bin/python3


lst = [[1,3,5], [2,6,7], [7, 8, 9]]

length = len(lst)
for i in range(length):
    for j in range(i, length):
        lst[j][i], lst[j][i] = lst[i][j], lst[i][j]

    for i in range(length):
        print(lst[i].reversed())
