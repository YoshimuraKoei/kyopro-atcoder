# 知識

## deque

https://zenn.dev/yuto_mo/articles/3a381c4a4086e7

**deque → 両端に対する要素の追加や削除が高速に行えるデータ構造**
最大の特徴は **キュー処理やスタック処理を高速に行うことができること**

```python
from collections import deque

d = deque()
d = deque([1, 2, 3])

d.append(4)
d.alppendleft(0)

last = d.pop()
first = d.popleft()

d.extend([4, 5, 6])
d.extendleft([0, -1, -2])

d = deque([1, 2, 3, 4, 5], maxlen=5)
d.append(6) # 長さ制限を超えると反対側の要素が自動で削除される
```
