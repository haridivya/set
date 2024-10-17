'''
Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.
'''
set1,set2=input().split(' '),input().split(' ')
values1,values2=set(set1),set(set2)
temp=''
for i in values1:
  if i in values2:
    temp+=i+' '
print(temp)
