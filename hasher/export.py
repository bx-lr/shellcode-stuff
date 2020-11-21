

def main():
    fd = open('test.txt', 'r')
    data = fd.read()
    fd.close()
    res = [i for i in range(len(data)) if data.startswith('def ', i)]
    funcs = []



    for i in range(0, len(res)-1):
        start = res[i]
        stop = res[i+1]

        funcs.append(data[start:stop])

    for f in funcs:
        name  = f[f.find('def ')+4: f.find('(')]
        code = f[f.find(':')+1:f.find('pseudo')]
        tmp = 'pseudocode_%s = ' % name
        if f.find(tmp) < 0:
            pseudo = "'no pseudocode'"
        else:
            pseudo = f[f.find(tmp)+len(tmp):-1]
        template = '''from utils.util import *

def run(inString,fName):
    %s

def get_pseudocode():
    pseudocode = %s
    return pseudocode

def get_name():
    return '%s'

def main():
    print 'main called'
    return
''' % (code, pseudo, name)
        #print template
        fd  = open('out\\'+name+'.py', 'w')
        fd.write(template)
        fd.close()

if __name__ == '__main__':
    main()