
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