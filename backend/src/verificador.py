def validar_valores(v):
    try:
        return float(v)
    except ValueError:
        raise ValueError(f"Valor inválido: '{v}'. Digite apenas números reais.")
