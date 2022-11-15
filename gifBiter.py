import random
import shutil




frame = 0
randomint = 1
print("put your file in same path of this script and type the name: (exemple: image.png)")
filepath = input()
print("")
print("how many frames do you want (int)")
frameAmount = int(input())
print("where the file heather ends (the part that if changed maybe turn the file useless)")
headerEnd = int(input())
#print("byte location that will be corrupted (int)")
#bytelocation = int(input())
randombytevalue = int.from_bytes(random.randbytes(1), "big")
frame = 0
bytevalue = frame.to_bytes(1, "big")


with open(filepath, "rb") as f:
    b = bytearray(f.read())
    bytelocation = random.randint(headerEnd,len(b))

while(frame < frameAmount):
    bytevalue = frame.to_bytes(1, "big")
    bytevalue = int.from_bytes(bytevalue, "big")

    

 
    frameName = str(frame)+filepath
    shutil.copyfile(filepath,frameName)
    b[bytelocation] = bytevalue
    
 
    randombytevalue = randombytevalue + 1

    with open(filepath, "wb") as f:
        f.write(bytes(b))
    frame = frame + 1
    print(frame, bytelocation, bytevalue)






