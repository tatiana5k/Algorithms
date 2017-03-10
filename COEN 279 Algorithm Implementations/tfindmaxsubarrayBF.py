import sys

#Python is dynamically typed
def FindMaxSubarrayBF (A):
    maxsum = A[0]
    i = 0
    j = 0
    for i in range(0, len(A)):
        sum = A[i]
        for j in range(i+1, len(A)):
            sum = sum + A[j]
            if sum > maxsum:
                maxsum = sum
                maxi = i
                maxj = j
    return maxi, maxj, maxsum


def main():
    tatianaArray = [1, -5, 10, 200, -100, 55, 2, 3, 44, 9, 8, 7, 6, 13, 15, 17, -2, -6, 1, 0, -1, 500, 4, -2, -1000]
    print "Input Array: " + str(tatianaArray)
    
    result = FindMaxSubarrayBF(tatianaArray)

    #print tatianaArray
    print "(maxi, maxj, maxsum): " + str(result)
    #print result


if __name__ == "__main__":
    sys.exit(main())
#makes this a standalone python script that runs by itself :)