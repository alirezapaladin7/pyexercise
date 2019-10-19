
def list_slicer(input_list):
    lengh=len(input_list)//3
   # l1=l2=l3=[]
    l1=input_list[0:lengh]
    l2=input_list[lengh:(2*lengh)]
    l3=input_list[(2*lengh):]

    l1.reverse()
    l2.reverse()
    l3.reverse()

    print(l1)
    print(l2)
    print(l3)



list_slicer([11, 45, 8, 23, 14, 12, 78, 45, 89,3,5,5])
