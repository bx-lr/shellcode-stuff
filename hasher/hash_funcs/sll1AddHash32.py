from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        b = ord(i)
        b = 0xff & (b | 0x60)
        val = val + b
        val = val << 1
        val = 0xffffffff & val
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
    acc = acc + (c | 0x60);
    acc = acc << 1;
}
'''

    return pseudocode

def get_name():
    return 'sll1AddHash32'

def main():
    print 'main called'
    return
