def Sieve_of_Eratosthenes(n):
    A = [True] * n
    squrtNum = int(sqrt(n)) + 1
    for i in range(2, squrtNum):
        if A[i]:
            j = i + i
            while j < n:
                A[j] = False
                j += i
    P = 0
    primes = []
    
    for u in A:
        if u == True:
            u = P
            primes.append(u)
        P += 1
    return primes
                

output = Sieve_of_Eratosthenes (1000)
print output