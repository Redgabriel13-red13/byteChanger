import random


print("put your file in same path of this script and type the name: (exemple: image.png)")
filepath = input()
print("")


with open(filepath, "rb") as f:
    b = bytearray(f.read())

b[random.randint(0,len(b))] = int.from_bytes(random.randbytes(1), "big") 

with open(filepath, "wb") as f:
    f.write(bytes(b))





