from utils.util import *

def run(inString,fName):
    
    '''Same as ror13AddHash32, but subtract 1 afterwards'''
    if inString is None:
        return -1
    val = 0
    for i in inString:
        val = ror(val, 0xd, 32)
        val += ord(i)
    return val -1

def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROR(acc, 13);
   acc := acc + c;
}
acc := acc - 1;
'''

    return pseudocode

def get_name():
    return 'ror13AddHash32Sub1'

def main():
    print 'main called'
    return
