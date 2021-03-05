from Cryptodome.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
n = 742449129124467073921545687640895127535705902454369756401331
e = 3
ct = 39207274348578481322317340648475596807303160111338236677373

p=752708788837165590355094155871
q=986369682585281993933185289261

f=(p-1)*(q-1)
def extgcd(p, q):

    if p == 0 :
        return q, 0, 1

    gcd, u1, v1 = extgcd(q%p, p)

    u = v1 - (q//p) * u1
    v = u1

    return  gcd,u,v

d=extgcd(e,f)[1]
m=pow(ct,d,n)
print(long_to_bytes(m))
