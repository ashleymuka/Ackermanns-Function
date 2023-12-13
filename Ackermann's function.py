
'''
Description:implement a Python function ackermann(m,n)
that calculates Ackermann's function. 
'''

def ackermann(m, n):
    if m == 0:
        return n + 1

    elif n == 0 and m > 0:
        return ackermann(m-1, 1)

    else:
        return ackermann(m-1, ackermann(m, n-1))

if __name__ == "__main__":

    mValues = [0,1,2,3]
    nValues = [0,1,2,3]

    for m in mValues:
        for n in nValues:
            result = ackermann(m, n)
     
            print(f' Ackermann({m}, {n}) = {result}')
