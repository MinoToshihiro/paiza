# coding: utf-8

import sys
num = 0

def print_state(state):
	#結果の出力
	if len(state["a"])>0:
		state["a"].sort(reverse=True)
		print ' '.join(map(str,state["a"]))
	else:
		print "-"

	if len(state["b"])>0:
		state["b"].sort(reverse=True)
		print ' '.join(map(str,state["b"]))
	else:
		print "-"

	if len(state["c"])>0:
		state["c"].sort(reverse=True)
		print ' '.join(map(str,state["c"]))
	else:
		print "-"

def hanoi(n,here,work,to,state,time):
	global num 
	#n番目をhereからtoへ移動する(workは残りのスペース)
	if n > 0:
		#n-1番目までをすべてworkへ移動する
		hanoi(n-1,here,to,work,state,time)

		num += 1
		#n番目をhereからtoへ移動する
		#print "step:"+str(num)+" "+str(n)+"th:"+here+"->"+to
		state[here].remove(n)
		state[to].append(n)
		#print state
		if num == time:
			print_state(state)
			sys.exit()

		#workにあるn-1個をtoへ移動させる
		hanoi(n-1,work,here,to,state,time)


if __name__ == "__main__":

	n,t = map(int,raw_input().split())
	state = {"a":[i for i in range(1,n+1)], "b":[], "c":[]} #各ステップでの状態
	#print state
	hanoi(n,"a","b","c",state,t)


