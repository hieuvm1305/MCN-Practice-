import math

def prob(n,p,r):
     xs = math.factorial(n - 1) / (math.factorial(n - r) * math.factorial(r - 1))
    return xs * (p ** r) * ((1 - p) ** (n - r))


def infoMeasure(n,p,r):
    k = -(math.log2(prob(n, p, r)))
    return k

def sumProb(N,p,r):
    
    sum = 0
    for i in range(r, N + 1):
        sum += prob(i, p, r)
    return sum
    '''
    created by VuMinhHieu
    '''
    ''' sumProb with N = 5, r = 2, p = 0.5:  0.8125 '''
    ''' sumProb with N = 10, r = 2, p = 0.5:  0.9892578125 '''
    ''' sumProb with N = 20, r = 2, p = 0.5:  0.9999799728393555 '''

def approxEntropy(N,p,r):
    '''
    ham tinh trung binh luong tin
    '''
    avg = 0
    for i in range(r, N + 1):
        avg+= prob(i, p, r) * infoMeasure(i, p, r)
    return avg 
'''
ham tinh trung binh luong tin 
'''
''' entropy with N = 10, r = 2, p = 0.5:  2.6178901263724024 '''
''' entropy with N = 20, r = 2, p = 0.5:  2.7111142477765284 '''
''' entropy with N = 50, r = 2, p = 0.5: 2.7114687242185123 '''
