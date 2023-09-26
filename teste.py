altura = float(input('Coloque a sua altura: '))
peso = float(input('Coloque o seu peso: '))
imc = peso / (altura**2)

print(f"Com seu peso de {peso}Kgs e com a sua altura de {altura}m, o seu IMC é:{round(imc, 1)}")