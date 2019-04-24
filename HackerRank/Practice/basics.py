# print Hello world
import sys
print("Hello, World!")


"""
Task
Read two integers from STDIN and print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers(first - second).
The third line contains the product of the two numbers.

Input Format:
The first line contains the first integer, . The second line contains the second integer, .

Output Format:
Print the three lines as explained above.

Sample Input 0
3
2

Sample Output 0
5
1
6
"""

a = int(input(""))
b = int(input(""))
print(a + b)
print(a - b)
print(a * b)


"""
divide two number and print one result in interger and another one in float

"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(int(a/b))
    print(float(a/b))

"""
Given an integer, , perform the following conditional actions:

If is odd, print Weird
If is even and in the inclusive range of 2 to 5, print Not Weird
If is even and in the inclusive range of 6 to 20, print Weird
If is even and greater than 20, print Not Weird

Input Format:
A single line containing a positive integer, .

Output Format:
Print Weird if the number is weird
otherwise, print Not Weird.
"""
N = int(input())
if (N % 2) == 1:
    print("Weird")
    sys.exit(0)

if (N > 20) or (2 < N < 5):
    print("Not Weird")
else:
    print("Weird")

"""
We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.Source

Task
You are given the year, and you have to write a function to check if the year is leap or not.

Note that you have to complete the function and remaining code is given as template.

Input Format

Read y, the year that needs to be checked.



Output Format

Output is taken care of by the template. Your function must return a boolean value (True/False)

"""


def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


year = int(input())

"""
Read an integer N.

Without using any string methods, try to print the following:

123....N

Note that "" represents the values in between.

"""

n = int(input())
print(*range(1, n), end='')

#  (OR)

if __name__ == '__main__':
    n = int(input())
    i = 1
    while (n+1) > i:
        print(i, end='')
        i += 1
