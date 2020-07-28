'''
### Petrol Pump

A big group of students, starting a long journey on different set of vehicles need to fill petrol in their vehicles.
As group leader you are required to minimize the time they spend at the petrol pump to start the journey at
the earliest. You will be given the quantity of petrol (in litres) that can be filled in each vehicle.
There  are  two  petrol  vending  machines  at  the  petrol  pump.  You  need  to  arrange  the vehicles in such
a way that they take shortest possible time to fill all the vehicles and provide the time taken in seconds as output.
Machine vends petrol @ 1litre/second.
Assume that there is no time lost between switching vehicles to start filling petrol.

##Constraints:
    1<= Number of vehicles < 50.
    and 0 <= Quantity of petrol required in any vehicle <= 200

##Input Format
First line will provide the quantity of petrol (separated by space) that can be filled in each vehicle.

##Output: Shortest possible time to fill petrol in all the vehicles.

##Timeout: 1

##Example:
1] Input: 1 2 3 4 5 10 11 3 6 16
   Output: 31

2] Input: 25 30 35 20 90 110 45 70 80 12 30 35 85
   Output: 335
'''

#Function To Calaculate Difference Between Two Least Combinations
def calc(lst):
    s = sum(lst)
    n = len(lst)-1

    #Table to Store Results, So That Same Result is Not Calculated Again and Again
    #In Table There are n (Size of List) number of Rows
    #In Table There is Column for Every Possible Sum of List up to Max Sum
    dp = [[0 for i in range(s+1)] for j in range(n+1)]
    
    #Initializing First Column True
    for i in range(n+1):
        dp[i][0] = True
    
    #Initializing Columns of First Row as False
    for j in range(s+1):
        dp[0][j] = False
    
    #Itterating Through Table
    for i in range(n+1):
        for j in range(s+1):
            dp[i][j] = dp[i-1][j]
            if(lst[i-1]<=j):
                dp[i][j] = dp[i][j] | dp[i-1][j-lst[i-1]]
    for j in range(s//2, -1, -1):
        if dp[n][j]==True:
            diff = s-(2*j)
            break
    return diff

lst = list(map(int, input().split(' ')))
diff = calc(lst)

#Least Sum From Two Combinations
min_p = (sum(lst)-diff)//2

#Largest Sum From Two Combination
max_p = min_p + diff
print(max_p)