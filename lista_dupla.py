class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.value)


class DoubledList:

    def __init__(self, max_length=None, force_type=None):
        self.__begin = None
        self.__end = None
        self.__length = 0
        self.__max_length = max_length
        self.force_type = force_type
        self.teste = 'teste'

    def validate(self, value=None, index=None):
        if self.__max_length and self.__length >= self.__max_length:
            raise Exception('O número máximo de elementos já foi atribuidos')
        if self.force_type and type(value) is not self.force_type:
            raise TypeError('O tipo não é válido')
        if index and index > self.__length - 1:
            raise IndexError('Index não existe na lista')

    def append(self, value):
        self.validate(value=value)
        no = Node(value)
        if self.__length == 0:
            self.__begin = no
            self.__end = no
        else:
            self.__end.next = no
            no.previous = self.__end
            self.__end = self.__end.next
        self.__length += 1

    def insert(self, index, value):
        no = Node(value)
        if index >= self.__length:
            self.append(value)
        elif index == 0:
            no.next = self.__begin
            self.__begin.previous = no
            self.__begin = no
            self.__length += 1
        else:
            novo_perc = self.__get_perc(index)
            perc_previous = novo_perc.previous
            no.next = novo_perc
            no.previous = perc_previous
            novo_perc.previous = no
            perc_previous.next = no
            self.__length += 1

    def update_value(self, index, value):
        self.validate(index=index)
        perc = self.__get_perc(index)
        perc.value = value

    def get_index(self, value):
        pass
        # retornar o index (posição) do primeiro elemento
        # que encontrar na lista
        # caso não encontre, retornar um raise ValueError()

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

    # def test(self,index):
    #     return self.__get_perc(index)

    def __get_perc(self, index):
        self.validate(index=index)
        point_index = self.__length - 1
        if index == 0:
            return self.__begin
        elif index == point_index:
            return self.__end
        else:
            point = 0
            next = True
            if index < (self.__length / 2):
                perc = self.__begin
                point = index
            else:
                perc = self.__end
                point = point_index - index
                next = False

            for i in range(point):
                if next:
                    perc = perc.next
                else:
                    perc = perc.previous

            return perc

    def get_item(self, index):
        perc = self.__get_perc(index)
        return perc.value

    def get_length(self) -> int:
        return self.__length

    def __print(self, reverse=False):
        if self.__begin is None:
            return '[]'
        value = ''
        perc = self.__begin if not reverse else self.__end
        apont = 'next' if not reverse else 'previous'
        while getattr(perc, apont):
            value += f'{perc.value}, '
            perc = getattr(perc, apont)
        else:
            value += f'{perc.value}'
        return f'[{value}]'

    def __str__(self):
        return self.__print()

    def print_reverse(self):
        return self.__print(True)

    def __len__(self):
        return self.get_length()

    def __getitem__(self, index):
        return self.get_item(index)

    def __setitem__(self, key, value):
        self.update_value(key, value)
