
class Biblioteca():
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionarLivro(self, livro):
        if livro not in self.livros:
            self.livros.append(livro)
            print(f"Livro '{livro.obterTitulo()}' adicionado à biblioteca.")
        else:
            print(f"Livro '{livro.obterTitulo()}' já adicionado.")

    def removerLivro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obterTitulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não está na biblioteca.")

    def buscarLivro(self, titulo):
        for livro in self.livros:
            if livro.obterTitulo() == titulo:
                    return livro
        return None

    def adicionarUsuario(self, usuario):
        try:
            self.usuarios.append(usuario)
            print(f"Usuário '{usuario.obterNome()}' adicionado à biblioteca.")
        except:
            print("Nome de usuário inválido.")

    def removerUsuario(self, usuario):
        if usuario in self.usuarios:
            self.usuarios.remove(usuario)
            print(f"Usuário '{usuario.obterNome()}' removido da biblioteca.")
        else:
            print(f"Usuário '{usuario.obterNome()}' não está registrado na biblioteca.")

    def buscarUsuario(self, nome):
        for usuario in self.usuarios:
            if usuario.obterNome() == nome:
                    return usuario
        return None
   
    def emprestarLivro(self, livro):
        if livro in self.livros and livro.estaDisponivel():
            self.buscarLivro(livro).atualizarStatus(False)
            return 1
        return 0

    def receberLivro(self, livro):
        if livro.estaDisponivel() == False:
           self.buscarLivro(livro).atualizarStatus(True)
           return 1
        return 0

