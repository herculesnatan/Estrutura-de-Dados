class BinaryTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.FilhoEsquerda = None
        self.FilhoDireita = None
    
    def InserirEsquerda (self, novoNodo):
        if self.FilhoEsquerda == None:
            self.FilhoEsquerda = BinaryTree(novoNodo)

        else:
            t = BinaryTree(novoNodo)
            t.FilhoEsquerda = self.FilhoEsquerda
            self.FilhoEsquerda = t
    
    def InserirDireita (self, novoNodo):
        if self.FilhoDireita == None:
            self.FilhoDireita = BinaryTree(novoNodo)
        
        else:
            t = BinaryTree(novoNodo)
            t.FilhoDireita  = self.FilhoDireita
            self.FilhoDireita = t
    
    def BuscaFilhoEsquerda (self):
        return self.FilhoEsquerda
    
    def BuscaFilhoDireita(self):
        return self.FilhoDireita
    
    def DefinirValorRaiz (self, obj):
        self.key = obj
    
    def BuscaValorRaiz (self):
        return self.key
    
    def Preorder (tree):
        if tree:
            print(tree.BuscaValorRaiz()) # Processa nodo
            Preorder(tree.BuscaFilhoEsquerda)
            Preorder(tree.BuscaFilhoDireita)
    
    def Inorder (tree):
        if tree:
            Inorder(tree.BuscaFilhoEsquerda)
            print(tree.BuscaValorRaiz()) # Processa nodo
            Inorder(tree.BuscaFilhoDireita)

    def Postorder (tree):
        if tree:
            Postorder(tree.BuscaFilhoEsquerda)
            Postorder(tree.BuscaFilhoDireita)
            print(tree.BuscaValorRaiz) # Processa nodo
