MOD = 1000000009
def mod(x):
    if x >= 0:
        return x % MOD
    else:
        return - ( - x % MOD)
n, k = map(int, input().split())
a = []
# b = []
for i in range(n):
    a.append(int(input()))
a.sort()
if a[n - 1] < 0:
    ans = 1
    if k % 2 == 1:
        for i in range(k):
            ans=mod(ans * a[n - i - 1])
    else:
        for i in range(k):
            ans = mod(ans * a[i])
elif a[n - 1] == 0:
    if k % 2 == 1:
        ans = 0
    else:
        if a[k - 1] == 0:
            ans = 0
        else:
            ans = 1
            for i in range(k):
                ans = mod(ans * a[i])
elif a[0] >= 0:
    ans = 1
    for i in range(k):
        ans = mod(ans * a[n-1-i])
else:
    if n == k:
        ans = 1
        for i in a:
            ans = mod(ans * i)
    else:
        q, p, ans = 0, n-1, 1
        w, e, r = 0, 0, 0
        fs = 0
        while k:
            if abs(a[q]) > abs(a[p]):
                if q > 0:
                    ans = mod(a[q - 1] * ans)
                    # b.append(a[q])
                if a[q] < 0:
                    fs += 1
                q += 1
                w = r
            else:
                if p < n-1:
                    ans = mod(a[p + 1] * ans)
                    # b.append(a[p])
                p -= 1
                e = r
            k -= 1
            r += 1
        if fs%2 == 1:
            if (a[q] * a[q - 1]) < (a[p] * a[p + 1]):
                # for i in range(len(b)):
                #     if b[i] == a[q - 1]:
                #         b[i] = a[p]
                #         break
                # b[w] = a[p]
                ans = mod(mod(ans * a[p]) * a[p + 1])
            else:
                # for i in range(len(b) - 1, -1, -1):
                #     if b[i] == a[p+1]:
                #         b[i] = a[q]
                #         break
                # b[e] = a[q]
                ans = mod(mod(ans * a[q]) * a[q - 1])
        else:
            # if q == 0:
            #     p += 1
            # if p == n-1:
            #     q -= 1
            ans = mod(mod(ans * a[p + 1]) * a[q - 1])
# for i in b:
#     ans = mod(ans * i)
print(ans)