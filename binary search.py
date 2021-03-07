"""binary search"""
def bin_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    
    while low<=high:
        mid=(low+high)//2
        
        if list1[mid]<n:
            low=mid+1
        elif list1[mid]>n:
            high=mid-1
        else:
            return mid
    return-1
    
list1 = [22,34,55,77,87,11,100,56,98]

n=int(input("enter the number for binary search:"))

result=bin_search(list1,n)

if result!=-1:
    print("Element is present at index:",str(result))
else:
    print("element is not present")