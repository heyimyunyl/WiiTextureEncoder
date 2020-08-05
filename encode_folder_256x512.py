import os 
import sys 
import subprocess
import binascii 
import struct 


header = binascii.unhexlify("00000009544558000000002C000400800400040000012000000400800000000000030ED3000A78F00000CCCC205344440000007C0000100F00000100000001000000040000000000000000000000000000000000000000000000000000000000000000000000000000000000000000005454564E00020007000000200000004141504D430000002000FF00000000FF00000000FFFF0000000000100000000000000000000000000000000000")


if __name__ == "__main__":
    folder = sys.argv[1]
    
    files = os.listdir(folder)
    
    for file in files:
        if not file.endswith(".png"):
            continue 
            
        path = os.path.join(folder, file)
        subprocess.call(["wimgt", "encode", path, "--dest", path+".bti", "-o", "--transform", "BTI.CMPR"])
        
        with open(path+".bti", "rb") as f:
            dat = f.read(6)
            _, _, height, width = struct.unpack(">BBHH", dat)
            
            f.seek(0x20)
            imgdata = f.read(int(height*width*0.5))
            with open(path+".ckd", "wb") as g:
                g.write(header)
                g.write(imgdata)