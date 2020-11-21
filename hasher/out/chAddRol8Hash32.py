from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = val ^ (ord(i) * 256)
        val = rol(val, 0x8, 32)
        val_hex = "%08x"%val
        valh_str = val_hex[4:6]
        valh = int(valh_str, 16)
        val = val ^ valh
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ch ^ c
   acc := ROL(acc, 8):
   acc := cl ^ ch;
}
'''

    return pseudocode

def get_name():
    return 'chAddRol8Hash32'

def main():
    print 'main called'
    return
