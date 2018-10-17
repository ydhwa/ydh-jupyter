# 숙제 (1).
# Unix의 cp(copy) 명령어를 python으로 구현하시오.
# 파일을 찾지 못했을 경우의 예외처리까지 구현해보았다.

import sys

try:
    copyf = open(sys.argv[1], 'r')
    pastef = open(sys.argv[2], 'w')
    while 1:
        line = copyf.readline()
        if not line: break
        pastef.write(line)
    copyf.close()
    pastef.close()
except:
    print ('error: file not found!')
