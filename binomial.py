import math
def prob(n,p,N):
    
    xs= math.factorial(N) / (math.factorial(n) * math.factorial(N- n))
    return xs * (p ** n) * ((1 - p) ** (N - n))
   

def infoMeasure(n,p,N):
    return -(math.log2(prob(n,p,N)))

def sumProb(n,p,N):
    '''
    ham tinh tong xac suat
    '''
    sum=0
    for i in range(0, N + 1):
        sum+=prob(i,p,N)
    return sum
   

def approxEntropy(n,p,N):
    '''
    tinh trung binh luong tin
    '''
    avg=0
    for i in range(0, N + 1):
        avg += prob(i, p, N) * infoMeasure(i, p, N)
    return avg
