from base64 import b64encode, b64decode

mode = input("Mode? E for encrypt or D for decrypt\n")
if mode == "E":
    emode = input("C for custom text or T for text file\n")
    if emode == "C":
        message = input("What is your message\n")
key = input("What is key\n")
key = int(key)

def single_byte_xor(message, key, encrypt=True):
    if encrypt:
        bs = bytearray(message, encoding='ASCII')
    else:
        bs = bytearray(b64decode(message))

    ba = bytearray()
    for b in bs:
        ba.append(b^key)

    if encrypt:
        encoded = b64encode(ba)
        return "B64 encoded: " + str(encoded)
    else:
        decoded = ba.decode("ASCII")
        return "B64 decoded: " + str(decoded)
    


if mode == "E":
    if emode == "C":
        print(single_byte_xor(message, key, encrypt=True))
    elif emode == "T":
        with open("etext.txt", "r") as f:
            message = f.readline()
            f.close()
        print(single_byte_xor(message, key, encrypt=True))
elif mode == "D":
    with open("cipher.txt", "r") as f:
        message = f.readline()
        f.close()
    print(single_byte_xor(message, key, encrypt=False))
else:
    print("Invalid mode entered")