from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = rol(val, 0x7, 32)
        val += (ord(i) ^ 2)
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROL(acc, 7):
   acc := acc + (c ^ 2);
}
'''

    return pseudocode

def get_name():
    return 'rol7AddXor2Hash32'

def main():
    print 'main called'
    return
