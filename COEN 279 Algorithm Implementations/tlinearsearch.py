import sys

#Python is dynamically typed
def LinearSearch(A,v):
    i = 0
    while i < len(A):
        if A[i] == v:
            return i
        i = i + 1
    return  "NIL"

def main():
    tatianaArray = [8, 4, 5, 3, 2, 6, 7, 8, 9]

    result = LinearSearch(tatianaArray, 55)

    print "Input Array: " + str(tatianaArray)
    #print tatianaArray
    print "I found: " + str(result)
    #print result


if __name__ == "__main__":
    sys.exit(main())
#makes this a standalone python script that runs by itself :)