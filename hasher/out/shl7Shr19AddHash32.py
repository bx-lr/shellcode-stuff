from utils.util import *

def run(inString,fName):
    
    val = 0
    for i in inString:
        edx = 0xffffffff & (val << 7)
        ecx = 0xffffffff & (val >> 0x19)
        eax = edx | ecx
        t = 0xff & ord(i)
        val = eax + t
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   t0 = (acc << 7);
   t1 = (acc >> 0x19);
   t2 = t0 | t1;
   acc = t2 + c;
}
'''

    return pseudocode

def get_name():
    return 'shl7Shr19AddHash32'

def main():
    print 'main called'
    return
