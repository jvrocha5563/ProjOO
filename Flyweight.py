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