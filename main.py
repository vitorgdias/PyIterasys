import pytest
#Funções
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
        resultado = n1 / n2
    else:
        resultado = "Não dividirás por zero"
    return resultado
#Outra possibilidade de evitar divisões por zero:
#def dividir(n1, n2)
    #try:
        #return n1 / n2
    #except ZeroDivisionError:
        #return 'Não é possível dividir por zero'

#Testes Unitários (Teste de Unidade)
    #Função somar
def elevar(n1, n2):
    return n1 ** n2

def calcular_area_circulo(raio):
    return 3.14 * raio ** 2
def calcular_volume_do_paralelograma(largura, comprimento, altura):
    return largura * comprimento * altura
#Testes Unitários
def test_somar():
    #1 - Configura/Prepara
    n1 = 8 #input
    n2 = 5 #input
    resultado_esperado = 13 #output

    #2 - Executa
    resultado_atual = somar(n1, n2)

    #3 - Valida
    assert resultado_atual == resultado_esperado

def test_somar_resultado_negativo():
    assert somar(-1000, -2000) == -3000

def test_multiplicar():
    assert multiplicar(2, 4) == 8

def test_subtrair():
    assert subtracao(4, 5) == -1

def test_dividir():
    assert dividir(8, 4) == 2

def test_potencia():
    assert elevar(2, 2) == 4
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


