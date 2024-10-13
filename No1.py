t = int(input())
arr = []

for _ in range(t):
    n, k = map(int, input().split()) 
    A = list(map(int, input().split())) 
    q = int(input()) 

    jumlah_saat_ini = sum(A[:k])
    max_sum = jumlah_saat_ini
    min_sum = jumlah_saat_ini 

    for i in range(1, k + 1):  
        jumlah_saat_ini = sum(A[:i]) 
        max_sum = max(max_sum, jumlah_saat_ini)
        min_sum = min(min_sum, jumlah_saat_ini)
        for j in range (1, n - i + 1):
            jumlah_saat_ini = jumlah_saat_ini - A[j - 1] + A[j + i - 1]
            max_sum = max(max_sum, jumlah_saat_ini)
            min_sum = min(min_sum, jumlah_saat_ini)


    if q == 1:
       arr.append(max_sum)
    elif q == 2: 
        arr.append(min_sum)

for i in arr:
    print(i)
