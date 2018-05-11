from sympy import *
from math import *
from prettytable import PrettyTable
import numpy as np
import closed

x=Symbol('x')
function = input("Enter the function to integrate: ")
a = input("Enter the lower limit: ")
b = input("Enter the upper limit: ")
n = input("Enter the number of data points to use: ")

print("\n------------------------\n")

p=integrate(function,x)
print('Symbolic Function used to find calculate true value: ' + str(p))

print("\n------------------------\n")

trueV = integrate(function,(x,a,b))
trueVF = eval(str(trueV))

print('True value: ' + str(trueVF))

print("\n------------------------\n")

print('Closed Methods\n')

trap = 0
simp13 = 0
simp38 = 0
bolle = 0

t = PrettyTable(['Function', 'Approximated Value', 'Error'])

trap = closed.evalTrap(a, b, function, str(trueV), n)
t.add_row(['Trapezoid', trap, abs(trueVF - trap)])

ni = int(n)
ni = ni - 1

if ( not (ni < 2 or ni % 2 != 0)):
	simp13 = closed.evalSimpson(a, b, function, str(trueV), n)
	t.add_row(['1/3rd Simpson', simp13, abs(trueVF - simp13)])

if ( not (ni < 3 or ni % 3 != 0)):
	simp38 = closed.eval3Simpson(a, b, function, str(trueV), n)
	t.add_row(['3/8th Simpson', simp38, abs(trueVF - simp38)])

if ( not (ni < 4 or ni % 4 != 0)):
	bolle = closed.evalBool(a, b, function, str(trueV), n)
	t.add_row(['Bolle', bolle, abs(trueVF - bolle)])

print(t)
