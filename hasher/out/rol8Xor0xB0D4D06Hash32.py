from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = val ^ (ord(i) & 0xDF)
        val = rol(val, 0x8, 32)
        val = val + (ord(i) & 0xDF)
    return (val ^ 0xB0D4D06) & 0xffffffff



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROL(acc, 8):
   acc := acc ^ c ^ 0xB0D4D06;
}

Smork_bot
'''

    return pseudocode

def get_name():
    return 'rol8Xor0xB0D4D06Hash32'

def main():
    print 'main called'
    return
