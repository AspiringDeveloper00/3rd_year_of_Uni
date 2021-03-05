p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e=65537
f=(p-1)*(q-1)

def extgcd(p, q):

    if p == 0 :
        return q, 0, 1

    gcd, u1, v1 = extgcd(q%p, p)

    u = v1 - (q//p) * u1
    v = u1

    return gcd, u, v

print(extgcd(e,f))
