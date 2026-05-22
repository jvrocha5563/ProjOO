class EspecieArvore:
    # __slots__ otimiza a memória
    __slots__ = ['nome_especie', 'textura_dados', 'proj_sombra_padrao']

    def __init__(self, nome_especie: str, textura_dados: str, proj_sombra_padrao: float):
        self.nome_especie = nome_especie
        self.textura_dados = textura_dados  # Simula uma string longa/pesada de bytes
        self.proj_sombra_padrao = proj_sombra_padrao

    def exibir(self, x: int, y: int, altura: float, largura_tronco: float):
        # Simulação de renderização 2D
        pass

class FabricaEspecie:
    _especies = {}

    @classmethod
    def get_especie(cls, nome: str, textura: str, sombra: float) -> EspecieArvore:
        if nome not in cls._especies:
            cls._especies[nome] = EspecieArvore(nome, textura, sombra)
        return cls._especies[nome]

    @classmethod
    def total_especies_criadas(cls) -> int:
        return len(cls._especies)
    
class Arvore:
    # Reduz drasticamente o tamanho de cada instância da árvore na memória do Python
    __slots__ = ['x', 'y', 'altura', 'largura_tronco', 'especie']

    def __init__(self, x: int, y: int, altura: float, largura_tronco: float, especie: EspecieArvore):
        self.x = x                          # Extrínseco
        self.y = y                          # Extrínseco
        self.altura = altura                # Extrínseco
        self.largura_tronco = largura_tronco # Extrínseco
        self.especie = especie              # Referência ao Flyweight (Intrínseco)

    def desenhar(self):
        self.especie.exibir(self.x, self.y, self.altura, self.largura_tronco)