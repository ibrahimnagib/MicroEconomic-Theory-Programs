## Monopolies

from sympy import *
x1, x2, y, z, p = symbols('x1 x2 y z p')



def monopoly():

	cost = sympify(input("Enter the cost function c(y): "))

	average_cost = simplify((cost/y))	#computes average cost
	marginal_cost = diff(cost,y)	#computes marginal cost

	print("Average Cost, Ac(y)=",average_cost,'\n')
	print("Marginal Cost, MC(y)=",marginal_cost,'\n')

	demand = sympify(input("Enter the demand function D(p): \n"))

	price = solve(Eq(demand, y),p)[0]		#computes the price function p(y) by inversing the demand function
	print("Inverse: p(y)=",simplify(price),'\n')

	revenue = price*y
	marginal_revenue = diff(revenue, y)

	print("Revenue p(y)*y=",revenue,'\n')
	print("Marginal Revenue MR(y)=",marginal_revenue,'\n')

	Ym = solve(Eq(marginal_revenue,marginal_cost),y)[0]
	Pm = solve(Eq(demand,Ym),p)[0]

	print('Ym=',Ym,'\n')
	print("Pm=",Pm,'\n')

	profit = revenue-cost
	total_profit = profit.subs(y,Ym)
	print("profit=",profit,'\n')
	print("Profit : ", total_profit,'\n')

	Yc = solve(Eq(price,marginal_cost),y)[0]
	Pc = solve(Eq(demand,Yc),p)[0]

	print("Optimal output and price, if market competitive instead of Monopoly: ")
	print("Yc=",Yc)
	print("Pc=",Pc,'\n')
	print()



monopoly()