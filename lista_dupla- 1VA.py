class Node:
    def __init__(self, value):
        pass

    def __str__(self):
        pass


class DoubledList:

    def __init__(self, max_length=None, force_type=None):
        pass

    def append(self, value):
        #Adicionar um elemento no final da lista
        pass

    def insert(self, index, value):
        # Adicionar um elemento em uma index na lista
        #Se for no final, usar o append
        pass

    def update_value(self, index, value):
        # Adicionar um elemento em uma posição na lista
        pass

    def get_index(self, value):
        # retornar o index (posição) do primeiro elemento
        # que encontrar na lista
        # caso não encontre, retornar um raise ValueError()
        pass

    def clear(self):
        pass
        # remove todos os ementos da lista

    def remove(self, index):
        pass
        # 1 - O index deve ser menor que o tamanho da lista
        # 2 - Se o index for igual a 0
        # 2.1 - colocar o apontando no proximo item
        # 3 - se o index for <= ao tamanho-1 da lista
        # 3.1 - Colocar um apontador no anterior da remoção
        # 3.2 - O end aponta para esse apontador
        # 3.3 - O next do novo end aponta para None

    def extend(self, other_list):
        pass
        # 1 - Validar se o other_list é do tipo NodeList
        # 2 - percorrer o other_list e adicionar para elemento ns lista atual

    def get_item(self, index):
        #Busca um elemento em uma posição da lista
        pass

    def get_length(self) -> int:
        pass


    def __str__(self):
        #retornar uma string com todos os elementos da lista
        pass

    def print_reverse(self):
        # retornar uma string com todos os elementos da lista, de fim ao início
        pass

    def __len__(self):
        #chamar o get_length
        pass

    def __getitem__(self, index):
        #chamar o get_item
        pass

    def __setitem__(self, key, value):
        # chamar o update_value
        pass
