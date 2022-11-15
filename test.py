import random
whilenumb = 0
bytevalueint = 0


bytevalue = bytevalueint.to_bytes(1, "big")


with open("image.png", "rb") as f:
    b = bytearray(f.read())
    bytelocation = random.randint(100,len(b))


while(whilenumb < 10):
    bytevalue = bytevalueint.to_bytes(1, "big")
    print(whilenumb, bytevalue,bytelocation )
    bytevalueint = bytevalueint + 1
    whilenumb = whilenumb + 1

