def singleton(class_):
    class class_w(class_):
        _instance = None
        def __new__(class_, *args, **kwargs):
            if class_w._instance is None:
                class_w._instance = super(class_w,
                                    class_).__new__(class_,
                                                    *args,
                                                    **kwargs)
                class_w._instance._sealed = False
            return class_w._instance
        def __init__(self, *args, **kwargs):
            if self._sealed:
                return
            super(class_w, self).__init__(*args, **kwargs)
            self._sealed = True
    class_w.__name__ = class_.__name__
    return class_w

@singleton
class BibliotecaSingleton():
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionarLivro(self, livro):
        if livro.estaDisponivel():
            self.livros.append(livro)
            print(f"Livro '{livro.obterTitulo()}' adicionado à biblioteca.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não está disponível.")

    def removerLivro(self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f"Livro '{livro.obterTitulo()}' removido da biblioteca.")
        else:
            print(f"Livro '{livro.obterTitulo()}' não está na biblioteca.")

    def buscarLivro(self, titulo):
        for livro in self.livros:
            if livro.obterTitulo() == titulo:
                if livro.obterTitulo() == titulo:
                    return livro
        return None

    def adicionarUsuario(self, usuario):
        if usuario.obterNome() != "":
            self.usuarios.append(usuario)
            print(f"Usuário '{usuario.obterNome()}' adicionado à biblioteca.")
        else:
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
                if usuario.obterNome() == nome:
                    return usuario
        return None
   
    def emprestarLivro(self, livro):
        if livro.estaDisponivel():
            self.livros.remove(livro)
            livro.atualizarStatus(False)
            self.livros.append(livro)
            return 1
        return 0

    def receberLivro(self, livro):
        if livro.estaDisponivel() == False:
           self.livros.remove(livro)
           livro.atualizarStatus(True)
           self.livros.append(livro)
           return 1
        return 0

