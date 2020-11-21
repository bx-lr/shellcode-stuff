from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    dllHash = 0
    for i in fName:
        dllHash = ror(dllHash, 0xd, 32)
        b = ord(i)
        if b >= 0x61:
            b -= 0x20
        dllHash += b
        dllHash = 0xffffffff & dllHash
    for i in inString:
        val = ror(val, 0xd, 32)
        val += ord(i)
        val = 0xffffffff & val
    return 0xffffffff & (dllHash + val)





def get_pseudocode():
    pseudocode = '''
acc := 0
dllhash := 0
for i in dllname {
   dllhash := ROR(acc, 13);
   dllhash := dllhash + toupper(c);
}
for i in input_string {
   acc := ROR(acc, 13);
   acc := acc + toupper(c);
}
return  acc + dllhash
'''

# as seen in Neutrino Bot launcher
    return pseudocode

def get_name():
    return 'hash_ror13AddUpperDllnameHash32'

def main():
    print 'main called'
    return
