import random
import shutil



frame = 0
print("put your file in same path of this script and type the name: (exemple: image.png)")
filepath = input()
print("")
print("how many frames do you want")
frameAmount = int(input())
print("where the file heather ends (the part that if changed maybe turn the file useless)")
headerEnd = int(input())


while(frame < frameAmount):
    shutil.copyfile(filepath,str(frame)+filepath)
    with open(filepath, "rb") as f:
        b = bytearray(f.read())

    b[random.randint(headerEnd,len(b))] = int.from_bytes(random.randbytes(1), "big") 

    with open(filepath, "wb") as f:
        f.write(bytes(b))
    frame = frame + 1





