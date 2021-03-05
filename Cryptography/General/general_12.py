def extgcd(p, q):

    if p == 0 :
        return q, 0, 1

    gcd, u1, v1 = extgcd(q%p, p)

    u = v1 - (q//p) * u1
    v = u1

    return gcd, u, v

p = 26513
q = 32321
g, u, v = extgcd(p, q)
print("crypto{"+str(u)+","+str(v)+"}")
