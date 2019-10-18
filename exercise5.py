def findDigitsCharsSymbols(in_str:str):

    numb=0
    lowercase=0
    upercase=0
    spesymbl=0
    for i in in_str:
        if i.islower():
            lowercase+=1
        elif i.isupper():
            upercase+=1
        elif i.isnumeric():
            numb+=1
        else:
            spesymbl+=1
        
    print("number=",numb,'  lower case=',lowercase,'  upper case= ',upercase,'   special symbol=',spesymbl)



findDigitsCharsSymbols('P@#yn26at^&i5ve')
