# 1. Find The greatest common divisor of multiple numbers read from the console.

def GCD(a, b):
    while a is not b :
        if a > b:
            a = a - b
        else:
            b = b - a
    return b

def GCD_multiple_numbers():
    # creating a list of numbers from console input
    # split() converts a strig to a list
    # map returns a MAP OBJECT which is a generator object
    print('GCD of multiple numbers (from console): ')
    list_of_numbers = list(map(int, input().split()))
    # calculating GCD of created list by parsing the list and calculate the GCD at every step
    res = GCD(list_of_numbers[0], list_of_numbers[1])
    for i in range(2, len(list_of_numbers)):
        res = GCD(res, list_of_numbers[i])
    return res

# 2. Write a script that calculates how many vowels are in a string.

def numberOfVowels():
    print('Number of vowels in string: ')
    string = input()
    vowel_count = 0
    for i in string :
        if i in "aAeEiIoOuU":
            vowel_count = vowel_count + 1
    print('vowel_count = ', vowel_count)

# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.

def numberOfOccurences():
    print('Number of occurences of a in b. Input string')
    a, b = input().split()
    print('String a is: ', a)
    print('String b is: ', b)
    print('Number of occurences of a in b: ', b.count(a))

# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

def stringFormatting(): # de completat
    print('Text to change from UpperCamelCase to lowercase_with_underscore: ')
    a = str(input())
    b = [a[0].lower()]
    for i in a[1:] :
        if i.isupper():
            b.append('_')
            b.append(i.lower())
        else :
            b.append(i)
    print(''.join(b))


# 5. Given a square matrix of characters write a script that prints the string obtained by going through the matrix
# in spiral order (as in the example):
# firs      1  2  3  4    =>   first_python_lab
# n_lt      12 13 14 5
# oba_      11 16 15 6
# htyp      10 9  8  7

def spiralParsing(m, n, a) :
    k = 0
    l = 0
    while k < m and l < n :
        for i in range(l, n) :
            print(a[k][i], end='')
        k += 1
        for i in range(k, m) :
            print(a[i][n - 1], end='')
        n -= 1
        if k < m :
            for i in range(n - 1, (l - 1), -1) :
                print(a[m - 1][i], end='')
            m -= 1
        if l < n :
            for i in range(m - 1, k - 1, -1) :
                print(a[i][l], end='')
            l += 1


def spiralParse():
    matrix = [['f', 'i', 'r', 's'], ['n', '_', 'l', 't'], ['o', 'b', 'a', '_'], ['h', 't', 'y', 'p']]
    row = len(matrix)
    col = len(matrix[0])
    spiralParsing(row, col, matrix)

#  6. Write a function that validates if a number is a palindrome.

def palindrome(string):
    if len(string) == 1:
        return True
    elif string[0] != string[-1]:
        return False
    # calls palindrome() for the string obtained by removing the first and last letter of the current string
    return palindrome(string[1:-1])

def palindromeFunction() :
    print('Check if console number is a palindrome. Input: ')
    number = input()
    val = palindrome(number)
    if val :
        print(number, ' is a palindrome')
    else :
        print(number, 'is NOT a palindrome')

# 7. Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function
# will # return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only
# the first number that is found.

def numberExtractor():
    string = input()
    i = 0
    found_first = 0
    new_string = []
    while found_first != 2 and i < len(string):
        if found_first == 1 and string[i] not in "0123456789":
            found_first = 2
        if string[i] in "0123456789":
            new_string.append(string[i])
            found_first = 1
        i += 1
    if found_first == 0:
        print('Not Found')
    else:
        print(''.join(new_string))


# 8.Write a function that counts how many bits with value 1 a number has. For example for number 24,
# the binary format is 00011000, meaning 2 bits with value "1"

def numberOf1Bits():
    print('Check how many 1 bits a number has. Number: ')
    number = int(input())
    count = 0
    while number != 0 :
        if number % 2 :
            count = count + 1
        number = number // 2
    print(count, 'number of 1 bits.')

# 9. Write a functions that determine the most common letter in a string. For example if the string
# is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters
# (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

def mostFrequentLetterApparition():
    string = input()
    freq_list = {}
    for i in string:
        if i != ' ':
            if i in freq_list:
                freq_list[i] += 1
            else:
                freq_list[i] = 1
    maxim = 0
    for index in freq_list:
        if freq_list[index] > maxim:
            maxim = freq_list[index]
    print(maxim)


# 10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.

def wordCount():
    my_string = input()
    count = 1
    for i in range(0, len(my_string)):
        if my_string[i] == ' ' and my_string[i - 1] != ' ':
            count += 1
    print(count)


def main():
    # print(GCD_multiple_numbers())            # 1
    # print(numberOfVowels())                  # 2
    # print(numberOfOccurences())              # 3
    # print(stringFormatting())                # 4
    # print(spiralParse())                     # 5
    print(palindromeFunction())              # 6
    # print(numberExtractor())                 # 7
    # print(numberOf1Bits())                   # 8
    # print(mostFrequentLetterApparition())    # 9
    # print(wordCount())                       # 10


if __name__ == "__main__":
    main()


