'''
 Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.
'''
elements=input().split(' ')
delete_ele=int(input())
set_value=[int(i) for i in elements]
set_value.remove(delete_ele)
str1=''
for i in set_value:
    str1+=str(i)+' '
print(str1)

