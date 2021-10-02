# Problem 2: Given a string, say sentence=” this is crazy and fun” and a list,
# say name=[“is”, “fun”]. Now you need to capitalize on the first letter of
# every word in the given string which is not present in the list.

def capitalize(string, arr):

    words_arr = string.split()
    result = ""
    for word in words_arr:
        if word not in arr:
            word = word.capitalize()
            result += word + " "
        else:
            result += word + " "
    
    return result


print(capitalize("this is crazy and fun", ["is", "fun"]))

