from utils.util import *

def run(inString,fName):
    
    result = 0x4e67c6a7
    if inString.startswith("Nt") or inString.startswith("Zw"):
        inString = inString[2:]
    for i in inString:
        result ^= (ord(i) + (result >> 2) + (result << 5)) & 0xffffffff
    return result



def get_pseudocode():
    pseudocode = '''acc := 0x4e67c6a7;
if input_string.startswith("Nt") or input_string.startswith("Zw") {
   input_string += 2;
}
for c in input_string {
   t0 := (acc >> 2);
   t1 := (acc << 5);
   acc := acc ^ (c + t0 + t1);
}
'''

    return pseudocode

def get_name():
    return 'shr2Shl5XorHash32'

def main():
    print 'main called'
    return
