h=2
p=18
print(p/(p+h))

import sympy as sy

d,x,ystar=sy.symbols('d x ystar')

pdlessthanystar=sy.integrate((1/60),(d,90,ystar))

pdlessthanystar

y_star=sy.solve(pdlessthanystar-p/(p+h),ystar)
y=sy.symbols('y')
S=int(y_star[0])
S

integral1=sy.integrate((1/60)*(y-d),(d,90,y))

integral1

integral2=sy.integrate((1/60)*(d-y),(d,y,150))

integral2

ECofy=h*integral1+p*integral2

K=10
solns=sy.solve(ECofy.subs(y,S)+K-ECofy,y)

ans=[]
for i in solns:
  if i>S:
    print(i,">S and discarded")
  else:
    ans.append(i)

ans

flag=0
for i in ans:
  if i>0:
    flag=1
if flag==0:
  print("No feasible value of s")

print("If x<{} order {}-x units".format(ans[0],S))
print("Else do not order")

solns

ECofy
