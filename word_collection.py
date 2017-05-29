# coding: utf-8
#https://paiza.jp/learning/word_collection

N,M = map(int,raw_input().split())
data = []
for i in range(N):
	data.append(raw_input().split())
#print data
queries = []
for i in range(M):
	queries.append(raw_input())
#print queries

'''
#ans1
for i in range(M):
	score = 0
	for j in range(N):
		if data[j][0].startswith(queries[i]):
			score += int(data[j][1])
	print score
'''

#ans2
def maketrie(*words):
	root = dict()
	for word in words:
		current_dict = root
		for letter in word[0]:
			#setdefaultで辞書オブジェクトのキーが存在しなくてもエラーが出ない
			current_dict = current_dict.setdefault(letter,{'sum':0})
			current_dict['sum'] += int(word[1])
	return root

def intrie(trie,word):
	current_dict = trie
	for letter in word:
		if letter in current_dict:
			current_dict = current_dict[letter]
		else:
			return {'sum':0} #クエリ文字列がtrieに存在しないとき
	
	return current_dict

trie = maketrie(*data)
for i in range(M):
	print intrie(trie,queries[i])['sum']


'''
memo
解答解説
http://paiza.hatenablog.com/entry/2017/04/06/%E3%80%8Cpaiza%E5%B0%B1%E6%B4%BB%E5%8B%89%E5%BC%B7%E4%BC%9A%E3%80%8D%E3%81%A7%E5%87%BA%E9%A1%8C%E3%81%95%E3%82%8C%E3%81%9F%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E5%95%8F%E9%A1%8C
ans1では文字列と価値の一覧に対して、各クエリごとに全ての文字列と前方一致を探しており、
計算量は
"一覧内の文字列(N)×前方一致の文字列の長さ(Si)×クエリ総数(M)"
となる
一方ans2ではトライ木と呼ばれる辞書検索等で使われるものを用いており、
計算量は
"一覧内の文字列(N)×各単語の文字数"
となる

まずmaketrieでrootに対して、文字列の文字を１つずつ与える
このとき、辞書オブジェクトとしてsumを用意し、文字を加えるごとにsumの値に価格を足していく
これにより、後のクエリと文字列が完全一致したところのsumに価格の合計が入るようになる
intrieでは、クエリで与えられた文字列に対して前方から一文字ずつ確認し、
trie内にあればそれをたどっていくようにしている（無ければ０を返す）
最後にcurrent_dictのsumをprintして値を出す

参考：http://qiita.com/IshitaTakeshi/items/04e6fcf7c9d52082d4de
さらにLOUDSという表記をつかってメモリ消費を抑えるなど
参考：http://d.hatena.ne.jp/takeda25/20120421/1335019644
'''