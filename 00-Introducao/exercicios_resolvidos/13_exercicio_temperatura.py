#Receba uma temperatura em Farenheit e exiba em graus celsius (c = 5 * f - 32 / 9)

farenheit = float(input("Informe a temperatura em Farenheit: "))

celsius = 5 * (farenheit - 32) / 9

print(f"A temperatura {farenheit} F em Celsius é: {celsius} C")
