# https://codeforces.com/problemset/problem/978/B
n = int(input())
x = input()
c = 0
for i in range(n-2):
    if x[i] == x[i+1] == x[i+2] == 'x':
        c += 1
print(c)
