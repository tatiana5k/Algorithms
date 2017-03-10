import sys

#Python is dynamically typed
def MergeSort(A):
       return  A

def main():
    tatianaArray = [8, 4, 5, 3, 2, 6, 9, 8, 7]
    print "Input Array: " + str(tatianaArray)
    
    result = MergeSort(tatianaArray)
    
    #print tatianaArray
    print "result: " + str(result)
#print result


if __name__ == "__main__":
    sys.exit(main())
#makes this a standalone python script that runs by itself :)