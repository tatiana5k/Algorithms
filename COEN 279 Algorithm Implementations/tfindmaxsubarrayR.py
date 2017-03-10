import sys
import math

def FindMaxSubarray (A, low, high):
    mid = (low+high)/2
    
    if high == low:
        return low, high, A[low]
    
    else:
        #mid = math.floor((low+high)/2)
        #mid = (low+high)/2
        #print "A:" + str(A) + " low:" + str(low) + " mid:" + str(mid) + " high:" + str(high)
        Llow, Lhigh, Lsum = FindMaxSubarray(A,low,mid)
        Rlow, Rhigh, Rsum = FindMaxSubarray(A,mid+1,high)
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

def main():
    tatianaArray = [1, -5, 10, 200, -100, 55, 2, 3, 44, 9, 8, 7, 6, 13, 15, 17, -2, -6, 1, 0, -1, 500, 4, -2, -1000]
    print "Input Array: " + str(tatianaArray)

    result = FindMaxSubarray(tatianaArray, 0, len(tatianaArray)-1)

    #print tatianaArray
    print "(Lindex, Rindex, maxsum): " + str(result)
    #print result


if __name__ == "__main__":
    sys.exit(main())
#makes this a standalone python script that runs by itself :)