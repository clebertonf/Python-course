from datetime import date

year_current_date = date.today().year


def get_info(name, age, height, weight):
    year_birth = year_current_date - age
    imc = round(weight / (height ** 2), 2)
    print(f"{name} tem {age} anos, {height} de altura e pesa {weight} KG.")
    print(f"O IMC do {name} é: {imc}")
    print(f"{name} nasceu em {year_birth}")


get_info("Cleberton", 28, 1.69, 75)

# Função recebe algumas informaçoes por parametro, e retorna ano de nascimento, imc
# com algumas frases customizadas
