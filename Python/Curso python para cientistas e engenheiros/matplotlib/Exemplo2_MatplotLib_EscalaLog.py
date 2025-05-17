import numpy as np
import matplotlib.pyplot as plt

x_array = np.linspace(0,10,500)
y_array = np.exp(x_array)

plt.figure()
plt.suptitle('Comparacao de escalas')
plt.subplot(2,1,1)
plt.title('Escala linear')
plt.plot(x_array,y_array)
plt.xlabel('x')
plt.xlim(0, 10)
plt.ylabel('exp(x)')
plt.grid()

plt.subplot(2,1,2)
plt.title('Escala logaritmica')
plt.yscale('log')
plt.plot(x_array,y_array)
plt.xlabel('x')
plt.ylabel('log(exp(x))') 
# Matematicamente log (nesse caso ln) e exp sao funcoes opostas, entao log(exp(x)) -> x=y
plt.xlim(0, 10)
plt.subplots_adjust(hspace=0.5) 
plt.grid()

plt.show()