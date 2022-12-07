from datetime import datetime

from lista import NodeList

lista_simples = NodeList()
lista_simples.append(25)
lista_simples.append(10)
lista_simples.append(30)
lista_simples.append(33)
lista_simples.append(5)
lista_simples.append(50)
lista_simples.append(70)
lista_simples.insert(3, 75)
print(lista_simples)
# lista_simples.update_value(2, 65)
lista_simples[2] = 65
print(lista_simples)
lista_simples.remove(0)

# index = lista_simples.get_index(30)


lista1 = [10, 20, 30, 40, 50]
lista2 = [100, 200]
lista1.extend(lista2)
print(lista1)
