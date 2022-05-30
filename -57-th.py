import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

data = [320, 330, 362, 362, 372, 377, 378, 379, 382, 383, 386, 390, 391, 392, 397, 400, 404, 405, 406, 406, 407, 411, 411, 414, 418, 418, 419, 421, 421, 422, 423, 426, 426, 427, 428, 428, 429, 429, 434, 434, 436, 437, 438, 438, 440, 442, 442, 443, 443, 446, 448, 449, 452, 452, 452, 453, 457, 458, 458, 459, 461, 462, 463, 463, 463, 463, 470, 470, 470, 474, 475, 475, 480, 481, 483, 483, 493, 493, 493, 495, 496, 498, 500, 501, 502, 506, 510, 512, 517, 518, 521, 523, 525, 525, 525, 532, 536, 541, 544, 544, 548, 553, 576, 585, 591, 593, 623]
data.sort()

h = 43.285714285714285

minimum = min(data)
curb = minimum
cur = minimum + h
count = 0
all_count = 0
mid_arr = []
count_arr = []
p_arr = []
for i in data:
    if i <= cur:
        count += 1
    else:
        all_count += count
        print(str(curb) +"-"+str(cur), (curb+cur)/2, count, '{}/107'.format(count), all_count, sep="&", end = "&")
        print()
        mid_arr.append((curb+cur)/2)
        count_arr.append(count)
        p_arr.append(count/107)
        curb = cur
        cur += h

        count = 1
all_count += count
mid_arr.append((curb+cur)/2)
count_arr.append(count)
p_arr.append(count/107)
print(str(curb) + "-" + str(cur), (curb + cur) / 2, count, '{}/107'.format(count), all_count, sep="&",
      end="&")
x_mid = 0
print("\n_________________")
for i in range(len(mid_arr)):
    x_mid += mid_arr[i]*count_arr[i]
x_mid /= 107
print("Выборочное среднее: ", x_mid)
x_dis = 0
for i in range(len(mid_arr)):
    x_dis += pow((mid_arr[i] - x_mid), 2)*count_arr[i]
x_dis /= 107
print("Выборочная депрессия: ", x_dis)
x_s = 107*x_dis/(106)
print("Исправленная тервером выборочная депрессия: ", x_s)
print("СКО: ", pow(x_dis,0.5))
print("Исправленное СКО: ", pow(x_s, 0.5))
print("Погрешность выборочных депрессий: ", abs(x_dis - x_s))
print("Погрешность СКО: ", abs(pow(x_dis,0.5) - pow(x_s, 0.5)))

print("___________")
v_i = []
for j in range(1, 5):
    S = 0
    for i in range(len(mid_arr)):
        S += pow(mid_arr[i], j)*p_arr[i]
    v_i.append(S)
print(p_arr, sum(p_arr))
print(v_i)
mu_3 = v_i[2] - 3*v_i[1]*v_i[0]+2*v_i[0]*v_i[0]*v_i[0]
mu_4 =  v_i[3]-4*v_i[2]*v_i[0]+6*v_i[1]*v_i[0]*v_i[0] - 3*pow(v_i[0], 4)
print("Центральный момент третьего порядка: ", mu_3)
print("Центральный момент четвертого порядка: ", mu_4)
print(pow(pow(x_dis,0.5), 3))
a_star = mu_3/pow(pow(x_dis,0.5), 3)
eps_star = mu_4/pow(pow(x_dis,0.5), 4)-3
print(a_star, eps_star)
print("___________")
mode = min(data) + h*2 + h*(p_arr[2] - p_arr[1])/((p_arr[2]-p_arr[1])+(p_arr[2]-p_arr[3]))
print("Мода: ", mode)
med_0 = min(data) + (((max(data)-min(data))/2) // h)*h
print(((max(data)-min(data))/2) )
sum_med = 0
for i in range(int(((max(data)-min(data))/2)//h)):
    sum_med += p_arr[i]*107
print(sum_med)
med = med_0 + (0.5*107-sum_med)*h/(sum_med + p_arr[int(((max(data)-min(data))/2) // h)]*107)
print("Медиана: ", med)
print("Коэффициент вариации: ", abs(pow(x_dis,0.5))/x_mid*100)
print("______________________")
print("Точность доверительного интервала при 0,95:", pow(x_s, 0.5) * 1.9825972617102907/pow(107, 0.5))
print("Точность доверительного интервала при 0,99:", pow(x_s, 0.5) * 2.6230084108138523/pow(107, 0.5))
print("Интервал 0.95: ", x_mid - pow(x_s, 0.5) * 1.9825972617102907/pow(107, 0.5), x_mid + pow(x_s, 0.5) * 1.9825972617102907/pow(107, 0.5))
print("Интервал 0,99: ", x_mid - pow(x_s, 0.5) * 2.6230084108138523/pow(107, 0.5), x_mid + pow(x_s, 0.5) * 2.6230084108138523/pow(107, 0.5))
print("______________")
print("Доверительный интервал 0.95: ", pow(x_s, 0.5) - pow(x_s, 0.5)*0.142, pow(x_s, 0.5) + pow(x_s, 0.5)*0.142)
print("Доверительный интервал 0,99: ", pow(x_s, 0.5) - pow(x_s, 0.5)*0.197, pow(x_s, 0.5)+pow(x_s, 0.5)*0.197)
print("____________")
phi = []
for i in range(len(p_arr)):
    phi.append((mid_arr[i]-x_mid)/pow(x_s, 0.5))
print(phi)
phi_new = [[-0.95/2+0.5],
           [-0.78130/2+0.95/2],
           [-0.38292/2+0.78130/2],
           [0.18191/2+0.38292/2],
           [0.66294/2-0.18191/2],
           [0.90897/2-0.66294/2],
           [0.98448/2-0.90897/2]]
print(phi_new)
n_new = []
for i in range(len(p_arr)):
    n_new.append(107*phi_new[i][0])
n_new_sum = 0
for i in range(len(n_new)):
    print(count_arr[i])
    n_new_sum += (pow(count_arr[i]-n_new[i], 2))/n_new[i]
print("Значение критерия: ", n_new_sum)

