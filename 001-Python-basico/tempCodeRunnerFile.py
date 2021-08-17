def calc_imc(peso, altura):
    result = peso / (altura ** 2)
    print("Seu imc é", round(result, 1))


calc_imc(75, 1.69)