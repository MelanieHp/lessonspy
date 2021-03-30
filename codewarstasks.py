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