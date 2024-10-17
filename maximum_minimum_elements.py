'''
Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
set_elements=input().split(' ')
values=[int(i) for i in set_elements]
print(f"Maximum: {max(values)}")
print(f"Minimum: {min(values)}")
