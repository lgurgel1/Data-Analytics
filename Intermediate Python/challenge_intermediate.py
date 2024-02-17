class Tabuada:
    def __init__(self, num):
        self.num = num

    def exibir_tabuada(self):
        try:
            if self.num < 1 or self.num > 10:
                print("Valor inválido. Digite um número entre 1 e 10.")
            else:
                for i in range(1, 11):
                    print(f'{self.num} X {i} = {self.num * i}')
        except ValueError:
            print("Erro. Entrada inválida. Insira um número inteiro")

    def __str__(self):
        if 1 <= self.num <= 10:
            return f'Tabuada do {self.num}'
        else:
            return f' '

while True:
    try:
        num = int(input("Digite um número entre 1 e 10 (ou 0 para sair): "))
        if num == 0:
            break
        t = Tabuada(num)
        t.exibir_tabuada()
        print(t)
    except ValueError:
        print("Erro: entrada inválida. Por favor insira um número inteiro.")
