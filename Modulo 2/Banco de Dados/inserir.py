from valores import Session
from manuela import Loja

with Session() as session:
    nova_loja = Loja(nome="Manucar", endereco="Rua Estrela", gerente="Gustavo")
    session.add(nova_loja)
    session.commit()
    print("Loja inserida com sucesso!")