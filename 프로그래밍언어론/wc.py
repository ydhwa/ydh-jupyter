# 숙제 (2).
# Unix의 wc 명령어를 python으로 구현하시오.
# 파일을 찾지 못했을 경우의 예외처리까지 구현해보았다.
# wc 명령어는 file의 라인 수, 단어 수를 구하여 출력시킨다.
# 단어는 공백으로 구분된 스트링이라고 가정한다.
# 대소문자 구분은 하지 않았다.

import sys

try:
    dic = {}
    linecount = 0
    f = open(sys.argv[1], 'r')
    for line in f:
        line = line.replace('\n', '')
        linecount += 1
        words = line.split(' ')
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    print ('Lines: ', linecount)
    print ('----- Words -----')
    for word in dic:
        print (word, dic[word])
    f.close()
except:
    print ('error: file not found!')
