from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString + "\x00":
        val = (val & 0xffffff00) + ((val + ord(i)) & 0xff)
        val = ror(val, 0x4, 32)
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string_with_trailing_NULL {
   acc := (acc & 0xffffff00) + ((acc + c) & 0xff);
   acc := ROR(acc, 4):
}
'''


    return pseudocode

def get_name():
    return 'addRor4WithNullHash32'

def main():
    print 'main called'
    return
