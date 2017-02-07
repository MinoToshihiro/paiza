# coding: utf-8
#https://paiza.jp/moshijo/challenge/moshijo_character_5


import sys

code = map(int,raw_input().split())
key = raw_input()
num = [int(x) for x in list(str(raw_input()))]

codemap = []
for i in range(10):
    codemap.append([i,code[i]])
#print codemap

ans = []
if key == "encode":
    for i in range(len(num)):
        for j in range(10):
            if num[i] == codemap[j][0]:
                ans.append(codemap[j][1])
elif key == "decode":
    for i in range(len(num)):
        for j in range(10):
            if num[i] == codemap[j][1]:
                ans.append(codemap[j][0])
else:
    print "Error"
    
for a in range (len(ans)):
    sys.stdout.write(str(ans[a]))

'''
メモ
num = [int(x) for x in list(str(raw_input()))]を
num = [int(x) for x in list(str(input()))]
としてしまうと0から始まる数字に対して対応できなくなるので、数字ではなく文字列として取得するのがよい

'''