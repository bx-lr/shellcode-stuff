from utils.util import *

def run(inString,fName):
    
    crc32_table = [0] * 256
    for i in xrange(256):
        v = i << 24
        for j in xrange(8):
            if (v & 0x80000000) == 0:
                v = (2 * v) & 0xffffffff
            else:
                v = ((2 * v) ^ 0x4C11DB7) & 0xffffffff
        crc32_table[i] = v

    result = 0xffffffff
    for c in inString:
        result = (crc32_table[ ord(c.lower()) ^ ((result >> 24) & 0xff) ] ^ (result << 8)) & 0xffffffff

    return (result ^ 0xffffffff) & 0xffffffff


def get_pseudocode():
    pseudocode = '''crc32bzip2lower(inString, fName):
    crc32_table = [0] * 256
    for i in xrange(256):
        v = i << 24
        for j in xrange(8):
            if (v & 0x80000000) == 0:
                v = (2 * v) & 0xffffffff
            else:
                v = ((2 * v) ^ 0x4C11DB7) & 0xffffffff
        crc32_table[i] = v

    result = 0xffffffff
    for c in inString:
        result = (crc32_table[ ord(c.lower()) ^ ((result >> 24) & 0xff) ] ^ (result << 8)) & 0xffffffff

    return (result ^ 0xffffffff) & 0xffffffff
'''
    return pseudocode

def get_name():
    return 'crc32bzip2lower'

def main():
    print 'main called'
    return
