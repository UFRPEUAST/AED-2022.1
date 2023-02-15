class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.nivel = 0

    def __str__(self):
        return f'{self.value}'

    def is_folha(self):
        return self.right is None and self.left is None


class Tree:
    def __init__(self):
        self.raiz = None
        self.__total_nodes = 0

    def add(self, value):
        no = No(value)
        self.__total_nodes += 1
        if not self.raiz:
            self.raiz = no
            return
        perc = self.raiz
        while True:
            no.nivel += 1
            if value > perc.value:
                if not perc.right:
                    perc.right = no
                    break
                perc = perc.right
            else:
                if not perc.left:
                    perc.left = no
                    break
                perc = perc.left

    def length(self):
        return self.__total_nodes

    def pre_ordem(self):
        self._print(self.raiz, 'pre')

    def in_ordem(self):
        self._print(self.raiz, 'in')

    def pos_ordem(self):
        self._print(self.raiz, 'pos')

    def _print(self, perc, type):
        if not perc:
            return
        if type == 'pre':
            print(perc.value)
        self._print(perc.left, type)
        if type == 'in':
            print(perc.value)
        self._print(perc.right, type)
        if type == 'pos':
            print(perc.value)

    def __str__(self):
        print(self.raiz.value)
        print(self.raiz.left.value)
        print(self.raiz.right.value)
        return

    def _get_perc(self, perc, value, ant=None):
        if not perc or perc.value == value:
            return perc, ant
        elif value > perc.value:
            return self._get_perc(perc.right, value, perc)
        else:
            return self._get_perc(perc.left, value, perc)

    def get(self, value):
        # perc = self._get_perc(self.raiz, value)
        # return perc
        perc = self.raiz
        if not perc:
            return None
        while perc is not None and perc.value != value:
            if value > perc.value:
                perc = perc.right
            else:
                perc = perc.left
        return perc

    def _get_sucessor(self, perc):
        sucessor = perc.right
        ant = None
        if not sucessor:
            return None
        while sucessor.left:
            ant = sucessor
            sucessor = sucessor.left
        return sucessor, ant

    def remove(self, value):
        perc, ant = self._get_perc(self.raiz, value)
        if perc:
            if perc.is_folha():
                if perc.value > ant.value:
                    ant.right = None
                else:
                    ant.left = None
                return True
            else:
                sucessor, ant_sucessor = self._get_sucessor(perc)
                if sucessor:
                    sucessor.nivel = perc.nivel
                    ant.right = sucessor
                    sucessor.left = perc.left
                    ant_sucessor.left = sucessor.right
                    sucessor.right = perc.right
                    return True
                # predecessor =
                # if predecessor:
                #     ....
        return False

        # o menor elemento da arvore da direita
        # do nó que vamos remover
        delete_no = self.get(value)
        if not delete_no:
            return False
        sucessor, anterior = self._get_sucessor(delete_no)
        if sucessor:
            sucessor.left = delete_no.left
            anterior.left = sucessor.right
            sucessor.right = delete_no.right
            delete_no.right = None
            delete_no.left = None

            print('VAMOS REMOVERS')
            return True
        # Maior elemento da arvore da esquerda
        # dor nó que vai remover
        # predecessor = self._get_predecessor(value)
        # if predecessor:
        #     print('VAMOS REMOVERS')
        #     return True
        return False


# 50,60,72,65,30,25
arvore = Tree()
arvore.add(50)
arvore.add(30)
arvore.add(25)
arvore.add(69)

arvore.add(60)
arvore.add(72)
arvore.add(65)
arvore.add(71)
# print('PRE----')
# arvore.pre_ordem()
# print('IN----')
# arvore.in_ordem()
# print('POS----')
# arvore.pos_ordem()

print('BUSCA')
no = arvore.get(60)
print(no)

print(arvore.remove(25))
print(arvore.remove(69))
