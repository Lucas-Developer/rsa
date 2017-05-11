from random import randint
import math

def is_prime(prime_candidate):
    i = 2
    while i < prime_candidate:
        if (prime_candidate % i == 0 ):
            return False
        i = i + 1
    return True

def generate_prime() :
    prime_candidate = randint(3, 100)

    if is_prime(prime_candidate):
        return prime_candidate

    return generate_prime()



def find_smallest_number_that_cannot_divide_t(t):
    i = 3
    while t % i != 0 :
        i  = i + 1
    return i

def extended_euclidian(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_euclidian(b % a, a)
        return (g, y - (b // a) * x, x)

def modular_inverse(b, n):
    g, x, _ = extended_euclidian(b, n)
    if g == 1:
        return x % n

def generate_params():
    p = generate_prime()
    q = generate_prime()
    # p = 29
    # q = 31
    N = p * q
    t = (p - 1) * (q -1)
    #e = find_smallest_number_that_cannot_divide_t(t)
    e = 11
    d = modular_inverse(e, t)

    if d == None:
        return generate_params()

    print ("p: " + str(p))
    print ("q: " + str(q))
    print ("N: " + str(N))
    print ("t: " + str(t))
    print ("e: " + str(e))
    print ("d: " + str(d))

    return (N, e, d)



def encrypt(data, N, e):
     return data ** e % N

def decrypt(encrypted, N, d):
    return encrypted ** d % N

data = 119

N, e, d = generate_params()
encrypted = encrypt(data, N, e)
print("Data: " + str(data))
print("Encrypted: " + str(encrypted))
print("decrypted: " + str(decrypt(encrypted, N, d)))

