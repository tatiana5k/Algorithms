import sys

#Python is dynamically typed
def SelectionSort(A):
    i = 0
    j = 0
    while i < len(A)-1:
        j = i
        minloc = i
        while j < len(A):
            if A[minloc] > A[j]:
                minloc = j
            j = j+1
        temp = A[minloc]
        A[minloc] = A[i]
        A[i] = temp
        i = i + 1
        print "iteration:" + str(i) + " " + str(A)
    return  A

def main():
    tatianaArray = [8, 4, 5, 3, 2, 6, 9, 8, 7]
    print "Input Array: " + str(tatianaArray)
    
    result = SelectionSort(tatianaArray)

    #print tatianaArray
    print "result: " + str(result)
    #print result


if __name__ == "__main__":
    sys.exit(main())
#makes this a standalone python script that runs by itself :)