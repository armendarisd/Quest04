def my_string_index(param_1, param_2):
    index = 0
    while(index < len(param_1)):
        if(param_1[index] == param_2):
            return index
        index += 1
    return -1

    