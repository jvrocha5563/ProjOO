import sys
import random

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
    __slots__ = ['x', 'y', 'altura', 'largura_tronco', 'especie']

    def __init__(self, x: int, y: int, altura: float, largura_tronco: float, especie: EspecieArvore):
        self.x = x                       
        self.y = y                     
        self.altura = altura               
        self.largura_tronco = largura_tronco
        self.especie = especie              # Referência ao Flyweight (Intrínseco)

    def desenhar(self):
        self.especie.exibir(self.x, self.y, self.altura, self.largura_tronco)

class Mundo2D:
    def __init__(self):
        self.arvores = []

    def plantar_arvore(self, x: int, y: int, altura: float, largura: float, especie: str, textura: str, sombra: float):
        especie_flyweight = FabricaEspecie.get_especie(especie, textura, sombra)
        arvore = Arvore(x, y, altura, largura, especie_flyweight)
        self.arvores.append(arvore)

def exibir_estimativa_memoria(total_arvores: int, total_especies: int):
        # CENÁRIO SEM FLYWEIGHT
        bytes_por_arvore_sem = 360
        memoria_sem = total_arvores * bytes_por_arvore_sem

        # CENÁRIO COM FLYWEIGHT + SLOTS
        bytes_por_arvore_com = 56
        memoria_arvores_com = total_arvores * bytes_por_arvore_com
            
        # As 1.000 espécies em cache (objetos ligeiramente mais pesados, mas são poucos)
        bytes_por_especie = 500
        memoria_especies = total_especies * bytes_por_especie
            
        memoria_total_com = memoria_arvores_com + memoria_especies

        # Conversão para Megabytes
        mb_sem = memoria_sem / (1024 * 1024)
        mb_com = memoria_total_com / (1024 * 1024)

        print("\n--- RESULTADO DA ESTIMATIVA DE MEMÓRIA ---")
        print(f"Espécies únicas em cache: {total_especies}")
        print(f"Memória Estimada SEM Flyweight: {mb_sem:.2f} MB")
        print(f"Memória Estimada COM Flyweight (+ Slots): {mb_com:.2f} MB")
        print(f"Economia Real de Memória: {(1.0 - (mb_com / mb_sem)) * 100:.2f}%")

if __name__ == "__main__":
    mundo = Mundo2D()
    
    total_arvores_teste = 10_000_000
    total_especies_disponiveis = 1_000

    print(f"Plantando {total_arvores_teste:,} árvores no cenário 2D... Aguarde.")

    # Massa de dados para o teste
    for i in range(10000):
        id_especie = random.randint(0, total_especies_disponiveis - 1)
        mundo.plantar_arvore(
            x=random.randint(0, 1920),
            y=random.randint(0, 1080),
            altura=round(random.uniform(1.5, 18.0), 2),
            largura=round(random.uniform(0.1, 2.5), 2),
            especie=f"Especie_{id_especie}",
            textura=f"Textura_Pesada_PNG_Simulada_Da_Especie_{id_especie}_Com_Muitos_Bytes_De_Informacao",
            sombra=7.5
        )

    exibir_estimativa_memoria(total_arvores_teste, FabricaEspecie.total_especies_criadas())
