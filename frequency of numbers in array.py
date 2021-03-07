arr=[]
dict={}
i=int(input("enter the number of elements u want:"))
for j in range(0,i):
    arr.append(input("enter the items:"))
    
print("printing the list items:")
for i in arr:
    print(i,end=" ")
for k in arr:
    if k in dict:
        dict[k]+=1
    else:
        dict[k]=1
print("\n number:frequency")
for key,value in dict.items():

    print(f"\n{key}:{value}")