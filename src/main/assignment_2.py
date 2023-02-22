import numpy as np

def neville():

    x = 3.7
    xVals = [3.6, 3.8, 3.9]
    yVals = [1.675, 1.436, 1.318]
    y = yVals.copy()
    numData = len(xVals)

    for k in range (1,numData):
        for i in range(numData-k):
            y[i] = ((x - xVals[i+k])*y[i] + (xVals[i] - x)*y[i+1])/ \
            (xVals[i]-xVals[i+k])
            return(y[0])

def newtonsForward():
    degree1 = (25.3913 - 23.5492) / (7.4 - 7.2)
    print(degree1)
    degree2 = (((25.3913 - 23.5492) / (7.4 - 7.2))*(-0.7183802816901438))/((25.3913 - 23.5492) / (7.4 - 7.2))
    print(degree2)
    degree3 = (((25.3913 - 23.5492) / (7.4 - 7.2))*(-0.12461196085345332))/((25.3913 - 23.5492) / (7.4 - 7.2))
    print(degree3)

    approx = 24.47718457889519
    print()
    print(approx)


if __name__ == "__main__":
    print(neville())
    print()
    newtonsForward()
    print("\n")
    print("couldnt get")
    print("couldnt get")
    print("couldnt get")
    print("couldnt get")
