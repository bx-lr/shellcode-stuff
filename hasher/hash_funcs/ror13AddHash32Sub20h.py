from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = ror(val, 0xd, 32)
        if ord(i) < 97:
            val = int(val) + ord(i)
        else:
            val = int(val) + ord(i) - 32
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROR(acc, 13);
   if (c > 0x61)
       c = c - 0x20;
   acc := acc + c;
}
'''

    return pseudocode

def get_name():
    return 'ror13AddHash32Sub20h'

def main():
    print 'main called'
    return
