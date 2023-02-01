	
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
# Определение пределов переменновй величины
teta = np.arange(0, 2*np.pi, 0.01)
 
# Создание дифференциальной функции изменяемой величины
def energy(w, teta):
    dwdteta = 1 / 4 * R_earth**2 * L_sun / (q * v_q)
    return dwdteta
 
# Определение начальных условий и параметров
w_0 = 0
R_earth = 6400000
L_sun = 3.827 * 10**(26)
q = 147 * 10**9
v_q = 30400

# Решение поставленной задачи
solve = odeint(energy, w_0, teta)

# Построение решения в виде графика функции
plt.plot(teta*180/np.pi, solve[:,0])
plt.xlabel('Оборот, градусы')
plt.ylabel('Солнечная энергия, Дж')
plt.title('Освещенность Земли')
plt.grid()

plt.savefig('lab_9_dop_3.png')