def char_frequency(string):
    result = ""
    i = 1
    while i < len(string):
        if string[i-1] != string[i]:
            result += string[i-1] + str(string.count(string[i-1]))
        i += 1
    
    result += string[-1] + str(string.count(string[-1]))

    return result


print(char_frequency("prepinsta"))

