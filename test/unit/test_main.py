import pytest
from main import somar, calcular_area_circulo, calcular_volume_do_paralelograma


def testar_somar():
    n1 = 8
    n2 = 9
    resultado_esperado = 17
    resultado_atual = somar(n1, n2)
    assert resultado_atual == resultado_esperado


# Anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio, resultado_esperado',[
                             (1, 3.14),   # Teste 1
                             (2, 12.56),  # Teste 2
                             (3, 28.26),  # Teste 3
                         ])
def testar_area_circulo(raio, resultado_esperado):
    # Parametros abaixo foram comentados para atribuir os valores da matriz acima
    # raio = 2
    # resultado_esperado = 12.56
    resultado_atual = calcular_area_circulo(raio)
    assert resultado_atual == resultado_esperado

def testar_calcular_volume_do_paralelograma():
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    resultado_atual = calcular_volume_do_paralelograma(largura, comprimento, altura)
    assert resultado_atual == resultado_esperado

