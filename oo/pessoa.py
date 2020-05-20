class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    lucas = Pessoa(nome='Lucas')
    diogo = Pessoa(lucas, nome='Diogo')
    print(Pessoa.cumprimentar(diogo))
    print(id(diogo))
    print(diogo.cumprimentar())
    print(diogo.nome)
    print(diogo.idade)
    for filho in diogo.filhos:
        print(filho.nome)
    diogo.sobrenome= 'Rebello'
    del diogo.filhos
    print(diogo.__dict__)
    print(lucas.__dict__)

