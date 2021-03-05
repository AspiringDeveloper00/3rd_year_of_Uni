from binascii import unhexlify

def xor(s1,s2):
    return format(int(s1, 16) ^ int(s2, 16),'x')


KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

KEY2 = xor("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e", KEY1)
print("KEY2: "+format(KEY2))

KEY3 = xor("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1", KEY2)
print("KEY3: "+format(KEY3))

tmp = xor(xor(KEY1, KEY2), KEY3)

FLAG = xor("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf", tmp)
print("FLAG: "+format(unhexlify(FLAG)))
