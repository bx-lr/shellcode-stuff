from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val += ord(i)
        val = ror(val, 0xd, 32)
    val = ror(val, 0xd, 32)
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := acc + c;
   acc := ROR(acc, 13);
}
acc := ROR(acc, 13);
'''

    return pseudocode

def get_name():
    return 'addRor13HashOncemore32'

def main():
    print 'main called'
    return
