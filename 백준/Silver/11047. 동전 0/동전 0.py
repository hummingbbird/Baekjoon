# https://www.acmicpc.net/problem/11047
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [0] * n
for i in range(n):
  coins[i] = int(input())

coins.sort(reverse=True)

cnt=0
for coin in coins:
  if k-coin < 0:
    continue
  else:
    cnt += k//coin
    k -= (k//coin)*coin

print(cnt)