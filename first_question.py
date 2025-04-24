l=[1284, 145612, 5671, 23, 1765, 594]



for i in range(1,len(l)-1):
    num=list(str(l[i]))[-2]
    prev_num=list(str(l[i-1]))[-2]
    if(num>prev_num):
        # temp=l[i]
        # num=
        # l[i-1]=num
        
        temp=l[i-1]
        l[i-1]=l[i]
        l[i]=temp
    
        

print(l)

[594, 1284, 5671, 1765, 23, 145612]
