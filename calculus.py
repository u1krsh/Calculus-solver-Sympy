# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:48:52 2022

@author: DHRUV
"""

import sympy as smp
from sympy import *

print('''      1-Derivatives
      2-Basic Antiderivatives
      3-Definite Integrals
      4-Limits
      5-Double Integrals
      6-Definite Double Integrals''')
c = str(input("What Calculus you want to do?: "))
a = str(input("Enter a Problem: "))
sin = smp.sin
cos = smp.cos
tan = smp.tan
csc = smp.csc
sec = smp.sec
cot = smp.cot
pi = smp.pi
theta = smp.symbols("theta")
if c=="1":
    b = str(input("What do you want to solve for: "))
    x = smp.symbols(b)
    pprint(Derivative((a), x))
    print('''   
          ''')
    pprint(Derivative((a), x).doit())
elif c=="2":
    b = str(input("What do you want to solve for: "))
    x = smp.symbols(b)
    pprint(Integral((a), x))
    print('''   
          ''')
    pprint(Integral((a), x).doit())
elif c=="3":
    d = str(input("You Want to solve from: "))
    e = str(input("You Want to solve to: "))
    b = str(input("What do you want to solve for: "))
    x = smp.symbols(b)
    pprint(Integral((a), (x, d, e)))
    print('''   
          ''')
    pprint(Integral((a), (x, d, e)).doit())
elif c=="4":
    d = str(input("You Want to solve from: "))
    e = str(input("You Want to solve to: "))
    pprint(Limit((a), d, e))
    print('''   
          ''')
    pprint(Limit((a), d, e).doit())
    
elif c=="5":
    b = str(input("What do you want to solve for in first integral: "))
    h = str(input("What do you want to solve for in second integral: "))
    x = smp.symbols(b)
    y = smp.symbols(h)
    pprint(Integral(Integral(a,x),y))
    print('''   
          ''')
    pprint(Integral(Integral(a,x),y).doit())
elif c=="6":
    d = str(input("You Want to solve from for first integral : "))
    e = str(input("You Want to solve to for first integral: "))
    f = str(input("You Want to solve from for second integral : "))
    g = str(input("You Want to solve to for second integral: "))
    b = str(input("What do you want to solve for in first integral: "))
    h = str(input("What do you want to solve for in second integral: "))
    x = smp.symbols(b)
    y = smp.symbols(h)
    pprint(Integral(Integral((a), (x, d, e)),(h , f , g)))
    print('''   
          ''')
    pprint(Integral(Integral((a), (x, d, e)),(h , f , g)).doit())
    
    

    

