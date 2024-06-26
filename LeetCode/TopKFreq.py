import numpy as np
ans = [1,1,1,2,2,3]
num = 0
k = 2
res = dict()

for i in range(len(ans)):
    if ans[i] in res.keys():
        continue
    ctr = ans.count(ans[i])
    res[ans[i]] = ctr

x = list(res.values())
sorted_index = np.argsort(x)[-k:][::-1]
print(sorted_index)

keys = list(res.keys())
result = []
[result.append(keys[sorted_index[i]]) for i in range(k)]


print(result)