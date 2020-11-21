from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0xFFFFFFFF
    for i in inString:
        ci = ord(i)
        ci = ci ^ val
        ci = ci * val
        ci_hex = "%16x"%ci
        ci_hex = ci_hex[8:16]
        ci_hex = int(ci_hex, 16)
        shr8 = val >> 8
        val = ci_hex ^ shr8
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc = (acc >> 8) ^ acc * (acc ^ c);
}
'''

    return pseudocode

def get_name():
    return 'xorShr8Hash32'

def main():
    print 'main called'
    return
