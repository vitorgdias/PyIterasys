import csv

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
#Ler dados de um CSV pra usar no teste seguinte

def ler_dados_csv():
    dados_csv = []
    nome_arquivo = 'C:/Users/Vitor/Desktop/Vitor/Cursos/Python2023/PyIterasys/test/db/massa_caixa.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile: #repete a leitura do arquivo CSV até o final do arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
            return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id, largura, comprimento, altura, resultado_esperado', ler_dados_csv())

def testar_calcular_volume_do_paralelograma(id,largura, comprimento, altura, resultado_esperado):
    '''
    Dados abaixo agora estão vindo do arquivo CSV
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100
    '''
    resultado_atual = calcular_volume_do_paralelograma(int(largura), int(comprimento), int(altura))
    assert resultado_atual == int(resultado_esperado)

