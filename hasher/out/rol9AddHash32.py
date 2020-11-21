from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = rol(val, 0x9, 32)
        val += ord(i)
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := ROL(acc, 9):
   acc := acc + c;
}
'''

    return pseudocode

def get_name():
    return 'rol9AddHash32'

def main():
    print 'main called'
    return
