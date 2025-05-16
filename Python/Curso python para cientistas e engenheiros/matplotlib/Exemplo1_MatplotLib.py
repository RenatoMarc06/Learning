import numpy as np
import matplotlib.pyplot as plt

const = 2

# Não seria necessário criar as variáveis y, fiz apenas por didática
x_array = np.linspace(0,2*np.pi,10)
print(x_array)
y_array = x_array**2
y_1array = x_array*const
y_3array = x_array**3

# Muito semelhante ao Matlab
plt.figure()
plt.subplot(3,1,1)
plt.plot(x_array,y_array)
plt.title("parábola (x^2)")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()

plt.subplot(3,1,2)
plt.plot(x_array,y_1array)
plt.title("Afim (ax + b)")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.subplots_adjust(hspace=1) 

plt.subplot(3,1,3)
plt.plot(x_array,y_3array)
plt.title("Polinomial de grau 3 (x^3)")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()
plt.subplots_adjust(hspace=1) 

# Pode-se também plotar tudo no mesmo
plt.figure()
plt.plot(x_array,y_array, 'r', label = 'Parábola')
plt.plot(x_array,y_1array, 'b', label = 'Afim')
plt.plot(x_array,y_3array, 'g', label = 'Polinomal de grau 3')
plt.legend()
plt.title("Funções")
plt.xlabel("Eixo x")
plt.ylabel("Eixo y")
plt.grid()

plt.show()
