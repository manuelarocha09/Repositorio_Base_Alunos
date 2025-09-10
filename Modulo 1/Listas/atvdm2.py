palavra= input("manu")
contador = 2
vogais = "a,e,i,o,u"

for letra in palavra:
    if letra in vogais:
        print('é uma vogal')
    else:
        print('casda')