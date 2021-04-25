import os
import numpy as np

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def obter_caminho():
    print("Forneca o caminho da entrada:")
    return str(input())

def validar_caminho(caminho):
    arquivoExiste = os.path.isfile(caminho)
    return arquivoExiste

def str_to_complex(string):
    numero = string.split('|')
    result = complex(0,0)

    # Se o tamanho for maior que 1 significa que o número tem uma parte imaginária
    if len(numero) > 1:
        result = complex(float(numero[0]), float(numero[1]))
    else:
        result = complex(float(numero[0]), 0)

    return result

def main():
    clear()

    print("Bem vindo ao resolvedor de matriz elétrica")
    print("==========================================")

    caminho = obter_caminho()
    valido = validar_caminho(caminho)

    while valido == False:
        print("Caminho inválido, por favor forneca um caminho válido ou envie 'q' para sair")
        caminho = obter_caminho()

        if caminho == "q":
            return

        valido = validar_caminho(caminho)

    # Abrindo o arquivo de entrada
    arquivoDeEntrada = open(caminho)

    # Recebendo a ordem da primeira linha
    ordem = int(arquivoDeEntrada.readline())

    coeficientes = []
    resposta = []

    # Lendo a matriz dos coeficientes e o vetor resposta
    for m in range(ordem):
        linha = arquivoDeEntrada.readline().split(' ')
        vetor = []

        for i in range(ordem):
            vetor.append(str_to_complex(linha[i]))

        coeficientes.append(vetor)
        resposta.append(str_to_complex(linha[ordem]))

    arquivoDeEntrada.close()

    # Resolvendo o sistema através do numpy
    sol = np.linalg.solve(coeficientes, resposta)

    print("A solucao do seu sistema é: ")

    for i in range(ordem):
        print(f'v{i+1} = {sol[i]:.4f}')

    print(np.allclose(np.dot(coeficientes, sol), resposta))

print("Sucesso!!!")
main()
