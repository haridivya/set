'''
SET
Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
Note: There is trailing space at the end of output
'''
no_input=int(input())
temp=''
set1=[]
for i in range(0,no_input):
    set1.append(int(input())) 
set1.sort()
for i in set1:
    temp+=str(i)+' '
print(temp)
