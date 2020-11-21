from utils.util import *

def run(inString,fName):
    
    dll_hash = 0
    for c in fName:
        dll_hash = ror(dll_hash, 0xd, 32)
        if ord(c) < 97:
            dll_hash = int(dll_hash) + ord(c)
        else:
            dll_hash = int(dll_hash) + ord(c) - 32

    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = ror(val, 0xd, 32)
        val += ord(i)
    val += dll_hash
    return val & 0xFFFFFFFF



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROR(acc, 13);
   acc := acc + c;
}
acc := acc + ror13add(dll_name);
'''

    return pseudocode

def get_name():
    return 'ror13AddHash32DllSimple'

def main():
    print 'main called'
    return
