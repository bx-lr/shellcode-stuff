from utils.util import *

def run (inString,fName):
    if inString is None:
        return 0
    ecx = 0
    eax = 0
    for i in inString:
        eax = eax | ord(i)
        ecx = ecx ^ eax
        ecx = rol(ecx, 0x3, 32)
        ecx += 1
        eax = 0xffffffff & (eax << 8)
    return ecx

def get_pseudocode():
    pseudocode_rol3XorEax = '''eax := 0;
ecx := 0;
for c in input_string {
    eax := eax | c ;
    ecx := ecx ^ eax;
    ecx := ROL(ecx, 0x3);
    ecx : ecx + 1;
    eax := 0xffffffff & (eax << 8);
};
return ecx;
'''
    return pseudocode_rol3XorEax

def get_name():
    return 'rol3XorEax'

def main():
    print 'main called'


if __name__ == '__main__':
    main()