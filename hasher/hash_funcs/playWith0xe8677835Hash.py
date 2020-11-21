from utils.util import *

def run(inString,fName):
    
    val = 0xFFFFFFFF
    for i in inString:
        val ^= ord(i)
        for j in range(0, 8):
            if (val&0x1) == 1:
                val ^= 0xe8677835
            val >>= 1
    return val ^ 0xFFFFFFFF



def get_pseudocode():
    pseudocode = '''
TBC
'''

    return pseudocode

def get_name():
    return 'playWith0xe8677835Hash'

def main():
    print 'main called'
    return
