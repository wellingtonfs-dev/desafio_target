import json


def analisar_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as f:
        dados = json.load(f)
    faturamentos = [dado['valor'] for dado in dados if dado['valor'] > 0]
    media = sum(faturamentos) / len(faturamentos)
    acima_media = sum(1 for valor in faturamentos if valor > media)
    return min(faturamentos), max(faturamentos), acima_media


arquivo = 'dados.json'
menor, maior, dias_acima_media = analisar_faturamento(arquivo)

if menor is not None:
    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

