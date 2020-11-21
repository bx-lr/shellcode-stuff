from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = ror(val, 0xb, 32)
        val += ord(i)
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROR(acc, 11);
   acc := acc + c;
}
'''

    return pseudocode

def get_name():
    return 'ror11AddHash32'

def main():
    print 'main called'
    return
