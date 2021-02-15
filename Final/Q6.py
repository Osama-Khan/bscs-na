#Write python code to calculate the value of
#∫_1.623^2.616▒〖x^2  cos⁡(3x)log⁡(√(x^3 ))〗 dx
#Using trapezoidal rule for n=6.
#Output sample is as follows

import numpy as np
from matplotlib import pyplot as plt
from math import cos, log, sqrt

f = lambda x: (x*x)*(cos(3*x))*(log(sqrt(x**3), 10))

def trap(f, a, b, n, x):
  h = (b-a)/n
  res = 0
  for i in range(1, n):
    res += f(x[i])
  res = (h/2)*(f(x[0])+(2*res)+f(x[n]))
  return res

lower = 1.623; upper = 2.616; n = 6

x = np.linspace(lower,upper,n+1)
y = [f(i) for i in x]

trapAnswer = trap(f, lower, upper, n, x)

X = np.linspace(lower,upper)
Y = [f(i) for i in X]
plt.plot(X,Y)

for i in range(n):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'b',edgecolor='b',alpha=0.25)

plt.title(f'Trapezoid Rule Answer = {trapAnswer}\nfor n = {n}')
plt.show()