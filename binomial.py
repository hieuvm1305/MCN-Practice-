import math
def gt(n):
    tich=1;
    for i in range(1,n+1):
        tich*=i
    return tich;

def prob(n,p,N):
    x=gt(N)
    y=gt(n)
    z=gt(N-n)
    p=float((x/(y*z))*(1/(2**n)))
    return p

def infoMeasure(n,p,N):
    k=-(math.log2(prob(n,p,N)))
    return k
def sumProb(n,p,N):
    '''
    created by VuMinhHieu_18020513
    ham tinh tong xac suat
    '''
    sum=0
    for i in range(1, N + 1):
        sum+=prob(i,p,N)
    return sum

def approxEntropy(n,p,N):
    '''
    tinh trung binh luong tin
    '''
    avg=0
    for i in range(1,N+1):
        avg+=infoMeasure(i,p,N)
    avg=avg/N
    return avg
