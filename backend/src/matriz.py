import sympy as sp

class Matriz:
    def __init__(self, valores, ordem):
        self.valores = valores
        self.ordem = ordem
        self.matriz = []

    def montar_matriz(self):
        self.matriz = []
        total_coef = self.ordem * self.ordem
        coefs = self.valores[:total_coef]
        termos_independentes = self.valores[total_coef:]
        for i in range(self.ordem):
            linha = coefs[i*self.ordem:(i+1)*self.ordem] + [termos_independentes[i]]
            self.matriz.append(linha)
        return self.matriz

    def exibir_matriz(self):
        for linha in self.matriz:
            coefs_formatados = "  ".join(f"{int(x):>3}" for x in linha[:-1])
            termo_indep = f"{int(linha[-1]):>3}"
            print(f"[ {coefs_formatados} | {termo_indep} ]")

    def calcular_determinante(self):
        A = sp.Matrix([linha[:-1] for linha in self.matriz])
        det = A.det()
        det_val = float(det)
        if det_val.is_integer():
            return int(det_val)
        return det_val

    
    def calcular_crammer(self):
        A = sp.Matrix([linha[:-1] for linha in self.matriz])
        b = sp.Matrix([linha[-1] for linha in self.matriz])
        solucao = A.LUsolve(b)

        variaveis_possiveis = ['x', 'y', 'z', 'w', 'v']
        resultado = {}

        for i, valor in enumerate(solucao):
            variavel = variaveis_possiveis[i]
            valor_simplificado = sp.nsimplify(valor, rational=True)
            num, den = valor_simplificado.as_numer_denom()

            if den == 1:
                resultado[variavel] = int(num)
            else:
                resultado[variavel] = f"{num}/{den}"

        return resultado

