'''
 Write a program to get input in a single line separated by space and print the values of set in single line separated by space.
Sample Input:
3 1 5 4 2
Sample Output:
1 2 3 4 5
Note: There is no trailing space at the end of output.
'''
input_elements=input().split(' ')
input_values=[int(i) for i in input_elements]
input_values.sort()
set1=set(input_values)
temp=''
for i in set1:
    temp+=str(i)+' '
print(temp)
