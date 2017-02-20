# coding: utf-8
#https://paiza.jp/moshijo/challenge/moshijo_character_8

import sys

c,p = raw_input().split()
c = list(c.split("/"))
del c[0] #cは/から始まるので最初に何も無い要素が出来る
p = list(p.split("/"))
#print c
#print p

for i in range(len(p)):
	if p[i] == "..":
		if len(c) > 0:
			del c[len(c)-1]
	elif p[i] == ".":
		pass
	else:
		c.append(p[i])


if len(c) == 0:
	print "/"
else:
	for i in range(len(c)):
		sys.stdout.write("/")
		sys.stdout.write(c[i])

'''
memo
ファイル階層の頂点である / ディレクトリの親ディレクトリは / 自身を指すので、..のときには
if len(c) > 0:
であるかどうか確認する必要がある。
ｃの要素が何も無い場合、出力は/だけになるので別処理する

for文で何もしないときはpass
'''