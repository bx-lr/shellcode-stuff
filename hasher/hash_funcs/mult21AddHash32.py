from utils.util import *

def run(inString,fName):
    
    acc = 0
    for i in inString:
        acc = 0xffffffff & (acc * 0x21)
        acc = 0xffffffff & (acc + ord(i))
    return acc




def get_pseudocode():
    pseudocode = '''mul32AddHash(inString,fName):
    acc = 0
    for i in inString:
        acc = 0xffffffff & (acc * 0x21)
        acc = 0xffffffff & (acc + ord(i))
    return acc
'''
    return pseudocode

def get_name():
    return 'mult21AddHash32'

def main():
    print 'main called'
    return
