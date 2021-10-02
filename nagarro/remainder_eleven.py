# return the remainder when a large number is divided by 11.
# divisibility rule of 11:
# sum all the odd digits and sum all the even digits and the difference of these sum
# if 0 or divisible by 11 then div by eleven


from typing import final


def divisibility_by_eleven(string):
    even = []
    odd = []
    counter = 1
    for digit in string:
        if counter % 2 == 0:
            even.append(int(digit))
        else:
            odd.append(int(digit))
        counter += 1
    final_num = abs(sum(even) - sum(odd))
    if final_num % 11 == 0:
        return 0
    return final_num % 11


print(divisibility_by_eleven("13589234356546756"))