import numpy as np
from matplotlib import pyplot as plt

p = 0.5
allSamples = []

def sumOfGeometricProbabilityFunctions(p,howMany):         #To concrete Sub Intervals
    sum = 0
    for i in range(1,howMany+1):
        sum+= geometricProbabilityFunction(i,p)
    return sum

def geometricProbabilityFunction(x,p):
    return ((1-p)**(x-1))*p

def createProbabilitySubIntervals(p,f): 
    probabilitySubIntervals = []
    for i in range(1,55):               # After n>55 the function return 0 so, it is enough to select n = 55
        if (i==1):
            probabilitySubIntervals.append([0,geometricProbabilityFunction(1,p)])
        else:
            probabilitySubIntervals.append([sumOfGeometricProbabilityFunctions(p,i-1),sumOfGeometricProbabilityFunctions(p,i)])
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
     probabilitySubIntervals = createProbabilitySubIntervals(p,geometricProbabilityFunction)
     u = np.random.rand()
     probability = findTheCorrespondingProbability(u,probabilitySubIntervals)
     allSamples.append(probability)
     
print("PROBABILITY SUB INTERVALS")
print("**************************")
print(probabilitySubIntervals)

plt.figure()
plt.hist(allSamples,20,density=True)
plt.show()


