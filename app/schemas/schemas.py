from pydantic import BaseModel

class Lead(BaseModel):
    nome: str
    empresa: str
    cargo: str
    tamanho_empresa: int
    mensagem: str
