from utils.util import *

def run(inString,fName):
    
    acc = 0
    for i in inString:
        acc = 0xffffffff & (acc * 0x21)
        acc = 0xffffffff & (acc + ord(i))
    return acc




def get_pseudocode():
    pseudocode = ,fName):
    acc = 0
    for i in inString:
        acc = 0xffffffff & (acc * 0x21)
        acc = 0xffffffff & (acc + ord(i))
    return acc


pseudocode_hashMult21 = '''acc := 0;
for c in input_string {
   acc := acc * 0x21;
   acc := acc + c;
}
'''

    return pseudocode

def get_name():
    return 'mult21AddHash32'

def main():
    print 'main called'
    return
