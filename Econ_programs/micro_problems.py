from sympy import *
x1, x2, y, z, p = symbols('x1 x2 y z p')

def main():

    print()
    print("MicroEconomics Problem Solver: \n")
    print(" For normal profit maximization enter 1\nFor profit maximization with endowment enter 2\nFor Optimal Choice for Monopolist enter 3\nFor Labor Supply enter 4\nFor Leisure and Consumption enter 5\n ")


    problem = 1

    while problem != 0:
        problem = int(input("Enter number (1-5) to compute problem type (or 0 to exit): "))
        print()
        if problem == 1:
            profit_max()
        elif problem  == 2:
            with_endowment()
        elif problem == 3:
            monopoly()

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
    
# prints the Foc's, and x1,x2 solved respectively for y (lambda)
#
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

def with_endowment():
    p1 = float(input("Input the price of good 1: "))    # price of good 1

    p2 = float(input("Input the price of good 2: "))    #price of good 2

    w1 = float(input("Input the endowment for good 1: "))   # endowment 1

    w2 = float(input("Input the endowment for good 2: "))   # endowment 2

    #m = float(input("Input the total income (m): "))    # total income
    m = (p1*w1)+(p2*w2) 

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
    print()
    
   

def monopoly():

    cost = sympify(input("Enter the cost function c(y): "))
    print()

    average_cost = simplify((cost/y))   #computes average cost

    marginal_cost = diff(cost,y)    #computes marginal cost

    print("Average Cost, Ac(y)=",average_cost)
    print()
    print("Marginal Cost, MC(y)=",marginal_cost)
    print()

    demand = sympify(input("Enter the demand function D(p): "))
    print()


    price = solve(Eq(demand, y),p)[0]       #computes the price function p(y) by inversing the demand function

    print("Inverse: p(y)=",simplify(price))
    print()

    revenue = price*y
    marginal_revenue = diff(revenue, y)

    print("Revenue p(y)*y=",revenue)
    print()
    print("Marginal Revenue MR(y)=",marginal_revenue)
    print()

    Ym = solve(Eq(marginal_revenue,marginal_cost),y)[0]
    Pm = solve(Eq(demand,Ym),p)[0]

    print('Ym=',Ym)
    print("Pm=",Pm)
    print()

    profit = revenue-cost
    total_profit = profit.subs(y,Ym)
    #profit = solve(Eq(y,finaly),(revenue-cost))
    print("profit=",profit)
    print()
    print("Profit : ", total_profit)
    print()

    Yc = solve(Eq(price,marginal_cost),y)[0]
    Pc = solve(Eq(demand,Yc),p)[0]

    print("Optimal output and price, if market competitive instead of Monopoly: ")
    print("Yc=",Yc)
    print("Pc=",Pc)
    print()
    
main()

