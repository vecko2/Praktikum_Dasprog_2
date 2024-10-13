N = int(input())
B = list(map(int, input().split()))
hasil = 1

for i in range(N):
    for j in range(i+1, N):
        if B[i] != B[j]:
            hasil *= B[i] ^ B[j]
        else:
            hasil = 0
            break
        
print(hasil)


