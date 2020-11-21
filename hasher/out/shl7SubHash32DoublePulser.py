from utils.util import *

def run(inString,fName):
    
    eax = 0
    edi = 0
    for i in inString:
        edi = 0xffffffff & (eax << 7)
        eax = 0xffffffff & (edi - eax)
        eax = eax + (0xff & ord(i))
    edi = 0xffffffff & (eax << 7)
    eax = 0xffffffff & (edi - eax)
    return eax



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   t0 = (acc << 7);
   t2 = t0 - t1;
   acc = t2 + c;
}
'''

    return pseudocode

def get_name():
    return 'shl7SubHash32DoublePulser'

def main():
    print 'main called'
    return
