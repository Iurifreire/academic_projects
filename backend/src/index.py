from backend.matriz import Matriz
from backend.verificador import validar_valores
    

def main():
    print("=== Cálculo de Determinante e Cramer ===")

    ordem = int(input("Informe a ordem da matriz (2 a 5): "))
    total = ordem * ordem + ordem  

    print(f"Informe {total} valores válidos (coeficientes + termos independentes):")
    valores = []
    
    for i in range(ordem):
        for j in range(ordem):
            x = input(f"Valor a{i+1}{j+1}: ")
            valores.append(validar_valores(x))


    for i in range(ordem):
        x = input(f"Termo independente b{i+1}: ")
        valores.append(validar_valores(x))


    matriz = Matriz(valores, ordem)
    matriz.montar_matriz()

    print("\nMatriz aumentada:")
    matriz.exibir_matriz()

    det = matriz.calcular_determinante()
    print(f"\nDeterminante: {det}")

    if det != 0:
        matriz.calcular_crammer()
    else:
        print("Não é possível calcular Cramer: determinante = 0")

if __name__ == "__main__":
    main()