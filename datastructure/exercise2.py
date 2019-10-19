def list_changer(input_list):
    temp=input_list.pop(4)
    input_list.insert(2,temp)
    input_list.append(temp)
    return input_list

print(list_changer([34, 54, 67, 89, 11, 43, 94]))