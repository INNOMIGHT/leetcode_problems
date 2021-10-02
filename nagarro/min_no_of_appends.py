# Given a string S and two positive integers X and Y,
# the task is to find the minimum number of operations required to obtain the original string.
# In each operation, append X or Y characters from the end of the string to the front
# of the string respectively in each operation.

def min_no_of_appends(string, x, y):

    count = 1
    tmp_str = string
    for i in string:
        
        x_str = tmp_str[-x:] + tmp_str[:-x]
        print(x_str)
        if x_str == string:
            return count
        else:
            count += 1
        
        y_str = x_str[-y:] + x_str[:-y]
        print(y_str)
        if y_str == string:
            return count
        else:
            count += 1
        tmp_str = y_str


print(min_no_of_appends("AbcDef", 1, 2))
            
        