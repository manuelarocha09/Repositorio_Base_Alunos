paciente=(input("digite o seu nome"))
peso=float(input("digite o seu peso"))
altura=float(input("digite sua altura"))

imc= peso/(altura*altura)

if imc < 18.5:
    print("abaixo do peso")

elif imc < 25.0:
    print("peso normal")

elif imc < 30.0:
    print("sobrepeso")

elif imc < 35.0:
    print("obesidade grau 1")

elif imc < 40.0:
    print("obesidade grau 2")

else:
    print("obesidade grau 3")
