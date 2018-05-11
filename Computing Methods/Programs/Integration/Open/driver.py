from sympy import *
from math import *
from prettytable import PrettyTable
import numpy as np
import open

x=Symbol('x')
function = input("Enter the function to integrate: ")
a = input("Enter the lower limit: ")
b = input("Enter the upper limit: ")

print("\n------------------------\n")

p=integrate(function,x)
print('Symbolic Function used to find calculate true value: ' + str(p))

print("\n------------------------\n")

trueV = integrate(function,(x,a,b))
trueVF = eval(str(trueV))

print('True value: ' + str(trueVF))

print("\n------------------------\n")

print('Open Methods\n')

n0 = 0
n1 = 0
n2 = 0
n3 = 0

t = PrettyTable(['Function', 'Approximated Value', 'Error'])

trap = open.n0(a, b, function, str(trueV))
t.add_row(['n = 0', trap, abs(trueVF - trap)])

simp13 = open.n1(a, b, function, str(trueV))
t.add_row(['n = 1', simp13, abs(trueVF - simp13)])

simp38 = open.n2(a, b, function, str(trueV))
t.add_row(['n = 2', simp38, abs(trueVF - simp38)])

bolle = open.n3(a, b, function, str(trueV))
t.add_row(['n = 3', bolle, abs(trueVF - bolle)])

print(t)
