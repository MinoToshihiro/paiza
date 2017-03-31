# coding: utf-8
#https://paiza.jp/moshijo/challenge/moshijo_character_9

import sys

a = raw_input()
num = int(a)
l = len(list(a))
#print num,l

anslist = [num]

for i in range(l):
    anslist.append(round(anslist[-1],-(i+1)))

tmp = max(anslist)
if tmp > num:
	print int(tmp)
else:
	print num


'''
memo
元の数を一の位から順々に四捨五入して、その中から一番大きいものを選べばよい
ただし、例えば455だと
455→500→1000となり最大の数の桁が上がる場合もあるので
round(tmp,-i)とすると間違いになることに注意（これだと答えが500になる）
'''

