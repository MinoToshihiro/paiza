# coding: utf-8
#https://paiza.jp/moshijo/challenge/moshijo_character_7

N = input()
data = []
for i in range(N):
	data.append(map(int,raw_input().split()))
#print data
M = input()
buy = []
for i in range(M):
	buy.append(map(int,raw_input().split()))
#print buy
#print N,M

for i in range(M):
	price = 0
	discount = 0
	discount = buy[i][1] // data[buy[i][0]-1][1]
	price = data[buy[i][0]-1][0] * buy[i][1] - discount * data[buy[i][0]-1][2]
	print price


'''
memo
//で小数点以下を計算しない除算
buy[i][0]に入っている番号はdataのリストの番号とは1ズレるので、priceの計算の際に修正する
ただしbuy自体のリスト番号とbuy[i][0]の番号も別物であることに注意する
'''