class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def obterTitulo(self):
        return self.titulo

    def obterAutor(self):
        return self.autor

    def obterAnoPublicacao(self):
        return self.ano_publicacao

    def estaDisponivel(self):
        return self.disponivel

    def atualizarStatus(self, status):
        self.disponivel = status