n = int(input())
answer = [0,1,2]
if n < 3:
  print(answer[n])
else:
  #n=4부터 여기로 들어옴
  for i in range(3, n+1):
    answer.append((answer[i-1]+answer[i-2])%10007)
  print(answer[n]%10007)