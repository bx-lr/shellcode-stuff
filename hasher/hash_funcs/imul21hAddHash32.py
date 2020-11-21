from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0x1505
    for i in inString:
        val = (val * 0x21) & 0xFFFFFFFF
        val = (val + (ord(i) & 0xFFFFFFDF)) & 0xFFFFFFFF
    return val



def get_pseudocode():
    pseudocode = '''acc := 0x1505;
for c in input_string {
   acc := acc * 21h;
   acc := acc + (c & 0xFFFFFFDF);
}
acc := SHL(acc, 7) - acc
'''

    return pseudocode

def get_name():
    return 'imul21hAddHash32'

def main():
    print 'main called'
    return
