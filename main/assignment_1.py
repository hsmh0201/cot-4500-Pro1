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
