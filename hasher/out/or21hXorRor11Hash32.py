from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    ors = 0
    for i in inString:
        ors = ord(i) | 33
        val = val ^ ors
        val = rol(val, 0xb, 32)
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   chr_or := chr | 21h;
   acc := acc ^ chr_or;
   acc := ROR(acc, 11);
}
'''

    return pseudocode

def get_name():
    return 'or21hXorRor11Hash32'

def main():
    print 'main called'
    return
