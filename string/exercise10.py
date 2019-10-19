def char_counter(input_str):
    char_set={}
    for i in input_str:
        if i not in char_set:
            char_set[i]=input_str.count(i)
    
    return char_set





A=char_counter("pynativepynvepynative")
print(A)