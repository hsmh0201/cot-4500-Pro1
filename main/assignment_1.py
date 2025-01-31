## Approximation Algorithm 
def root_two():
    x0 = 1.5
    tol = 0.000001

    iteration_count = 0
    diff = x0
    x = x0

    print(f"{iteration_count} : {x}")

    while diff >= tol:
        iteration_count += 1
        y = x
        x = (x / 2) + (1 / x)
        print(f"{iteration_count} : {x}")

        diff = abs(x - y)

    print(f"\nConvergence after {iteration_count} iterations")

root_two()



## Bisection Method
## Coded to get output from slide 18 of Ch. 2.1 Powerpoint 

import math

def bisection(f, left, right, tol=1e-3, max_iter=10):
    
    if f(left) * f(right) >= 0:
        raise ValueError("Function values at the interval endpoints must have opposite signs.")

    for i in range(max_iter):
        mid = (left + right) / 2  
        print(f"Iteration {i+1}: x = {mid}")

        if abs(right - left) < tol:  
            break
        if (f(left) < 0 and f(mid) > 0) or (f(left) > 0 and f(mid) < 0):
            right = mid  
        else:
            left = mid  
    return mid  


f = lambda x: x**3 + 4*x**2 - 10
root = bisection(f, 1, 2)
print(f"Approximate root: {root}")



## Fixed Point Iteration
## Coded to get output for example function x^3+4x^2-10=0 from slide 14 Ch. 2.2

def fixed_point_iteration(g, p0, tol=1e-3, max_iteration=100):
    i = 1

    while i <= max_iteration:
        p = g(p0)

        if abs(p - p0) < tol:
            print(f"{p} Success")
            return
        
        i += 1
        p0 = p

    print("Failure")
g = lambda x: (10 - 4*x**2) ** (1/3)
fixed_point_iteration(g, 1.5)



## Newton Raphson
## Coded to get output for f(x)=cos(x)-x=0 example from slide 8 Ch. 2.3

import math

def newton_raphson(f, p0, tol=1e-6, max_iterations=100):
    for i in range(1, max_iterations + 1):
        if df(p0) == 0:
            print("Failure")
            return
        
        p_next = p0 - f(p0) / df(p0)
        if abs(p_next - p0) < tol:
            print(f"Root: {p_next} success in {i} iterations")
            return
        p0 = p_next
    print("Failure, max reached")

f = lambda x: math.cos(x) - x
df = lambda x: -math.sin(x) - 1

newton_raphson(f, df, 0.5)
