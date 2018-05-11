from sympy import *
from math import *
import numpy as np


def evalBool(a, b, list, trueVal, n):

    n = eval(n)

    n = n - 1

    h = eval('(' + b + '-' + a + ')' + '/' + str(n))

    simpsonPointslist = list

    i = 0
    ans = 0

    v = eval(trueVal)

    while (true):
        if (i + 4 >= len(simpsonPointslist)):
            break

        val1 = simpsonPointslist[i]
        val2 = simpsonPointslist[i + 1]
        val3 = simpsonPointslist[i + 2]
        val4 = simpsonPointslist[i + 3]
        val5 = simpsonPointslist[i + 4]

        i = i + 4

        func1 = 'val1'
        func1 = '7*(' + func1 + ')'

        func2 = 'val2'
        func2 = '32*(' + func2 + ')'

        func3 = 'val3'
        func3 = '12*(' + func3 + ')'

        func4 = 'val4'
        func4 = '32*(' + func4 + ')'

        func5 = 'val5'
        func5 = '7*(' + func5 + ')'

        funcF = func1 + '+' + func2 + '+' + func3 + '+' + func4 + '+' + func5
        p = eval(funcF)
        hp = p * ((2 * h) / 45)
        ans = ans + hp

    return ans


def eval3Simpson(a, b, list, trueVal, n):

    n = eval(n)

    n = n - 1

    h = eval('(' + b + '-' + a + ')' + '/' + str(n))

    simpsonPointslist = list

    i = 0
    ans = 0

    v = eval(trueVal)

    while (true):
        if (i + 3 >= len(simpsonPointslist)):
            break

        val1 = simpsonPointslist[i]
        val2 = simpsonPointslist[i + 1]
        val3 = simpsonPointslist[i + 2]
        val4 = simpsonPointslist[i + 3]

        i = i + 3

        func1 = 'val1'
        func2 = 'val2'
        func2 = '3*(' + func2 + ')'
        func3 = 'val3'
        func3 = '3*(' + func3 + ')'
        func4 = 'val4'
        funcF = func1 + '+' + func2 + '+' + func3 + '+' + func4
        p = eval(funcF)
        hp = p * ((3 * h) / 8)
        ans = ans + hp

    return ans


def evalSimpson(a, b, list, trueVal, n):

    n = eval(n)

    n = n - 1

    h = eval('(' + b + '-' + a + ')' + '/' + str(n))

    simpsonPointslist = list

    i = 0
    ans = 0

    v = eval(trueVal)

    while (true):
        if (i + 2 >= len(simpsonPointslist)):
            break

        val1 = simpsonPointslist[i]
        val2 = simpsonPointslist[i + 1]
        val3 = simpsonPointslist[i + 2]

        i = i + 2

        func1 = 'val1'
        func2 = 'val2'
        func2 = '4*(' + func2 + ')'
        func3 = 'val3'
        funcF = func1 + '+' + func2 + '+' + func3
        p = eval(funcF)
        hp = p * (h / 3)
        ans = ans + hp

    return ans


def evalTrap(a, b, list, trueVal, n):
    h = eval('(' + b + '-' + a + ')' + '/' + n)

    n1 = eval(n)

    ans = 0.0

    for i in range(n1):
        if (i+1 >= len(list)):
            break;

        a1 = list[i]
        b1 = list[i+1]

        func1 = 'a1'
        func2 = 'b1'
        funcF = func2 + '+' + func1

        p = eval(funcF)
        hp = p * (h / 2)
        ans = ans + hp

    return ans