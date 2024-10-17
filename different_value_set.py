'''
Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
Note: There are trailing spaces at the end of output.
'''
set1=input().split(' ')
set2=input().split(' ')
values1={int(i) for i in set1}
values2={int(i) for i in set2}
