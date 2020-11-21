from utils.util import *

def run(inString,fName):
    
    '''Same as ror13AddHash32, but subtract 1 afterwards'''
    return ror13AddHash32(inString,fName) - 1



def get_pseudocode():
    pseudocode = ,fName):
    '''Same as ror13AddHash32, but subtract 1 afterwards'''
    return ror13AddHash32(inString,fName) - 1

pseudocode_ror13AddHash32 = '''acc := 0;
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
