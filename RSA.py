def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt(p, q, x, pt):
    #4 parameters + plaintext
    n = p * q
    phi_n = (p-1) * (q-1)
    # x**e mod n
    e = 5

    #assume e was found
    ct = [(ord(i) ** (x ** e)) % n for i in pt]
    return ct

def decrypt(p, q, d, ct):
    n = p * q
    e = 5 

    #Assume e was found
    pt = [chr((i ** (d ** e)) % n) for i in ct]
    return pt

#3a
y = encrypt(3, 11, 5, "hello")
decrypt(3, 11, 7, y)

#3b
z = encrypt(5, 11, 9, "world")
print(z)
decrypt(5, 11, 3, z)



