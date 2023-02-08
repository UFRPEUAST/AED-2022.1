class No:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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


arvore = Tree()
arvore.add(50)
arvore.add(32)
arvore.add(60)
arvore.add(72)
arvore.add(65)
arvore.add(25)
print('PRE----')
arvore.pre_ordem()
print('IN----')
arvore.in_ordem()
print('POS----')
arvore.pos_ordem()
