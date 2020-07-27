'''
### Digit Pairs

Given  N  three-digit  numbers,  your  task  is  to  find  bit  score  of  all  N  numbers  and  then  print
the number of pairs possiblebased on these calculated bit score

1.Rule for calculating bit score from three digit number:
From the 3-digit number,
· extract largest digit and multiply by 11 then
· extract smallest digit multiply by 7 then
· add both the result for getting bit pairs.

Note: -Bit score should be of 2-digits, if above results in a 3-digit bit score, simply ignore most significant digit.

Consider following examples:
Say, number is 286Largest digit is 8 and smallest digit is 2
So, 8*11+2*7 =102 so ignore most significant bit , So bit score = 02.
Say, Number is 123Largest digit is 3 and smallest digit is 1
So, 3*11+7*1=40, so bit score is 40.

2.Rules for making pairs from above calculated bit scores
Condition for making pairs are
· Both bit scores should be in either odd position or even position to be eligible to form a pair.
· Pairs can be only made if most significant digit are same and at most two pair can be made for a given
significant digit.

##Constraints: N<=500

##Input Format
First line contains an integer N, denoting the count of numbers.
Second line contains N 3-digit integers delimited by space

##Output: One integer value denoting the number of bit pairs.

##Timeout: 1

##Example:
1] Input: 
    8
    234 567 321 345 123 110 767 111
   Output: 3
'''

n = int(input())
lst = list(map(int, input().split(' ')))
import time
now = time.time()
evenLst =[]
oddLst = []

#Here, c is Position
#And i is Element of List
for c,i in enumerate(lst):
    #Making list of Digits
    dig = [int(x) for x in str(i)]
    #Rule 1
    elestr = list(str((max(dig)*11)+(min(dig)*7)))
    #Here If Number is 3 Digits We Will Take 2nd Digit Else We Will Take 1st Digit 
    if len(elestr)==3:
        ele = elestr[1]
    else:
        ele = elestr[0]
    #Seperating Even and Oddth Position Elements
    if c%2==0:
        evenLst.append(ele)
    else:
        oddLst.append(ele)

j=0
tmpE = evenLst
tmpO = oddLst
for i in evenLst:
    #Counting Occurence of The Digit
    cnt = tmpE.count(i)
    #Deleting All Occurences of That Integers
    tmpE = [x for x in tmpE if x!=i]
    #If Count is 2, One Pair is Possible
    if cnt==2:
        j += 1
    #If Count is More Than 2 We Have to Take Only 2 Pairs Since Rule 2
    elif cnt>2:
        j += 2

#Same for Odd List
for i in oddLst:
    cnt = tmpO.count(i)
    tmpO = [x for x in tmpO if x!=i]
    if cnt==2:
        j += 1
    elif cnt>2:
        j += 2
print(j)
end = time.time()
print(str(end-now)+" Seconds")