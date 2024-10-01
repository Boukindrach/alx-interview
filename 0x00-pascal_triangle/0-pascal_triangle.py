#!/usr/bin/python3

array2 = [1, 3, 3, 1]

"""if len(array) % 2 == 1:
    length = int (len(array) - 1 / 2)
    number = 0
    array1 = []
    n = 0
    o = 0
    for i in range(0, length):
        n -= o
        number += array[i]
        array1.append(number)
        n += 1
        if n == 2:
            number = array[i]
            o = 1
        if array[i] > array[i + 1]:
            break
    array2 = array1[::-1]
    total_array = array1 + array2
    print(total_array)
"""
if len(array2) % 2 == 0:
    length = int (len(array2) - 1 / 2)
    number = 0
    array1 = []
    n = 0
    o = 0
    print(length)
    for i in range(0, length):
        n -= o
        number += array2[i]
        array1.append(number)
        n += 1
        if n == 2:
            number = array2[i]
            o = 1
        if array2[i] > array2[i + 1]:
            break
    array2 = array1[::-1]
    total_array = array1 + array2
    print(total_array)
