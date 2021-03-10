from base64 import b64encode, b64decode
import operator

penalites = {
  "e":"1",
  "E":"1",
  "t":"1",
  "T":"1",
  "a":"1",
  "A":"1",
  "o":"1",
  "O":"2",
  "i":"1",
  "I":"1",
  "n":"1",
  "N":"1",
  "s":"2",
  "S":"2",
  "h":"2",
  "H":"2",
  "r":"2",
  "R":"2",
  "d":"2",
  "D":"2",
  "l":"2",
  "L":"2",
  "c":"3",
  "C":"3",
  "u":"3",
  "U":"3",
  "m":"3",
  "M":"3",
  "w":"3",
  "W":"3",
  "f":"3",
  "F":"3",
  "g":"3",
  "G":"3",
  "y":"4",
  "Y":"4",
  "p":"4",
  "P":"4",
  "b":"4",
  "B":"4",
  "v":"4",
  "V":"4",
  "k":"4",
  "K":"4",
  "j":"5",
  "J":"5",
  "x":"5",
  "X":"5",
  "q":"6",
  "Q":"7",
  "z":"6",
  "Z":"6",
  "1":"6",
  "2":"7",
  "3":"7",
  "4":"7",
  "5":"7",
  "6":"7",
  "7":"7",
  "8":"7",
  "9":"7",
  "0":"6",
  " ":"1",
  ".":"3",
  ",":"3",
  "!":"4",
  "(":"5",
  ")":"5",
  "-":"10",
  "&":"10",
  "?":"9",
}

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
        return str(encoded)
    else:
        decoded = ba.decode("ASCII")
        return str(decoded)

def score(bfdict, penalites):
  results = {}
  for key, value in bfdict.items():
    score = 0
    for i in value:
      if i[0] in penalites.keys():
        penalty = int(penalites.get(i[0]))
        score += penalty
      else:
        score += 10000
    results[key] = score
  return results

def sort(results):
  return sorted(results.items(), key=lambda x: int(x[1]), reverse=False)

def main():
    mode = input("Mode? E for encrypt or D for decrypt\n")
    if mode == "E":
        emode = input("C for custom text or T for text file\n")
        if emode == "C":
            message = input("What is your message\n")
        key = input("What is key\n")
        key = int(key)
    elif mode == "D":
        dmode = input("With key (K), or brute force (B)?\n")
        if dmode == "K":
            key = input("What is key\n")
            key = int(key)

    if mode == "E":
        if emode == "C":
            print(single_byte_xor(message, key, encrypt=True))
        elif emode == "T":
            with open("etext.txt", "r") as f:
                message = f.readline()
                f.close()
            encrypted = single_byte_xor(message, key, encrypt=True)
            print(encrypted)
            with open("encripted.txt", "w") as f:
                f.write(encrypted)
                f.close()
    elif mode == "D":
        with open("encripted.txt", "r") as f:
            message = f.readline()
            f.close()
        if dmode == "K":
            print(single_byte_xor(message, key, encrypt=False))
        elif dmode == "B":
            dictionary = {}
            for k in range(256):
                try:
                    decrypted = single_byte_xor(message, k, encrypt=False)
                    dictionary[k] = decrypted
                except:
                    pass
            print("Completed")
            results = score(dictionary, penalites)
            sortedResults = sort(results)
            for i in range(5):
                result = sortedResults[i]
                key = result[0]
                scored = result[1]
                print("(" + str(i) + ")" + " Key: " + str(key) + " Score: " + str(scored))
                value = dictionary[key]
                print(value)
                print("\n")
            largest = sortedResults[-1]
            largestscore = largest[1]
            print("Largest score: " + str(largestscore))
    else:
        print("Invalid mode entered")

if __name__ =="__main__":
    while True:
        main()
