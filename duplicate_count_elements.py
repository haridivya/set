'''
Write a program to get set values in a single line with space(including duplicate values) and find the number of duplicate values given during input and print the output set value without duplicate elements.
Sample Input:
6
1
2
1
2
3
1
Sample Output:
Duplicate Values: 3
1 2 3 
'''
n=int(input())
value=[int(input()) for i in range(0,n)]
elements=set(value)
duplicate_values=len(value)-len(elements)
print(f"Duplicate Values: {duplicate_values}")
str1=''
for j in elements:
    str1+=str(j)+' '
print(str1)
