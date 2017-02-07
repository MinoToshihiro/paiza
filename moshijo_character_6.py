# coding: utf-8
#https://paiza.jp/moshijo/challenge/moshijo_character_6

N = input()
row = [int(x) for x in list(map(int,raw_input().split()))]
col = [int(x) for x in list(map(int,raw_input().split()))]
#print row
#print col

ans = []
for i in range(N):
    for j in range(N):
        ans.append(row[j]+col[i])
#print ans

for i in range(N):
    for j in range(N):
        print ans[i*N+j],
    print 

'''
rowとcolこれであってるのか… 逆か…？

'''    