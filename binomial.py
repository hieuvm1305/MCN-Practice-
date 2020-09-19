import math
def gt(n):
    sum=1;
    for i in range(1,n+1):
        sum*=i
    return sum;

def prob(n,p,N):
    x=gt(n)
    y=gt(p)
    z=gt(n-p)
    t=float((x/(y*z))*(1/(2**n)))
    return t

def infoMeasure(n,p,N):
    k=-(math.log2(prob(n,p)))
    return k
def sumProb(n,p,N):
    '''


    '''
    sum1=0

def approxEntropy(n,p,N):
    '''

    '''
