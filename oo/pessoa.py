class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome = None, idade = 37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3

if __name__ == '__main__':
    lucas = Mutante(nome='Lucas')
    diogo = Homem(lucas, nome='Diogo')
    print(Pessoa.cumprimentar(diogo))
    print(id(diogo))
    print(diogo.cumprimentar())
    print(lucas.cumprimentar())
    print(diogo.nome)
    print(diogo.idade)
    for filho in diogo.filhos:
        print(filho.nome)
    diogo.sobrenome= 'Rebello'
    del diogo.filhos
    diogo.olhos = 1
    del diogo.olhos
    print(diogo.__dict__)
    print(lucas.__dict__)
    print(Pessoa.olhos)
    print(lucas.olhos)
    print(diogo.olhos)
    print(id(Pessoa.olhos), id(lucas.olhos), id(diogo.olhos))
    print(Pessoa.metodo_estatico(), diogo.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), diogo.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(lucas, Pessoa))
    print(isinstance(lucas, Homem))
    print(lucas.olhos)
