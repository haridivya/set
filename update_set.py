'''
Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''
set1=input().split(' ')
set2=input().split(' ')
set1.extend(set2)
temp=set(set1)
x=list(temp)
x.sort()
output_values=''
for i in x:
    output_values+=i+' '
print(output_values)

