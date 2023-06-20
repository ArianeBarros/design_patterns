from Biblioteca import Biblioteca
from Usuario import Usuario
from Livro import Livro


class Program:
    @staticmethod
    def main():
        # Exemplo de uso do código:

        # Criação de alguns livros
        livro1 = Livro("Python para Iniciantes", "John Smith", 2018)
        livro2 = Livro("Python Avançado", "Jane Doe", 2020)

        # Criação de usuários
        usuario1 = Usuario("Alice", "alice@example.com")
        usuario2 = Usuario("Bob", "bob@example.com")

        # Criação da biblioteca
        biblioteca = Biblioteca()

        # Adicionar livros à biblioteca
        biblioteca.adicionarLivro(livro1)
        biblioteca.adicionarLivro(livro2)

        # Adicionar usuários à biblioteca
        biblioteca.adicionarUsuario(usuario1)
        biblioteca.adicionarUsuario(usuario2)

        # Empréstimo de livro
        usuario1.emprestarLivro(livro1)

        # Tentativa de empréstimo de livro indisponível
        usuario2.emprestarLivro(livro1)

        # Devolução de livro
        usuario1.devolverLivro(livro1)

        # Remoção de livro
        biblioteca.removerLivro(livro2)

        # Remoção de usuário
        biblioteca.removerUsuario(usuario2)

        # Busca de livro e usuário
        livro_encontrado = biblioteca.buscarLivro("Python para Iniciantes")
        usuario_encontrado = biblioteca.buscarUsuario("Alice")

        # Exemplo de uso dos métodos de acesso
        if livro_encontrado:
            print(livro_encontrado.obterTitulo())
        if usuario_encontrado:
            print(usuario_encontrado.obterNome())


# Executar o método main
if __name__ == '__main__':
    Program.main()