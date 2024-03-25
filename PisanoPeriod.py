import numpy as np

F = np.array([[1, 1], 
              [1, 0]])

n = 4

def pi(n):
    order = 1
    result = F
    while not np.array_equal(result, np.identity(2)):
        result = np.mod(np.matmul(result, F), n)
        order += 1
    return(order)

print(pi(n))