class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class NodeList:

    def __init__(self, max_length=None, force_type=None):
        self.__begin = None
        self.__end = None
        self.__length = 0
        self.__max_length = max_length
        self.force_type = force_type

    def validate(self, value=None, index=None):
        if self.__max_length and self.__length >= self.__max_length:
            raise Exception('O número máximo de elementos já foi atribuidos')
        if self.force_type and type(value) is not self.force_type:
            raise TypeError('O tipo não é válido')
        if index and index > self.__length - 1:
            raise IndexError('Index não existe na lista')

    def append(self, value: str):
        self.validate(value=value)
        no = Node(value)
        if self.__length == 0:
            self.__begin = no
            self.__end = no
        else:
            self.__end.next = no
            self.__end = self.__end.next
        self.__length += 1

    def get_item(self, index):
        self.validate(index=index)
        if index == 0:
            return self.__begin.value
        elif index == self.__length - 1:
            return self.__end.value
        else:
            perc = self.__begin
            for i in range(index):
                perc = perc.next
            return perc.value

    def get_length(self) -> int:
        return self.__length

    def __str__(self):
        if self.__begin is None:
            return '[]'
        value = ''
        perc = self.__begin
        while perc.next:
            value += f'{perc.value}, '
            perc = perc.next
        else:
            value += f'{perc.value}'
        return f'[{value}]'
