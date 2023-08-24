import numpy as np
from matplotlib import pyplot as plt
from math import factorial

n = 10
p = 0.5
allSamples = []
def sumOfBinomialProbabilityFunctions(n,p,howMany):    #We will use it for constructing probability sub intervals
    sum = 0
    for i in range(howMany):
        sum+= binomialProbabilityFunction(i,n,p)
    return sum
        
def binomialProbabilityFunction(x,n,p):               #Our binomial probability function
    if(x>n):
        return 0
    else:
        combination  = factorial(n)/(factorial(n-x)*factorial(x))
        return combination * (p**x) * (1-p)**(n-x)
    
def createProbabilitySubIntervals(n,p,f): 
    probabilitySubIntervals = []
    for i in range(0,n+1):
        if(i == 0):
            probabilitySubIntervals.append([i,f(i,n,p)])
        else:
            probabilitySubIntervals.append([sumOfBinomialProbabilityFunctions(n,p,i),sumOfBinomialProbabilityFunctions(n,p,i+1)])
    return probabilitySubIntervals

def findTheCorrespondingProbability(u,probabilitySubIntervals):
    for i in range(len(probabilitySubIntervals)):
        if(i == len(probabilitySubIntervals)-1):
            if((float(probabilitySubIntervals[i][0]) <= u) and (u < float(probabilitySubIntervals[i][1]))):
                return i
                break
        elif((float(probabilitySubIntervals[i][0]) <= u) and (u < float(probabilitySubIntervals[i][1]))):
            return i
            break

for j in range(1000):
     probabilitySubIntervals = createProbabilitySubIntervals(n,p,binomialProbabilityFunction)
     u = np.random.rand()
     probability = findTheCorrespondingProbability(u,probabilitySubIntervals)
     allSamples.append(probability)
     
print("PROBABILITY SUB INTERVALS")
print("**************************")
print(probabilitySubIntervals)

plt.figure()
plt.hist(allSamples,20,density=True)
plt.show()




    
    
    