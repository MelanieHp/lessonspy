
# function that generates a phone number of a list.

def number(q):
    for el in q:
        if el > 10 or len(q) != 10:
            return 'The list is to long or the number in the list exeeds 10.'

    else:
        str_q = ''.join(str(x) for x in q)
        number = '(' + str_q[0: 3] + ')' + '-' + str_q[3: 6] + '-' + str_q[6: 8] + '-' + str_q[8: 10]

        return number

q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(number(q))

# function that changes the letters in str.

def DNA_strand(dna):
    dict = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    return ''.join(dict[l] for l in dna if l in dict.keys())
print(DNA_strand('ATCG'))

# function that returns the sum of two least numbers.
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
numbers = [1, 10, 2, 6, 8]
print(sum_two_smallest_numbers(numbers))

# ф-я которая определяет является ли число полным квадратом.

from math import sqrt
def is_square(n):
    if n < 0:
        return False

    elif sqrt(n) == int(sqrt(n)):
        return True

    else:
        return False

print(is_square(12))

# ф-я, кооторая находит следующий целочисленный полный квадрат после переданного в качестве параметра.
from math import sqrt

def find_next_square(sq):
    if sqrt(sq) == int(sqrt(sq)):
        sq_next = (sqrt(sq) + 1) ** 2

        return int(sq_next)

    else:
        return -1

print(find_next_square(144))

# ф-я, которая принимает число и меняет его порядок от большего к меньшему.
def descending_order(num):
    str_num = str(num)
    list_num = [int(n) for n in str_num]
    list_num.sort(reverse=True)
    num_1 = int(''.join(list(map(str, list_num))))
    return num_1

print(descending_order(34267))