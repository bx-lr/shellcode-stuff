from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = val ^ ord(i)
        val = rol(val, 0x9, 32)
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := acc ^ c;
   acc := ROL(acc, 9):
}
'''

    return pseudocode

def get_name():
    return 'xorRol9Hash32'

def main():
    print 'main called'
    return
