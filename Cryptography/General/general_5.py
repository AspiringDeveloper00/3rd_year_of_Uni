import telnetlib
import json
import base64
import codecs
from binascii import unhexlify

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def list_to_string(s):
    output = ""
    return(output.join(s))

for i in range(0,101):

    received = json_recv()

    if "flag" in received:
        print("Flag: " + format(received["flag"]))
        break

    print("Received type: " + format(received["type"]))
    print("Received encoded value: " + format(received["encoded"]))

    word = received["encoded"]
    encoding = received["type"]

    if encoding == "base64":
        decoded = base64.b64decode(word).decode('utf8').replace("'", '"')
    elif encoding == "hex":
        decoded = (unhexlify(word)).decode('utf8').replace("'", '"')
    elif encoding == "rot13":
        decoded = codecs.decode(word, 'rot_13')
    elif encoding == "bigint":
        decoded = unhexlify(word.replace("0x", "")).decode('utf8').replace("'", '"')
    elif encoding == "utf-8":
        decoded = list_to_string([chr(b) for b in word])

    print("Decoded: " + format(decoded))

    to_send = {
        "decoded": decoded
    }

    json_send(to_send)
