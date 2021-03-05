from binascii import unhexlify

def xor(input, k):

    output = b''
    for b1, b2 in zip(input, k):
        output += bytes([b1 ^ b2])
    try:
        return output.decode("utf-8")
    except:
        return "error"

data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
raw = unhexlify(data)
key = (xor(raw[:7], "crypto{".encode()) +"y").encode()
key += key * int((len(raw) - len(key))/len(key))
key += key[:((len(raw) - len(key))%len(key))]
flag = xor(raw, key)
print("FLAG: "+flag)
