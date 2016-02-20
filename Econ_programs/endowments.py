## Endowments

from sympy import *


## Profit Maximization Problem

x1, x2, y, z = symbols('x1 x2 y z')
init_printing()

def main():

    print("MicroEconomics Problem Solver: ")
    print()
    print(" For normal profit maximization enter 1, ")
    print(" For profit maximization with endowment enter 2, ")

    problem = 1

    while problem != 0:
        problem = int(input("Enter number (1-?) to compute problem type (or 0 to exit): "))
        if problem == 1:
            profit_max()
        elif problem  == 2:
        	with_endowment()
   

def with_endowment():
    p1 = float(input("Input the price of good 1: "))    # price of good 1

    p2 = float(input("Input the price of good 2: "))    #price of good 2

    w1 = float(input("Input the endowment for good 1: "))	# endowment 1

    w2 = float(input("Input the endowment for good 2: "))	# endowment 2

    #m = float(input("Input the total income (m): "))    # total income
    m = (p1*w1)+(p2*w2) 

    utility = sympify(input("Enter the Utility Function using variables x1, and x2: ")) # utility function U(x1,x2)

    print("Utility: U(x1,x2)=",utility)
    print()
 
    Lagrange = utility + y*(m-(p1*x1)-(p2*x2))

    print("Lagrangian for the profit maximization: ")
    print("L =", simplify(Lagrange))
    print()

    dL_dx1 = diff(Lagrange, x1)     # solves the foc with respect to x1
    dL_dx2 = diff(Lagrange, x2)     # solves the foc with respect to x2
    dL_dy = diff(Lagrange, y)       # solves the foc with respect to y (lambda)
    
###
#
# prints the Foc's, and x1,x2 solved respectively for y (lambda)
#
###

    print("F.O.C.'s: ")
    print("--------------")
    print()
    print("[x1]: ",simplify(dL_dx1))
    print('[x2]: ',expand(dL_dx2))
    print('[y]: ',cancel(dL_dy))
    print()
    a = solve(dL_dx1, y) # Solves x1's foc for lambda(y)
    b = solve(dL_dx2, y) # Solves x2's foc for lambda(y)
    print("lambda for x1: ",a)
    print("lmabda for x2: ",b)
    print()

    x1_star = (solve(Eq(a[0],b[0]), x1))[0]
    print("x1* =",x1_star)
    if (x1_star < w1):
    	print("Net Seller of Good 1")
    else:
    	print("Net Buyer of Good 1")
    print()

    x2_star = (solve(m-(p1*x1_star)-(p2*x2),x2))[0]
    print("x2*=",x2_star)
    if (x2_star < w2):
    	print("Net Seller of Good 2")
    else:
    	print("Net Buyer of Good 2")
    
main()

