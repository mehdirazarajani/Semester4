import closed
from prettytable import PrettyTable

def tableFunction(a,b,n,list, trueVal):
    trap = 0
    simp13 = 0
    simp38 = 0
    bolle = 0

    trueVal = str(trueVal)
    trueVF = float(trueVal)

    ni = int(n)
    ni = ni - 1

    t = PrettyTable(['Function', 'Approximated Value', 'Error'])
    trap = closed.evalTrap(a, b, list, trueVal, n)
    t.add_row(['Trapezoid', trap, abs(trueVF - trap)])

    if (not (ni < 2 or ni % 2 != 0)):
        # print("Simp")
        simp13 = closed.evalSimpson(a, b, list, trueVal, n)
        t.add_row(['1/3rd Simpson', simp13, abs(trueVF - simp13)])
        # print(simp13)

    if (not (ni < 3 or ni % 3 != 0)):
        # print("Simp38")
        simp38 = closed.eval3Simpson(a, b, list, trueVal, n)
        t.add_row(['3/8th Simpson', simp38, abs(trueVF - simp38)])
        # print(simp38)
    if (not (ni < 4 or ni % 4 != 0)):
        # print("Bolle")
        bolle = closed.evalBool(a, b, list, trueVal, n)
        t.add_row(['Bolle', bolle, abs(trueVF - bolle)])
        # print(bolle

    print(t)

trueVal = input("Enter the true value: ")
a = input("Enter the lower limit: ")
b = input("Enter the upper limit: ")
n = input("Enter the number of data points to use: ")

wholeList = []

for i in range(int(n)):
    wholeList.append(float(input("Enter the data point: ")))

tableFunction(a, b, str(len(wholeList)), wholeList, trueVal)
