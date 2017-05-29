# coding: utf-8
#https://paiza.jp/learning/book_sort
#いわゆる選択ソート

N = input()
data = map(int,raw_input().split())

'''
#入れ替えする関数
def Replace(list,pos):
	target = pos #入れ替え先
	num = N #入れ替え先の数
	#pos以降の最小値を探し、posと異なれば入れ替える
	for i in range(pos,len(list)):
		if num > list[i]:
			target = i
			num = list[i]
	if target == pos:
		return 0
	else:
		list[pos],list[target] = list[target],list[pos]
		return 1

def Replace2(list,pos):
	target = list.index(min(list[pos:]))
	if target == pos:
		return 0
	else:
		list[pos],list[target] = list[target],list[pos]
		return 1

def Replace3(list,pos): 
	target = pos
	for i in range(pos,len(list)):
		if list[target] > list[i]:
			target = i
	if target == pos:
		return 0
	else:
		list[pos],list[target] = list[target],list[pos]
		return 1

steps = 0
for i in range(N):
	#steps += Replace(data,i)
	#steps += Replace2(data,i)
	steps += Replace3(data,i)

print steps
'''


index = [0]*N
for i in range(N):
	index[data[i]-1] = i
#print data
#print index

steps = 0
for i in range(N):
	if data[i]-1 != i:
		tmp = index[i]
		index[i],index[data[i]-1] = index[data[i]-1],index[i]
		data[i],data[tmp] = data[tmp],data[i]
		steps += 1
	print data
	print index

print steps

'''
memo
解答解説
https://www.slideshare.net/ginoaki/3-25-74598164
まじめに実装すると上のReplace関数のようにどれもfor i in range(N)の２重ループで計算量がO(N^2)になる
なので、本の番号順にならべたときのiのリストをindexとして、
i番目の本とiの本を交換(data)
i番目の位置とiの本の位置を交換(index)
この２つを同時に行うことで、計算量をO(N)に抑えることができる、らしい（入れ替え先を探すためのfor文がなくなる分速くなる）
'''