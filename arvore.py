class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.nivel = 0

    def __str__(self):
        return f'{self.value}'

    def is_leaf(self):
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

    def _get_min(self, no):
        perc = no
        while perc.left:
            perc = perc.left
        return perc

    def _get_max(self, no):
        pred = no
        while pred.right:
            pred = pred.right
        return pred

    def _get_sucessor(self, no):
        sucessor = self._get_min(no.right)
        return sucessor

    def _get_predecessor(self, no):
        perc = self._get_max(no.left)
        return perc

    def remove(self, value):
        perc, ant = self._get_perc(self.raiz, value)
        if perc:
            # 1 - saber se o No é uma folha
            if perc.is_leaf():
                if ant.value > perc.value:
                    ant.left = None
                else:
                    ant.right = None
                return True
            sucessor = self._get_sucessor(perc)
            ant_sucessor = self._get_perc(perc, sucessor.value)[1]
            # predecessor = self._get_predecessor(perc)
            # if predecessor.is_leaf():
            #     print('----')
            # else:
            perc.value = sucessor.value
            if ant_sucessor.value>sucessor.value:
                ant_sucessor.left = sucessor.right
                sucessor.right = None
            else:
                ant_sucessor.right = sucessor.left
                sucessor.left = None
            return True
            # print('***', perc)
            # print('***', ant)
            # print('***', sucessor)
            # print('***', ant_sucessor)
            # print('***', predecessor)

        return False


# 50,60,72,65,30,25
arvore = Tree()
arvore.add(50)
arvore.add(30)
arvore.add(25)
arvore.add(69)
arvore.add(60)
arvore.add(75)
arvore.add(72)
arvore.add(65)
arvore.add(78)
arvore.add(35)
arvore.add(73)
# print('PRE----')
# arvore.pre_ordem()
# print('IN----')
# arvore.in_ordem()
# print('POS----')
# arvore.pos_ordem()

# no = arvore.get(60)
print(arvore.in_ordem())
# print(arvore.remove(25))
print(arvore.remove(69))
print(arvore.remove(30))
print(arvore.remove(50))
print(arvore.remove(60))
print('----')
print(arvore.in_ordem())

print('******')
