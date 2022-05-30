import random
import math

def sifting(a, b):
    global data
    ans = []
    for i in data:
        if i >= a and i <= b:
            ans.append(i)
    return ans

data = []
while True:
    try:
        data.append(int(input().split(',')[0]))
    except EOFError:
        break
print(min(i for i in data), max(i for i in data))
ans301_400 = sifting(320, 396)
ans401_500 = sifting(397, 473)
ans501_600 = sifting(474, 548)
ans601_700 = sifting(549, 623)
print(len(ans601_700), len(ans501_600), len(ans401_500), len(ans301_400))
S = 100 + 7 % 21
count = 0
answer = random.sample(ans301_400, math.floor(len(ans301_400)*S/len(data)))
count += math.floor(len(ans301_400)*S/len(data))
answer.extend(random.sample(ans401_500, math.floor(len(ans401_500)*S/len(data))))
count += math.floor(len(ans401_500)*S/len(data))
answer.extend(random.sample(ans501_600, math.floor(len(ans501_600)*S/len(data))))
count += math.floor(len(ans501_600)*S/len(data))
print(S, count)
answer.extend(random.sample(ans601_700, S - count))
print(min(i for i in answer), max(i for i in answer))
print(len(answer))
print('____')
print(', '.join(list(map(str, answer))))
