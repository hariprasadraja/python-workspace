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
N = int(input())
if (N % 2) == 1:
    print("Weird")
    sys.exit(0)

if (N > 20) or (2 < N < 5):
    print("Not Weird")
else:
    print("Weird")
