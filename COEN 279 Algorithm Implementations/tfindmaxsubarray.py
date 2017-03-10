import sys
import math
import time

def FindMaxSubarrayR (A, low, high):
    mid = (low+high)/2
    
    if high == low:
        return low, high, A[low]
    
    else:
        if (high - low) < 6:
            return FindMaxSubarrayBF(A,low,high)
    

    Llow, Lhigh, Lsum = FindMaxSubarrayR(A,low,mid)
    Rlow, Rhigh, Rsum = FindMaxSubarrayR(A,mid+1,high)
    Clow, Chigh, Csum = FindMaxCrossingSubarray(A,low,mid,high)

    if Lsum >= Rsum and Lsum >= Csum:
        return Llow, Lhigh, Lsum

    else:
        if Rsum >= Lsum and Rsum >= Csum:
            return Rlow, Rhigh, Rsum

    return Clow, Chigh, Csum

def FindMaxCrossingSubarray(A, low, mid, high):
    Lsum = float("-inf")
    sum = 0
    Lindex = 0
    Rindex = 0
    
    for i in range(mid, low, -1):
       
        sum = sum + A[i]
        if sum > Lsum:
            Lsum = sum
            Lindex = i

    Rsum = float("-inf")
    sum = 0

    for j in range(mid+1, high):
        sum = sum + A[j]
        if sum > Rsum:
            Rsum = sum
            Rindex = j

    return Lindex, Rindex, Lsum+Rsum

def FindMaxSubarrayBF (A, low, high):
    maxsum = A[0]
    i = 0
    j = 0
    maxi = 0
    maxj = 0
    for i in range(0, high):
        sum = A[i]
        for j in range(i+1, high):
            sum = sum + A[j]
            if sum > maxsum:
                maxsum = sum
                maxi = i
                maxj = j
    return maxi, maxj, maxsum

def main():
    
    tatianaArray = [1, -5, 10, 200, -100, 55, 2, 3, 44, 9, 8, 7, 6, 13, 15, 17, -2, -6, 1, 0, -1, 500, 4, -2, -1000, 10, 200, -100, 55, 2, 3, 44, 9, 8, 7, 10, 200, -100, 55, 2, 3, 44, 9, 8, 7, 1, 1, 1, 30, 33, -44, -50, -5000, 5, 55, 155, 66, 166]
    
    flag = 0
    i=1
 
    while i < len(tatianaArray) and flag == 0:
        print "n = " + str(i+1)
        
        start = time.clock()
        result = FindMaxSubarrayBF(tatianaArray,0,i)
        end = time.clock()
        
        BFruntime = end - start
        print " Brute Force Runtime: " + str(BFruntime)
        #print " Brute Force Result: " + str(result)

        
        start = time.clock()
        result = FindMaxSubarrayR(tatianaArray,0,i)
        end = time.clock()
        Rruntime = end - start
        print " Recursive Runtime: " + str(Rruntime)
        #print " Recursive Result: " + str(result)
    
    
        Delta = BFruntime - Rruntime
        print " Delta " + str(Delta)
        
        if( Rruntime < BFruntime ):
            print "Winner: Recursive"
            flag = 1
        
        if( BFruntime < Rruntime):
            print "Winner: Brute Force"
    
        i = i + 1

if __name__ == "__main__":
    sys.exit(main())
