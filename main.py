faturamento_exemplo = [
    150, 180, 0, 200, 170, 0, 0, 
    200, 325, 0, 179, 0, 400, 205,
]


def calcular_faturamento():
    faturamento_valido = [f for f in faturamento_exemplo if f > 0]

    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)

    media_anual = sum(faturamento_valido) / len(faturamento_valido)


    dias_acima_da_media = sum(1 for f in faturamento_valido if f > media_anual)


    print(f"Menor faturamento: {menor_faturamento}")
    print(f"Maior faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

calcular_faturamento()
