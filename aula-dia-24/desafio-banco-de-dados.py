# Criar um sistema python, resolva um problema de 2 algortimos com matrizes.

def multiplicar_matrizes(a, b):
    if len(a[0]) != len(b):
        print("Erro: número de colunas da matriz A deve ser igual ao número de linhas da matriz B.")
        return None

    # Inicializa a matriz resultado com zeros
    resultado = [[0 for _ in range(len(b[0]))] for _ in range(len(a))]

    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                resultado[i][j] += a[i][k] * b[k][j]

    return resultado


def multiplicar_por_escalar(matriz, escalar):
    return [[elemento * escalar for elemento in linha] for linha in matriz]


def ler_matriz():
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    matriz = []

    for i in range(linhas):
        linha = list(map(float, input(f"Digite os elementos da linha {i+1}, separados por espaço: ").split()))
        while len(linha) != colunas:
            print("Número incorreto de elementos. Tente novamente.")
            linha = list(map(float, input(f"Digite os elementos da linha {i+1}, separados por espaço: ").split()))
        matriz.append(linha)

    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(f"{num:.2f}" for num in linha))


def main():
    print("=== Sistema de Multiplicação de Matrizes ===")
    print("1 - Multiplicar duas matrizes")
    print("2 - Multiplicar uma matriz por um escalar")
    opcao = input("Escolha uma opção (1 ou 2): ")

    if opcao == "1":
        print("\nMatriz A:")
        a = ler_matriz()
        print("\nMatriz B:")
        b = ler_matriz()
        resultado = multiplicar_matrizes(a, b)
        if resultado:
            print("\nResultado da multiplicação A × B:")
            imprimir_matriz(resultado)
    elif opcao == "2":
        print("\nMatriz:")
        matriz = ler_matriz()
        escalar = float(input("Digite o valor do escalar: "))
        resultado = multiplicar_por_escalar(matriz, escalar)
        print("\nResultado da multiplicação por escalar:")
        imprimir_matriz(resultado)
    else:
        print("Opção inválida.")


if __name__ == "__main__":
    main()
