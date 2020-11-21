from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0
    val = 0
    for i in inString:
        val = val * 131
        val += ord(i)
    val = val & 0xFFFFFFFF
    return val



def get_pseudocode():
    pseudocode = '''acc := 0;
for c in input_string {
   acc := acc * 83h:
   acc := acc + c;
}
'''

    return pseudocode

def get_name():
    return 'imul83hAdd'

def main():
    print 'main called'
    return
