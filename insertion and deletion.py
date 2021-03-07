"""insertion and deletion of a number at a particular position"""

list1=[1,2,3,4,5,6]
i=int(input("enter the number to be inserted: "))
n=int(input("enter the place value in which the number to be inserted: "))
list1.insert(n,i)
print(list1)

j=int(input("enter the place value of the number to be removed: "))
del(list1[j])
print(list1)