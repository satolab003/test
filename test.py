#!/usr/bin/python
# coding: UTF-8

import sys
from operator import itemgetter

file_name = input()

lines = []
f = open(file_name)
line = f.readline() # 1行を文字列として読み込む(改行文字も含まれる)
while line:
    if ":" in line:
        a = line.split(":")
        a[1] = a[1].rstrip('\n')
        lines.append(a)
    else:
        num =line
    line = f.readline()
f.close

m = int(num)
lines_i = [[int(b[0]),str(b[1])] for b in lines]
result = []

count = 0
for one in lines_i:
    if m % int(one[0]) == 0:
        result.append(one)
        #print(one)
        count += 1
    else:
        one_n = m

if count == len(lines_i):
       print(one_n)

result_new = sorted(result, key=itemgetter(0))
result_new = [v[1] for v in result_new]


maped_list = map(str, result_new)
#print(maped_list)  #mapで要素すべてを文字列に
mojiretu = ''.join(maped_list)
print(mojiretu)