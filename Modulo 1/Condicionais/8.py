valor=int(input("digite o valor da compra"))

if valor> 100:
   valorfinal = valor - (valor * 0.10)
   print("ganhou 10% de desconto. r$: valorfinal",valorfinal)

elif valor== 100:
   print(" valor igual a 100 e sem desconto",valor)

else:(" valor menor que 100 e sem desconto")
