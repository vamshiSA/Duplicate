def fun(x):
    repeated=[]
    size=len(x)
    for i in range(size):
        k=i+1;
        for j in range(k,size):
            if (x[i]==x[j] and x[i] not in repeated):
                repeated.append(x[i])
    return repeated;
                
print("the duplicate elements in the list are given below")
list=[20,20,10,10]
result=[]
result=fun(list)
print(result)
