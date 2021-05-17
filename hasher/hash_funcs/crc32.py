from utils.util import *

def run(inString,fName):
    
    return 0xffffffff & (zlib.crc32(inString))


def get_pseudocode():
    pseudocode = '''crc32(inString,fName):
    return 0xffffffff & (zlib.crc32(inString))
'''
    return pseudocode

def get_name():
    return 'crc32'

def main():
    print 'main called'
    return
