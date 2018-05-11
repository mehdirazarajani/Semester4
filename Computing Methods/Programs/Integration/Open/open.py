from sympy import *
from math import *
import numpy as np

def n0(a,b,func,trueval):
    n = str(0)
    a=eval(a)
    b=eval(b)
    n=eval(n)
    x = a
    b = b
    func = func
    h = ((b) - a) / (n+2)
    x=a+h
    p=eval(func)
    hp=2*h*p

    return hp

def n1(a,b,func,trueval):
    n = str(1)
    a = eval(a)
    b = eval(b)
    n = eval(n)
    h = ((b) - a) / (n + 2)

    a=a+h
    b=a+h
    func1 = func.replace('x', 'a')
    func2 = func.replace('x', 'b')
    funcF=func1+'+'+func2
    p=eval(funcF)
    hp=((3*h)/2)*p
    return hp

def n2(a,b,func,trueval):
    n = str(2)
    a = eval(a)
    b = eval(b)
    n = eval(n)
    h = ((b) - a) / (n + 2)
    a = a + h
    b = a + h
    c = b + h
    func1 = func.replace('x', 'a')
    func1= '2*('+func1+')'
    func2 = func.replace('x', 'b')
    func2 = '('+func2+')'
    func3 = func.replace('x', 'c')
    func3 = '2*(' + func3+')'
    funcF = func1 + '-' + func2 +  '+' + func3
    p = eval(funcF)
    hp = ((4* h) / 3) * p
    return hp

def n3(a,b,func,trueval):
    n = str(3)
    a = eval(a)
    b = eval(b)
    n = eval(n)
    h = ((b) - a) / (n + 2)
    a = a + h
    b = a + h
    c = b + h
    d = c + h
    func1 = func.replace('x', 'a')
    func1= '11*('+func1+')'
    func2 = func.replace('x', 'b')
    func3 = func.replace('x', 'c')
    func4 = func.replace('x','d')
    func4 = '11*('+func4+')'
    funcF = func1 + '+' + func2 +  '+' + func3  +  '+' + func4
    p = eval(funcF)
    hp = ((5* h) / 24) * p
    return hp