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