# Problem Statement:  Given a positive whole number n, 
# find the smallest number which has the very same digits existing 
# in the whole number n and is greater than n. 
# In the event that no such certain number exists, return – 1. 
#  Note that the returned number should fit in a 32-digit number, 
# if there is a substantial answer however it doesn’t fit in a 32-bit number, return – 1.

def next_greater_number(n):
    ascend = []
    for digits in str(n):
        ascend.append(int(digits))
    ascend = reversed(sorted(ascend))

    result = ""
    for digit in ascend:
        result = result + str(digit)
    
    if int(result) <= n:
        return -1
    else:
        return result


print(next_greater_number(21))