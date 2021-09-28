#  Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

l = []
print("Listede kaç eleman olacağını girin:")
n = int(input())
i=1

for _ in range(n):
    m = []
    print("Listenin", i , ". elemanında kaç eleman olacağını girin:")
    nn = int(input())
    print("Elemanları girin:")
    for _ in range(nn):
        t = int(input())
        m.append(t)
    
    if type(m) == list:
        m.reverse()

    l.append(m)
    i += 1
l.reverse()
print(l)
