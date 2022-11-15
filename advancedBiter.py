import random


print("put your file in same path of this script and type the name: (exemple: image.png) [str]")
filepath = input()
print("")
print("do you want do corrupt in a specific location? [string]")
if(input()=="yes"):
    havecustomlocation = true
    print("type the location: [int]")
    customlocation = input() 


with open(filepath, "rb") as f:
    b = bytearray(f.read())

b[random.randint(0,len(b))] = int.from_bytes(random.randbytes(1), "big") 

with open(filepath, "wb") as f:
    f.write(bytes(b))





