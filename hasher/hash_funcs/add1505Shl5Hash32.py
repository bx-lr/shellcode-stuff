from utils.util import *

def run(inString,fName):
    
  val = 0x1505
  for ch in inString:
    val += (val << 5)
    val &= 0xFFFFFFFF
    val += ord(ch)
    val &= 0xFFFFFFFF
  return val



def get_pseudocode():
    pseudocode = '''val := 0x1505;
for c in input_string {
   val := val +  (val << 5);
   val := val + c;
}
'''

    return pseudocode

def get_name():
    return 'add1505Shl5Hash32'

def main():
    print 'main called'
    return
