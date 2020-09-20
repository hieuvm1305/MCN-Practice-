import math
def prob(n,p):
    p=float(1/(2**n))
    return p

def infoMeasure(n,p):
    L=float(-(math.log2(prob(n,p))))
    return L
def sumProb(N,p):
    '''
    xac suat cua mot symbol la 1/2^k .
    Khi k cang lon, thi tong xac suat se tien ve gan gia tri 1.
    '''

    sum=0.;
    for i in range(1,N+1):
        sum += prob(i, p)
    return sum

def approxEntropy(N,p):
    '''
    voi n=1, ta co luong tin la 1 = voi luong tin trung binh la 1,p=1/2.
    con cang ve sau gia tri trng binh luong tin chi sap xi
    '''
    sum1=0.
    for i in range(1,N+1):
        sum1+=-(math.log2(prob(i,p)))
    sum1=sum1/N
    return sum1


