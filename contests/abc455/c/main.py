N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
A.reverse()

dic = {}
for a in A:
  if a not in dic:
    dic[a] = 0
  dic[a] += 1

sortlist = []
for a in dic:
    index = a * dic[a]
    sortlist.append(index)

sortlist.sort()
sortlist.reverse()

counter = 0
summ = 0
i = 0
while counter <= K-1:
  if len(sortlist) <= i:
    break;
  counter += 1
  summ += sortlist[i]
  i += 1

print(sum(sortlist)-summ)
