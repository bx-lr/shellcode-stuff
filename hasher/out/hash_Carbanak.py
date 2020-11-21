from utils.util import *

def run(inString,fName):
    
    a2 = map(ord, inString)
    ctr = 0
    for i in a2:
        ctr = (ctr << 4) + i
        if (ctr & 0xF0000000):
            ctr = (((ctr & 0xF0000000) >> 24) ^ ctr) & 0x0FFFFFFF

    return ctr



def get_pseudocode():
    pseudocode = '''
    acc_1 = 0
    for c in input_string:
        acc_1 = (acc_1 << 4) + c
        if (acc_1 & 0xF0000000):
            acc_1 = (((acc_1 & 0xF0000000) >> 24) ^ acc_1) & 0x0FFFFFFF
    return acc_1
'''

    return pseudocode

def get_name():
    return 'hash_Carbanak'

def main():
    print 'main called'
    return
