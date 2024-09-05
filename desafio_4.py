def calcular_percentuais(faturamento_estados):
    faturamento_total = sum(faturamento_estados.values())
    percentuais = dict()
    for estado, valor in faturamento_estados.items():
        percentuais[estado] = (valor / faturamento_total) * 100
    return percentuais


faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
resultados = calcular_percentuais(faturamento)
for estado, percentual in resultados.items():
    print(f"O estado {estado} representou {percentual:.2f}% do faturamento total.")
