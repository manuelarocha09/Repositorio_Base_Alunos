from valores import Session
from manuela import Vendedor

with Session() as session:
    loja_vendedor = Vendedor(nome="Roberta")
    session.add(loja_vendedor)
    session.commit()
    print("Vendedor inserido com sucesso!")