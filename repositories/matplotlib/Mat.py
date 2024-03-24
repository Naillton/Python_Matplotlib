import numpy as np
import matplotlib.pyplot as plt
import random as rand

km = rand.randrange(1, 50) # gerando numeros aleatorios em um range
fig, ax = plt.subplots() # retrando do objeto subplots o figure e os eixos

people = ("Tom", "Dick", "Harry", "Slim", "Jim") # lista de pessoas
y_position = np.arange(len(people)) # utilizando o tamanho da lista e setando na posicoa y do grafico
x_position = km * np.random.rand(len(people)) # setando os valores na posição X gerados na variavel km
error = np.random.rand(len(people))

ax.barh(y_posisition, x_position, xerr=error, align='center') # setando informações em um grafico de barras horizontal
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()
ax.set_ylabel('Y Position PEOPLE NAME')
ax.set_xlabel('X Position KM TRAVELED')
ax.set_title('Performance dos candidatos no dia de hoje!')
plt.show()
