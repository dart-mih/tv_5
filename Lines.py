import math
import matplotlib.pyplot as plt
import seaborn as sns

data = [320, 330, 362, 362, 372, 377, 378, 379, 382, 383, 386, 390, 391, 392, 397, 400, 404, 405, 406, 406, 407, 411, 411, 414, 418, 418, 419, 421, 421, 422, 423, 426, 426, 427, 428, 428, 429, 429, 434, 434, 436, 437, 438, 438, 440, 442, 442, 443, 443, 446, 448, 449, 452, 452, 452, 453, 457, 458, 458, 459, 461, 462, 463, 463, 463, 463, 470, 470, 470, 474, 475, 475, 480, 481, 483, 483, 493, 493, 493, 495, 496, 498, 500, 501, 502, 506, 510, 512, 517, 518, 521, 523, 525, 525, 525, 532, 536, 541, 544, 544, 548, 553, 576, 585, 591, 593, 623]
data.sort()
print(data)
set_data = list(set(data))
set_data.sort()
print(len(set_data))
for i in set_data:
    print(i, '&', data.count(i), '&', str(data.count(i)) + '/107 &')
k = math.floor(1 + math.log2(len(data)))
h = (max(data) - min(data))/k
print(h)
print('----')
count = min(data) + h
last_step = min(data)-1
buf_count = 0
s = 0
v = []
while count <= max(data):
    for i in data:
        if i <= count and i > last_step:
            buf_count += 1
    v.append([last_step + (count - last_step)/2, buf_count])
    s += buf_count
    print(str(last_step) + ';'  + str(count), '&', buf_count, '&' , str(buf_count) + '/107 &')
    last_step = count
    count += h
    buf_count = 0
for i in data:
    if i <= count and i > last_step:
        buf_count += 1

v.append([last_step + (count - last_step)/2, buf_count])
print(str(last_step) + ';'  + str(count), '&', buf_count, '&' , str(buf_count) + '/107 &')
print(v)
v[0][0] = 320
myhex = '#660099'
fig, ax = plt.subplots()


#for i in v:
 #   plt.scatter(i[0], i[1], color=myhex)
for i in range(len(v)-1):
    plt.plot([v[i][0], v[i+1][0]],[v[i][1]/107, v[i+1][1]/107], color=myhex, marker = 'o')
ax.set_xlabel('Середины интервалов')
ax.set_ylabel('Относительные частоты')
grid1 = plt.grid(True)   # линии вспомогательной сетки
plt.title("Графический полигон относительных частот")
plt.show()

fig, ax = plt.subplots()
for i in range(len(v)-1):
    plt.plot([v[i][0], v[i+1][0]],[v[i][1], v[i+1][1]], color=myhex, marker = 'o')
ax.set_xlabel('Середины интервалов')
ax.set_ylabel('Абсолютные частоты')
grid1 = plt.grid(True)   # линии вспомогательной сетки
plt.title("Графический полигон абсолютных частот")
plt.show()

fig, ax = plt.subplots()
cur = min(data)
count = 0
plt.plot([300, 320], [0, 0], color=myhex)
for i in range(len(v)-1):
    plt.plot([cur, cur + h], [v[i][1] + count, v[i][1]+count], color=myhex)
    plt.scatter(cur, v[i][1]+count, color=myhex)
    count += v[i][1]
    cur += h
plt.plot([cur, 650], [v[len(v)-1][1] + count,v[len(v)-1][1] + count], color=myhex)
plt.scatter(cur, v[len(v)-1][1] + count, color=myhex)
ax.set_xlabel('Середины интервалов')
ax.set_ylabel('Абсолютные частоты')
plt.xlim(300, 650)
grid1 = plt.grid(True)   # линии вспомогательной сетки
plt.title("Эмпирическая функция для абсолютных частот")
plt.show()


fig, ax = plt.subplots()
cur = min(data)
count = 0
plt.plot([300, 320], [0, 0], color=myhex)
for i in range(len(v)-1):
    plt.plot([cur, cur + h], [(v[i][1] + count)/107, (v[i][1]+count)/107], color=myhex)
    plt.scatter(cur, (v[i][1]+count)/107, color=myhex)
    count += v[i][1]
    cur += h
plt.plot([cur, 650], [(v[len(v)-1][1] + count)/107, (v[len(v)-1][1] + count)/107], color=myhex)
plt.scatter(cur, (v[len(v)-1][1] + count)/107, color=myhex)
ax.set_xlabel('Середины интервалов')
ax.set_ylabel('Относительные частоты')
plt.xlim(300, 650)
grid1 = plt.grid(True)   # линии вспомогательной сетки
plt.title("Эмпирическая функция для относительных частот")
plt.show()


new_data = { "Середины интервалов": data, "w": [1/107 for i in range(len(data))]}
sns.histplot(new_data, x = "Середины интервалов",weights= "w", bins=7)
plt.title("Гистограмма для относительных частот")
#f.set_yticks("Относительные частоты")
plt.show()

new_data = { "Середины интервалов": data}
f = sns.histplot(new_data, bins=7, x = "Середины интервалов")
plt.title("Гистограмма для абсолютных частот")
#f.set_yticks("Абсолютные частоты")
#f.set_xticks("Середины интервалов")
plt.show()



