from datetime import datetime

from lista import NodeList

lista_simples = NodeList()
lista_simples.append(10)
lista_simples.append(30)
lista_simples.append(5)
lista_simples.append(50)
lista_simples.append(70)
print(lista_simples)
print(lista_simples.get_item(0))
print(lista_simples.get_item(1))
print(lista_simples.get_item(2))
print(lista_simples.get_item(3))
print(lista_simples.get_item(4))

# # 8 segundos
# print(datetime.now().time())
# for i in range(0, 20000):
#     lista_simples.append(i)
# print(datetime.now().time())
#
# print('----------')
#
# lista = []
# print(datetime.now().time())
# for i in range(0, 20000):
#     lista.append(i)
# print(datetime.now().time())


lista = [2, 5, 7, 10]
print(lista[6])

# for i in range(5):
#     print(i)