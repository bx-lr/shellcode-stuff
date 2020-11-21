from utils.util import *

def run(inString,fName):
    
    if inString is None:
        return 0

    v4, v8 = 0, 1
    for ltr in inString:
        v8 = (ord(ltr) + v8) % 0x0FFF1
        v4 = (v4 + v8) % 0x0FFF1
    return (v4 << 0x10)|v8



def get_pseudocode():
    pseudocode = '''
acc_1 := 0
acc_2 := 0
for c in input_string {
    acc_2 = (acc_2 + c) % 0x0FFF1
    acc_1 = (acc_1 + acc2) % 0x0FFF1
}
return (acc_1 << 0x10) | acc2
'''

    return pseudocode

def get_name():
    return 'dualaccModFFF1Hash'

def main():
    print 'main called'
    return
