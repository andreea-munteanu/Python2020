# 1. Write a function to return a list of the first n numbers in the Fibonacci string.
import math


def Fibo(n) :
    fibonacci = []
    a = 0
    b = 1
    i = 0
    while i < n :
        c = a + b
        a = b
        b = c
        fibonacci.append(b)
        i += 1
    return fibonacci

#
# a = Fibo(10)
# print(a)


def fibonacci(n):
    list = [1, 1]
    for i in range(2,n):
        list.append(sum(list[-2:]))
    print(list[:n])


# fibonacci(10)


# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def prime(n) :
    if n == 2 :
        return True
    if n % 2 == 0 or n == 1 :
        return False
    for i in range(3, int(math.sqrt(n)), 2) :
        if n % i == 0 :
            return False
    return True


# print(prime(19))

def prime_numbers(list) :
    for i in range(len(list)) :
        if prime(list[i]) :
            print(list[i])


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# prime_numbers(list)

def recursie(n):
    if n == 0 :
        return n
    else:
        print(n)
        return recursie(n-1)


# recursie(100)

# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited
# with b, a - b, b - a)

def set_operations(a, b) :
    # a intersection b
    # a reunited b
    # a - b
    # b - a
    set_a = set(a)
    set_b = set(b)
    print(set_a.union(set_b))
    print(set_a.intersection(set_b))
    print(set_a - set_b)
    print(set_b - set_a)


# a = [1,2,3,4,5,6]
# b = [4,5,6,7,8,9,10]
# set_operations(a, b)

# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers)
# and a start position (integer). The function will return the song composed by going though the musical notes
# beginning with the start position and following the moves given as parameter.
# Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]

def compose(notes: [str], moves: [int], start_pos: int) :
    print('nu-nteleg')


# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing
# all the elements under the main diagonal with 0 (zero).

def replace_matrix(matrix) :
    for i in range(len(matrix)) :
        for j in range(len(matrix[0])) :
            if i > j :
                matrix[i][j] = 0
    print(matrix)


# a = [[1,5,6,8],[1,2,5,9],[7,5,6,2],[9,9,9,9]]
# replace_matrix(a)

# 6. Write a function that receives as a parameter a variable number of lists and a whole number x.
# Return a list containing the items that appear exactly x times in the incoming lists.

# def x_times(x, *lists: int) :
#     freq_list = {}
#     for list_i in lists :  # n lists
#         for index in range(len(list_i) :
#             if index in freq_list :
#                 freq_list[index] += 1
#             else :
#                 freq_list[index] = 1
#     items = []
#     for i in freq_list :
#         print(i, "appears ", freq_list[i], " times")
#         if freq_list[i] == x :
#             items.append(freq_list[i])
#     return items


# print("list of items is: ", x_times(5,
#                                    [1, 2, 3, 4],
#                                    [1, 2, 3, 4, 5, 6],
#                                    [1, 2],
#                                    [1, 2, 3, 4, 6],
#                                    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# 1, 2      apar de 5 ori
# 3, 4, 6   apar de 3 ori
# 5         apare de 2 ori
# 7,8,9,10  apar 1 data

# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element
# will be the greatest palindrome number.

def palindrome(n) :
    ogl = 0
    copy = n
    while copy != 0 :
        ogl = ogl * 10 + copy % 10
        copy = copy // 10
    return ogl == n


def tuple_palindrome(list) :
    count_palindrome = 0
    maxim = list[0]
    for i in range(len(list)) :
        if palindrome(list[i]) :
            count_palindrome += 1
            if list[i] > maxim :
                maxim = list[i]
    tuple_palindrom = (count_palindrome, maxim)
    return tuple_palindrom


# list7 = [10, 101, 1001, 202, 203, 304, 173, 1729, 1000001, 89, 989, 242]
# print(tuple_palindrome(list7))

# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set
# to True. For each string, generate a list containing the characters that have the ASCII divisible by x if the flag
# is set to True, otherwise it should contain characters that have the non-xvid ASCII code.


def ASCII_div_by_x(x: int = 1, *strings, flag: bool) :
    list_of_lists = []
    for string in strings :
        # print(string)
        if flag :
            for i in string :
                if ord(i) % x == 0 :
                    list_of_lists.append(i)
        else :
            for i in string :
                if ord(i) > 127 :
                    list_of_lists.append(i)
    print(list_of_lists)

#  9. Write a function that receives as paramer a matrix which represents the heights of the spectators in a stadium
#  and will return a list of tuples (line, column) each one representing a seat of a spectator which can't see the game.
#  A spectator can't see the game if there is at least one taller spectator standing in front of him. All the seats are
#  occupied. All the seats are at the same level. Row and column indexing starts from 0, beginning with the closest
#  row from the field.
#
# 	Example:
#
# # FIELD
#
# [[1, 2, 3, 2, 1, 1],
#
# [2, 4, 4, 3, 7, 2],
#
# [5, 5, 2, 5, 6, 4],
#
# [6, 6, 7, 6, 7, 5]]
#
# Will return : [(2, 2), (3, 4), (2, 4)]



# print(ASCII_div_by_x(2, "ana", "are", "mere", "zahar","apa", flag = True))

# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows:
# the first tuple contains the first items in the lists, the second element contains the items on the position 2 in
# the lists, etc. Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1.5, "a ") ,(5, 6, "b"), (3,7, "c")].



# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the
# tuple. Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]


def sort_tuples(*string_tuples) :
    print(sorted(string_tuples, key=lambda y: y[1][2], reverse=False))


tuples_string = [("turda", "zazar", "placinta"), ("bunica", "visine", "zootehnie"), ("FII", "pnmera", "aaaaaaa")]
sort_tuples(tuples_string)


# 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words,
# grouped by rhyme. Two words rhyme if both of them end with the same 2 letters.
#
# 	Example:
#
#   group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return
#   [['ana', 'banana'], ['carte', 'parte'],  ['arme']]
