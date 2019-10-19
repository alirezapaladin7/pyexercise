def list_intersection(list1,list2):
    intersetion=[]
    for i in list1:
        if i in list2:
            intersetion.append(i)
            list1.remove(i)
    
    print (intersetion)
    print(list1)
    print(list2)




First=[2, 3, 4, 5, 6, 7, 8]
Second=[4, 9, 16, 25, 36, 49, 64]
list_intersection(First,Second)