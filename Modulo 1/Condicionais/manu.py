peso = int(input("digite o seu peso"))
altura= int(input("digite sua altura"))

imc = peso/ (altura**2)

print(" seu imc é")
if imc < 18.5:
    print ("classificação: abaixo do peso ")
elif imc < 25:
    print(" classificação: peso normal ")
elif imc < 30:
    print ("classificação: sobrepeso")

else:
    print ("classificação obesidade")