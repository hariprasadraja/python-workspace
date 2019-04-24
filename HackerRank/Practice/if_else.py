import sys
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

print('Weird' if N % 2 == 1 or (N in range(6, 21)) else 'Not Weird')
