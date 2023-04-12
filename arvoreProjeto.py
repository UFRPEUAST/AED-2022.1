class No:
    def __init__(self, value):
        # receber o valor
        # ter um apontador para esquerda
        # ter um apontador para direita
        pass

    def __str__(self):
        # retornar o valor do no
        pass

    def is_leaf(self):
        # retorna True ou False para saber se o nó é uma folha
        pass


class Tree:
    def __init__(self):
        # receber a raiz como None
        # ter uma variavel que armazena o total de nós de uma arvore.
        pass

    def add(self, value):
        # 1 - adicionar um no na arvore AVL
        # 2 - incrementar a variavel de total de nos da arvore
        # 3 - Chamar a função balancear a arvore - Deixa essa por ultimo
        # Função - self.rotacao(self.raiz)
        pass

    def length(self):
        # retornar o total de nos da arvore
        pass

    def pre_ordem(self):
        # imprimir os nos de uma arvore em pre_ordem
        pass

    def in_ordem(self):
        # imprimir os nos de uma arvore em in_ordem
        pass

    def pos_ordem(self):
        # imprimir os nos de uma arvore em pos_ordem
        pass
        # self._print(self.raiz, 'pos')

    def _print(self, perc, type):
        # função interna para imrprimir a arvore de umas das opções
        # onde type pode ser pre|in|pos
        pass

    def __str__(self):
        pass

    def _get_perc(self, perc, value, ant=None):
        # Usar para buscar um no a partir de um valor
        pass

    def get(self, value):
        # buscar um elemento na arvore, se existir, retonrar o no dele
        ## Umas opção é criar um função _get_perc - recursiva
        pass

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

    def altura(self, valor):
        # buscar um no pelo valor, se exitir, verificar a altura desse no
        # usado na função de balancar
        pass

    def fator(self, valor):
        # buscar um no pelo valor, se exitir, verificar o fator de balanceamento
        # usado na função de balancar
        pass

    def remove(self, value):
        # remover um no da arvore
        # Pode usar as funções internas dadas em aula./
        # _get_min | _get_max | _get_sucessor | _get_predecessor
        # Chamar a função balancear a arvore
        pass

    def rotacao(self, atual):
        print('VAMOS ROTACIONAR', atual)
        # 1 - pega o nó
        # 2 - verifica o fator de balanceamento (Pega o fator da esquerda e o da direita e subtrai e verifica)
        # 3 rotaciona para esqueda ou direita, antes de rotacionar verificar se é rotação simples ou duplas

    def rotacionar_direita(self):
        # adicionar os parametros desejados
        pass

    def rotacionar_esquerda(self):
        # adicionar os parametros desejados
        pass

    def lista_to_arvore(self, lista):
        # 1 - Vai receber a lista dupla cria na 1 VA
        # 2 - Fazer um for nela e chama a função add
        pass

    def arvore_to_lista(self, type):
        # 1 - Vai receber um type, pre|in|pos/
        # 2 - Vai retornar a lista dupla, criado na 1v com a lista de acorod com o type.
        # 3 - Tentar usar algo parecido com pre_ordem| pos_ordem| in_ordem
        pass
