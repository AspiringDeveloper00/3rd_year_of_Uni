string = "label"
flag = ''

for s in string:
    flag += chr(ord(s) ^ 13)

print('crypto{'+ format(flag) +'}')
