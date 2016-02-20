## Profit Maximization

from sympy import *
x1, x2, y, z, p = symbols('x1 x2 y z p')


def profit_max():
    p1 = float(input("Input the price of good 1: "))    # price of good 1

    p2 = float(input("Input the price of good 2: "))    #price of good 2

    m = float(input("Input the total income (m): "))    # total income 

    utility = sympify(input("Enter the Utility Function using variables x1, and x2: ")) # utility function U(x1,x2)

    print("Utility: U(x1,x2)=",utility)
    print()
 
    Lagrange = utility + y*(m-(p1*x1)-(p2*x2))

    print("Lagrangian for the profit maximization: ")
    print("L =", simplify(Lagrange))
    print()

    x1_foc = diff(Lagrange, x1)     # solves the foc with respect to x1
    x2_foc = diff(Lagrange, x2)     # solves the foc with respect to x2
    y_foc = diff(Lagrange, y)       # solves the foc with respect to y (lambda)
    
###
#
# prints the Foc's, and x1,x2 solved respectively for y (lambda)
#
###

    print("F.O.C.'s: ")
    print("--------------")
    print()
    print("[x1]: ",simplify(x1_foc))
    print('[x2]: ',expand(x2_foc))
    print('[y]: ',cancel(y_foc))
    print()
    a = solve(x1_foc, y) # Solves x1's foc for lambda(y)
    b = solve(x2_foc, y) # Solves x2's foc for lambda(y)
    print("lambda for x1: ",a)
    print("lmabda for x2: ",b)
    print()

    mrs = (p1/p2)
    print("MRS = (p1/p2) =",mrs)

    x1_star = (solve(Eq(a[0],b[0]), x1))[0]
    if type(x1_star) != float:
    	x2_star = (solve(m-(p1*x1_star)-(p2*x2),x2))[0]
    	x1_star = x1_star.subs(x2,x2_star)
    else:
    	x2_star = (solve(m-(p1*x1_star)-(p2*x2),x2))[0]


    print("x1* =",x1_star) # 4 * x2
    #x2_star = (solve(m-(p1*x1_star)-(p2*x2),x2))[0]
    print("x2*=",x2_star) # 2
    #x2_star = x2_star.subs(x1,x1_star)
    #x1_star = x1_star.subs(x2,x2_star)
    #print("x2*=",x2_star)
    print()

profit_max()