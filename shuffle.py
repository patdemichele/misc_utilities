import sys
import random
import re

def fix(s):
    if len(s) == 0 or s[-1] != '\n':
        return s + '\n'
    return s
if __name__ == '__main__':
    filename = sys.argv[1]
    f = open(filename, 'r+')
    static = []
    shuffle = []
    count = 0
    for line in f:
        if count < 3: static.append(line)
        else: shuffle.append(line)
        count += 1
    random.shuffle(shuffle)
    f.seek(0)
    for s in static:
        f.write(s)
    for i in range(len(shuffle)):
        to_write = fix(re.sub("\[[0-9]*\]", "["+str(i+1)+"]",str(shuffle[i])))
        f.write(to_write)
        
    f.close()
