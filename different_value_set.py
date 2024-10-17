'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.
'''
set1,set2=input().split(' '),input().split(' ')
values1={int(i) for i in set1}
values2={int(i) for i in set2}
duplicates=''
for i in values1:
    if i in values2:
        duplicates+=str(i)+' '
print(duplicates)
