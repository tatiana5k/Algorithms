import sys
import math

#Tatiana Petkova
#COEN 279: Design & Analysis of Algorithms
#Santa Clara University
#Homework #5
#9 May 2016

#Python is dynamically typed
def countingSortforRad (A, max, d):
    
    B = [0 for x in range(0,len(A))]
    #temporary array for sorting
    
    C = [0 for x in range(0, max+1)]
    #declare and initialize counting array C
    
    print "d = " + str(d)
    for j in range(0, len(A)):
        C[int(str(A[j])[-d])] = C[int(str(A[j])[-d])] + 1
        #count the number of instances of each number in A and store the counts in C

    for i in range(1,max+1):
        C[i] = C[i] + C[i-1]
        #update counts to correlate with indecies

    print "C = " + str(C) #ready to sort

    for j in range(len(A)-1,-1,-1):     #stable algorithm
        print "j = " + str(j)
        B[C[int(str(A[j])[-d])]-1] = A[j]
        C[int(str(A[j])[-d])] = C[int(str(A[j])[-d])]-1
        print "B = " + str(B)

    #move B to A for next raxix sort iteration
    for i in range(0,len(A)):
        A[i]=B[i]

    print "A = " + str(A)
    print " "
    print " "


def radixSort (A, d):
    #calls counting sort to sort array A on digit i
    for i in range (1,d+1):
        countingSortforRad(A, 10, i)


def main():
    
    testArray = [329, 457, 657, 839, 436, 720, 355]
    
    d = len(str(max(testArray)))
    print "Input: " + str(testArray)
    print "d: " + str(d)
    
    radixSort(testArray, d)

    print "Result: " + str(testArray)

if __name__ == "__main__":
    sys.exit(main())
