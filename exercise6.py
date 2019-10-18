def StrMixer(str1,str2):
    answer=''
    str2_index=-1

    for i in str1:
        answer+=i
        if len(str2)> -str2_index:
            answer+=str2[str2_index]
    if len(str2)>len(str1):
        final_ader=len(str2)-len(str1)
        answer+=str2[final_ader:]
    return answer


print(StrMixer("Pynative", "Website"))


