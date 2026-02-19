"Calculadora de IMC (Índice de Massa Corporal)"

weight = float(input("Peso en kg: "))
height = float(input("Altura en metros: "))

imc = weight / (height ** 2)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Bajo peso")
elif 18.5 <= imc < 25:
    print("Peso normal")
elif 25 <= imc < 30:
    print("Sobrepeso")