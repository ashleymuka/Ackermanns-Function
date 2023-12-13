
'''
Author: Ashley Muka
Assignment Title: Ackermann's Function
Assignment Description:implement a Python function ackermann(m,n)
that calculates Ackermann's function. 
Due Date: 11/03/2023
Date Created:11/01/2023
Date Last Modified:11/01/2023

'''


#process
def ackermann(m, n):
    if m == 0:
        return n + 1

    elif n == 0 and m > 0:
        return ackermann(m-1, 1)

    else:
        return ackermann(m-1, ackermann(m, n-1))

if __name__ == "__main__":
#input
    mValues = [0,1,2,3]
    nValues = [0,1,2,3]

    for m in mValues:
        for n in nValues:
            result = ackermann(m, n)
#output           
            print(f' Ackermann({m}, {n}) = {result}')
