from Biblioteca import Biblioteca

class Usuario:

    def __init__(self, nome, email):
        if nome != "":
            self.nome = nome
            self.email = email
            self.biblioteca = Biblioteca()
        else:
            raise
        
    def obterNome(self):
        return self.nome

    def obterEmail(self):
        return self.email

    def emprestarLivro(self, livro):
        if self.biblioteca.emprestarLivro(livro) == True:
            print(f"Livro '{livro.obterTitulo()}' emprestado para {self.nome}.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não está disponível.")

    def devolverLivro(self, livro):
        if self.biblioteca.receberLivro(livro) == 1:
            print(f"Livro '{livro.obterTitulo()}' devolvido por {self.nome}.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não foi emprestado por {self.nome}.")