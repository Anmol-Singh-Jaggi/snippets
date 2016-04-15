'''
Compute square root using gradient descent.
'''


n = 50


# Cost function
def J(x):
    return (x * x - n)**2


# Derivative of the cost function
def Jd(x):
    return 4 * x * (x * x - n)


def gradient_descent(x, alpha=10**-3, iters=10**6, error=10**-4):
    print(x, J(x))
    for i in range(iters):
        if J(x) <= error:
            break
        x -= alpha * Jd(x)
        print(x, J(x))
        # If x becomes negative, it means that
        # the learning rate is not small enough
        if x < 0:
            # Restart the process after making the learning rate smaller
            x = n
            alpha /= 10


x = n
gradient_descent(x)
