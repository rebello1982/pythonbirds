class Pessoa:
    def __init__(self, *filhos, nome = None, idade = 37):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rebello = Pessoa(nome='Rebello')
    juliana = Pessoa(rebello, nome='Juliana')
    print(Pessoa.cumprimentar(juliana))
    print(id(juliana))
    print(juliana.cumprimentar())
    print(juliana.nome)
    print(juliana.idade)
    for filho in juliana.filhos:
        print(filho.nome)



