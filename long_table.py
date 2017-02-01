# coding: utf-8
#長テーブルのうなぎ屋 (paizaランク B 相当)
#https://paiza.jp/learning/long-table


Snum, Gnum = map(int,raw_input().split())
data = []
for i in range(Gnum):
    data.append(map(int, raw_input().split()))

seat = [0]*Snum
pre_seat = []

#各グループごとにseat情報を保存し、席がかぶったときは前のseat情報をリロードする
for j in range(Gnum):
    pre_seat = seat[:]
    for mem in range(data[j][0]):
        if  seat[(data[j][1]-1+mem)%(Snum)] == 0:
            seat[(data[j][1]-1+mem)%(Snum)] = 1
        else:
            seat = pre_seat
            break
        #print pre_seat
        #print seat
print sum(seat)        


'''
メモ
pre_seat=seat[:]のところでpre_seat=seatとしてしまうと、pre_seatとseatが同一のものと扱われ、
seatの値が変わるたびにpre_seatの値も変更されてしまう
→pre_seat=seat[:]と書くと配列コピーになるので、seatが変更されてもpre_seatは元の値を保持する
'''