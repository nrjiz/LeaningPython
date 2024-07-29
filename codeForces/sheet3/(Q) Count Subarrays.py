  nbTestCases = int(input())
def nbOfSubarrays(my_list):
    counter =0
    length =1
    for i in range(len(my_list)):
        counter+=length
        if i<len(my_list)-1 and my_list[i]<=my_list[i+1]:
            length+=1
        else:
            length=1

    return counter

while (nbTestCases>0): 

    
    listLength = int(input())
    input_list = list(map(int,input().split()))
    
    print(input_list)
    count = nbOfSubarrays(input_list)
    print(count)


    



    nbTestCases-=1
