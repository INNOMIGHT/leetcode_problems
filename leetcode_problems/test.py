my_dict = {
    1: 4,
    2: 3,
    6: 7,
}

for key, value in my_dict.items():
    if max(my_dict.values()) == value:
        print(key)