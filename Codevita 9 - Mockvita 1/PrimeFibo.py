'''
### Prime Fibonnaci

Given two numbers n1 and n2
1. Find prime numbers between n1 and n2, then
2. Make all possible unique combinations of numbers from the prime numbers list you found in step 1. 
3. From this new list, again find all prime numbers.
4. Find smallest (a) and largest (b) number from the 2nd generated list, also count of this list.
5. Consider smallest and largest number as the 1st and 2nd number to generate Fibonacci series respectively till
the count (number of primes in the 2nd list).
6. Print the last number of a Fibonacci series as an output


##Constraints:
    2 <= n1, n2 <= 100
    n2 - n1 >= 35

##Input Format
    One line containing two space separated integers n1 and n2.

##Output:
    Last number of a generated Fibonacci series.

##Timeout: 1

##Example:
1] Input:
    2 40
   Output:
    13158006689
'''
import math
from itertools import permutations

#Function to Check if Prime
def isPrime(n):
    if n==1:
        return False
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

i1,i2 = map(int, input().split(" "))

#First List of Prime Numbers
list1 = [i for i in range(i1, i2+1) if isPrime(i)]

#Possible Combination
comb = {int(''.join([str(x) for x in i])) for i in permutations(list1,2)}

#Second List of Prime Numbers
list2 = [i for i in comb if isPrime(i)]
c = len(list2)

print(fibo[-1])