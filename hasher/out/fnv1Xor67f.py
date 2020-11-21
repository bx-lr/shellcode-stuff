from utils.util import *

def run(inString,fName):
    
    val = 0x811c9dc5
    for c in inString:
        val = (0x1000193 * (ord(c) ^ val)) & 0xffffffff
    return val ^ 0x67f



def get_pseudocode():
    pseudocode = '''
    acc = 0x811c9dc5
    for c in inString:
        acc = (0x1000193 * (ord(c) ^ acc)) & 0xffffffff
    return acc ^ 0x67f

    return acc
'''

    return pseudocode

def get_name():
    return 'fnv1Xor67f'

def main():
    print 'main called'
    return
