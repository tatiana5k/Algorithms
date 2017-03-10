import sys

#Tatiana Petkova
#COEN 279: Design & Analysis of Algorithms
#Santa Clara University
#Homework #5
#9 May 2016

#Python is dynamically typed
def countingSort (A, B, max):
    
    print "max = " + str(max)
    
    C = [0 for x in range(0, max+1)]
    #declare and initialize counting array C
    
    print "C length =" + str(len(C))

    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
        #count the number of instances of each number in A and store the counts in C

    for i in range(1,max+1):
        C[i] = C[i] + C[i-1]
        #update counts to correlate with indecies

    print "C = " + str(C) #ready to sort

    for j in range(len(A)-1,-1,-1):     #stable algorithm
        print "j = " + str(j)
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]]-1
        print "B = " + str(B)
        print "C = " + str(C)
                   
def main():
    
    testArray = [6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
    
    tmax = max(testArray)

    result = [0 for x in range(0,len(testArray))]
    
    countingSort(testArray, result, tmax)
    
    print "Input: " + str(testArray)
    print "Max: " + str(tmax)
    print "Result: " + str(result)

if __name__ == "__main__":
    sys.exit(main())
