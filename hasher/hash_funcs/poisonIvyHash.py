
from utils.util import rcr
from utils.util import rol
from utils.util import *

def run(inStr,fName):
    #need a null at the end of the string
    if inStr[-1] != '\x00':
        inStr = inStr + '\x00'
    cx = 0xffff
    dx = 0xffff
    for b1 in inStr:
        bx = 0
        ax = ord(b1) ^ (cx & 0xff)
        cx =  ((cx>>8)&0xff) | ((dx&0xff)<<8)
        dx = ((dx>>8)&0xff) | 0x800
        while (dx & 0xff00) != 0:
            c_in = bx & 1
            bx = bx >> 1          
            ax, c_out = rcr(ax, 1, c_in, 16)
            if c_out != 0:
                ax = ax ^ 0x8320
                bx = bx ^ 0xedb8
            dx =  (dx&0xff) | (((((dx>>8)&0xff)-1)&0xff)<<8)
        cx = cx ^ ax
        dx = dx ^ bx
    dx = 0xffff & ~dx
    cx = 0xffff & ~cx
    return  0xffffffff & ((dx<<16) | cx)

def get_pseudocode():
    pseudocode_poisonIvyHash = '''Too hard to explain.\nString hash function from POISON IVY RAT.\nSee code for information'''
    return pseudocode_poisonIvyHash

def get_name():
    return 'posionIvyHash'

def main():
    print 'main called'
    return

if __name__ == '__main__':
    main()
