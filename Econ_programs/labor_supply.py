#Labor Supply

from sympy import *
x1, x2, y, z, p, C, R = symbols('x1 x2 y z p C R')

def labor_supply():

	pc = float(input("Input the price of consumption (p): "))
	wage = float(input("Input the wage rate (w): "))
	u_m = float(input("Input unearned income (m): "))
	rbar = float(input("Input time of endowment for maximum rest (R-bar): "))

	utility = sympify(input("Enter the Utility Function using variables C, and R: ")) # utility function U(C,R)
	
	print("Utility: U(C,R)=",utility)
	print()
 
	Lagrange = utility + y*(u_m+(wage*rbar)-(wage*R-pc*C))

	print("Lagrangian for the profit maximization: ")
	print("L =", simplify(Lagrange))
	print()

	C_foc = Eq(diff(Lagrange, C),0)     # solves the foc with respect to C
	R_foc = Eq(diff(Lagrange, R),0)     # solves the foc with respect to R
	y_foc = Eq(diff(Lagrange, y),0)       # solves the foc with respect to y (lambda)
    
# prints the Foc's, and x1,x2 solved respectively for y (lambda)
#
	print("F.O.C.'s: ")
	print("--------------")
	print()
	print("[C]: ",simplify(C_foc))
	print('[R]: ',expand(R_foc))
	print('[y]: ',cancel(y_foc))
	print()
	a = solve(C_foc, y) # Solves x1's foc for lambda(y)
	b = solve(R_foc, y) # Solves x2's foc for lambda(y)
	print("lambda for C: ",a)
	print("lmabda for R: ",b)
	print()

	#ans = solve([a[0],b[0], Eq((u_m+(wage*rbar)-(wage*R-pc*C)),0) ],[R,C])
	#print(ans)

	C_star = (solve(Eq(a[0],b[0]), C))[0]
	# if type(C_star) != float:
	# 	R_star = (solve((u_m+(wage*rbar)-(wage*R-pc*C)),R))[0]
	# 	C_star = R_star.subs(C,C_star)
	# else:
	# 	R_star = (solve(u_m+(wage*rbar)-(wage*R-pc*C),R))[0]


	# print("R* =",R_star) # 4 * x2
	# #x2_star = (solve(m-(p1*x1_star)-(p2*x2),x2))[0]
	print("C*=",C_star) # 2
	# #x2_star = x2_star.subs(x1,x1_star)
	# #x1_star = x1_star.subs(x2,x2_star)
	# #print("x2*=",x2_star)
	# print()

labor_supply()
