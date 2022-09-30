from node import Node


class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None

    #adicionar no final da lista
    def adicionar(self, valor, inicio=False):
        if (inicio):
            self.adicionar_no_inicio(valor)
        else:
            self.adicionar_no_fim(valor)

    def adicionar_no_inicio(self, valor):
        if (self.inicio == None):
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            node = Node(valor, None)
            node.proximo = aux
            self.inicio = node

    def adicionar_no_fim(self, valor):
        if (self.inicio == None):
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio
            while (aux.proximo != None):
                aux = aux.proximo

            aux.proximo = Node(valor, None)

    def remover(self, valor):
        anterior = None
        aux = self.inicio
        if aux.valor == valor:
            self.inicio = aux.proximo
        else:
            while aux.valor != valor:
                anterior = aux
                aux = aux.proximo
            if aux.proximo == None:
                anterior.proximo = None
            else:
                anterior.proximo = aux.proximo

    def show(self):
        aux = self.inicio
        print("[", end=' ')
        while (aux.proximo != None):
            print(f"{aux.valor}", end=', ')
            aux = aux.proximo
        print(f"{aux.valor}]")
