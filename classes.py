class Pessoa:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade
        
p1 = Pessoa("alice",25)
print(p1.nome)
print(p1.idade)