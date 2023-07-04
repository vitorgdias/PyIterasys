def print_hi(name):
    print(f'Hi, {name}')

def somar(n1, n2):
    return n1 + n2

def multiplicar(n1, n2):
    return n1 * n2
def subtracao(n1, n2):
    return n1 - n2

def dividir(n1, n2):
    if n2 != 0:
        resultado = n1/n2
    else:
        resultado = "Não dividirás por zero"
    return resultado

if __name__ == '__main__':
    print_hi('Vitor')

    resultado = somar(1,2)
    print(f'O resultado da soma é: {resultado}')
    resultado = subtracao(5,3)
    print(f'O resultado da subtração é: {resultado}')
    resultado = multiplicar(2, 4)
    print(f'O resultado da multiplicação é: {resultado}')
    resultado = dividir(9, 0)
    print(f'O resultado da divisão é: {resultado}')


