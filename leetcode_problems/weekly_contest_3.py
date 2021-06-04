# def check_words(first, second, target):
#     first_num = ""
#     second_num = ""
#     target_num = ""
#     for letters in first:
#         order = ord(letters)-97
#         first_num = first_num + str(order)

#     for letters in second:
#         order = ord(letters)-97
#         second_num = second_num + str(order)

#     for letters in target:
#         order = ord(letters)-97
#         target_num = target_num + str(order)

#     summation = int(first_num) + int(second_num)
#     if summation == int(target_num):
#         return True
#     else:
#         return False



def max_val(s, n):
    digits = []
    if s[0] != '-':
        for num in range(len(s)):
            if int(s[num]) < n:
                s = s[:num] + str(n) + s[num:]
                return s
            elif int(s[num]) == n:
                for sec_largest in range(num, len(s)):
                    if sec_largest < n:
                        s = s[:num] + str(n) + s[num:]
                        return s
                    elif sec_largest == len(s)-1:
                        s = s + str(n)
                        return s


    for num in range(1,len(s)):
        if int(s[num]) > n:
            s = s[:num] + str(n) + s[num:]
            return s
        elif num == len(s)-1:
            s = s + str(n)
            return s




print(max_val('-132', 3))

    
