# coding: utf-8

def origami(n,orime):
	if n>1:
		orime2 = orime[:]
		orime2[len(orime2)/2] = 1
		next_orime = orime + [0] + orime2 
		return origami(n-1,next_orime)
	else:
		return orime


if __name__ == "__main__":
	N = input()
	orime = [0]
	ans = origami(N,orime)
	print ''.join(map(str,ans))



"""
n=1:0
n=2:001
n=3:0010011
n=4:001001100011011
...
n回目の折り目
=(n-1)回目の折り目＋谷折＋(n-1)回目の折り目の真ん中を山折にしたもの
と表せるので、再帰で表現

"""