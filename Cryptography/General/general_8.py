from binascii import unhexlify

data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
decoded = unhexlify(data)


def xor(input, k):

    output = b''
    for b in input:
        output += bytes([b ^ k])

    try:
        return output.decode("utf-8")
    except:
        return "error"


for i in range(0,255):
    a=(xor(decoded, i))
    if "crypto" in a:
        print ("FLAG:"+a)
        break
