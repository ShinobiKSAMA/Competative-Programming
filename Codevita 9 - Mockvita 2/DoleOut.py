'''
### Dole Out Cadbury

You are a teacher in reputed school. During Celebration Day you were assigned a task to distribute Cadbury  such
that  maximum  children  get  the  chocolate.  You  have  a  box  full  of  Cadbury  with different width and height.
You can only distribute largest square shape Cadbury. So if you have a Cadbury of ength 10 and width 5,
then you need to break Cadbury in 5X5 square and distribute to first child and then remaining 5X5 to next in queue

##Constraints: 0<P<Q<1501 and 0<R<S<1501

##Input Format
First line contains an integer P that denotes minimum length of Cadbury in the box
Second line contains an integer Q that denotes maximum length of Cadbury in the box
Third line contains an integer R that denotes minimum width of Cadbury in the box
Fourth line contains an integer S that denotes maximum width of Cadbury in the box

##Output: Print total number of children who will get chocolate.

##Timeout: 1

##Example:
1] Input: 
    5
    7
    3
    4
   Output: 24
'''

p = int(input())
q = int(input())
r = int(input())
s = int(input())

def cPCB(l,b):
    c = 0
    wl,wb = l,b
    
    #If It Exist in Dictionary
    if (wl,wb) in cD:
        c = cD[(wl,wb)]
    
    #If Not
    else:
        while(wl!=0 or wb!=0):
            
            #If New Piece Exist add it in Count
            if (wl,wb) in cD:
                c += cD[(wl,wb)]
                break
            lr = max(wl,wb)
            sr = min(wl,wb)
            if (lr%sr==0):
                c += lr//sr
                break
            
            #If New Piece Doesn't Exist Create New Piece
            else:
                wl = sr
                wb = lr-sr
                c += 1
        
        #Add Non Existing Value in Dictionary
        cD[(l,b)] = c
        cD[(b,l)] = c
    return c
        
total = 0
cD = dict() #Count Dictionary
for i in range(p,q+1):
    for j in range(r,s+1):
        total += cPCB(i,j)
print(total)