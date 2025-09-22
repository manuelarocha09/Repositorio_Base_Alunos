import requests
# Resumao criar um sistema que traz os pedidos , deleta e publica pedidos

opção= input("Digite 1 para fazer um pedido ou 2 para ver o cardápio: 3 para alterar um pedido 4 para deletar um pedido ")


if opção == "1":
    Prato=input("Digite seu prato: ")
    bebida=input("Digite sua bebida: ")
    mesa=input("Digite sua mesa: ")

    dados={
        "Prato": Prato,
        "Bebida": bebida,
        "Mesa": mesa
    }
    resposta = requests.post("https://68ca9fc5430c4476c34a3dbe.mockapi.io/Restaurante/", json=dados)

elif opção == "2":

    resposta = requests.get('https://68ca9fc5430c4476c34a3dbe.mockapi.io/Restaurante')

    print(resposta.json())
elif opção == "3":
    pedido= input('digite o id do seu pedido para poder alterar')
    Prato=input("Digite seu prato: ")
    bebida=input("Digite sua bebida: ")
    mesa=input("Digite sua mesa: ")
    dados={
        "Prato": Prato,
        "Bebida": bebida,
        "Mesa": mesa
    }
    requests.put(f"https://68ca9fc5430c4476c34a3dbe.mockapi.io/Restaurante/{pedido}", json=dados)
elif opção == "4":
    
   possibilidade=input('digite qual o seu id para verificarmos ')

   resposta = requests.get(f'https://68ca9fc5430c4476c34a3dbe.mockapi.io/Restaurante/{possibilidade}')

   print(resposta.json())

   pedido= input('digite o id do seu pedido para poder deletar')
   requests.delete(f'https://68ca9fc5430c4476c34a3dbe.mockapi.io/Restaurante/{pedido}')