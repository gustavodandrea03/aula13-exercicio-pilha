class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.proximo = None

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Páginas: {self.paginas}"

class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, livro: Livro):
        livro.proximo = self.topo
        self.topo = livro
        self.tamanho += 1
        print(f"Livro '{livro.titulo}' adicionado à pilha.")

    def remover(self):
        if self.tamanho == 0:
            print("A pilha está vazia, não há livros para remover.")
            return None
        livro_removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        print(f"Livro '{livro_removido.titulo}' removido da pilha.")
        return livro_removido

    def imprimir(self):
        if self.tamanho == 0:
            print("A pilha está vazia.")
            return
        atual = self.topo
        print("Pilha de livros:")
        while atual is not None:
            print(atual)
            atual = atual.proximo

    def tamanho_pilha(self):
        return self.tamanho

    def topo_pilha(self):
        if self.topo is not None:
            return self.topo
        print("A pilha está vazia.")
        return None

def menu():
    pilha_de_livros = Pilha()
    while True:
        print("\nMenu:")
        print("1. Adicionar Livro")
        print("2. Remover Livro")
        print("3. Visualizar Pilha")
        print("4. Ver Tamanho da Pilha")
        print("5. Ver Livro no Topo")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            while True:
                try:
                    paginas = int(input("Digite o número de páginas: "))
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número inteiro para o número de páginas.")
            livro = Livro(titulo, autor, paginas)
            pilha_de_livros.add(livro)
        elif opcao == "2":
            pilha_de_livros.remover()
        elif opcao == "3":
            pilha_de_livros.imprimir()
        elif opcao == "4":
            print(f"Tamanho da pilha: {pilha_de_livros.tamanho_pilha()}")
        elif opcao == "5":
            topo = pilha_de_livros.topo_pilha()
            if topo is not None:
                print(f"Livro no topo: {topo}")
        elif opcao == "6":
            print("Saindo...")
            break
        else:
            print("Opção inválida, por favor tente novamente.")

menu()
