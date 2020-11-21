from utils.util import *

def run(inString,fName):
    
    dllHash = 0
    for c in fName:
        dllHash = ror(dllHash, 0xd, 32)
        if ord(c) < 97:
            dllHash = int(dllHash) + ord(c)
        else:
            dllHash = int(dllHash) + ord(c) - 32
        dllHash = ror(dllHash, 0xd, 32)
    dllHash = ror(dllHash, 0xd, 32)
    dllHash = ror(dllHash, 0xd, 32)

    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = ror(val, 0xd, 32)
        val += ord(i)
    val = ror(val, 0xd, 32)
    val += dllHash
    if val >= 4294967296:
        val -= 4294967296
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROR(acc, 13);
   acc := acc + c;
}
acc := acc + ror13add(DllName);
'''

    return pseudocode

def get_name():
    return 'ror13AddHash32AddDll'

def main():
    print 'main called'
    return
