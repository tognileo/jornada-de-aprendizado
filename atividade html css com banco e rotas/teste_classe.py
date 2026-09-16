from database import session_local
from classe import Produto
session = session_local()



novo_produto = Produto( nome= "sabonete",marca = "MARCA" , preco = 10.02, data_validade = "10/02/85" )
session.add(novo_produto)
session.commit()
print("inserido com sucesso")


































