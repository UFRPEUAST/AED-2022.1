from datetime import datetime

from lista import NodeList

# lista_simples = NodeList()
# lista_simples.append(25)
# lista_simples.append(10)
# lista_simples.append(30)
# lista_simples.append(33)
# lista_simples.append(5)
# lista_simples.append(50)
# lista_simples.append(70)
# lista_simples.insert(3, 75)
# print(lista_simples)
# lista_simples.update_value(2, 65)
# lista_simples[2] = 65
# print(lista_simples)
# lista_simples.remove(0)


# for i in lista_simples:
#     print(i)

# index = lista_simples.get_index(30)


# lista1 = [10, 20, 30, 40, 50]
# lista2 = [100, 200]
# lista1.extend(lista2)
# print(lista1)


# print(len(lista_simples))
# print(lista_simples[0])
from lista_dupla import DoubledList

lista = DoubledList()
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)
lista.insert(0, 2)
lista.insert(10, 50)
lista.insert(4, 25)
lista.insert(1, 5)
print(lista[-1])
list1 = [1, 2, 3]
list1.reverse()
print(list1)
lista.update_value(4, 100)
print(lista)
print(lista.print_reverse())
