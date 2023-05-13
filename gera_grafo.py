def gera_grafo(G):
    # Adiciona arestas com pesos do mapa
    def gera_grafo(G):
        # Adiciona nós nas salas
        G.add_node('caf')
        G.add_node('arma')
        G.add_node('o2')
        G.add_node('navega')
        G.add_node('escudo')
        G.add_node('comun')
        G.add_node('adm')
        G.add_node('armazena')
        G.add_node('eletri')
        G.add_node('enfermaria')
        G.add_node('motorSup')
        G.add_node('reator')
        G.add_node('motorInf')

        # Adiciona os nós das tasks
        G.add_node('fiacaoCaf')
        G.add_node('esvaziaLixoCaf')
        G.add_node('fiacaoArmazena')
        G.add_node('esvaziaEscotilhaArmazena')
        G.add_node('esvaziaLixoArmazena')
        G.add_node('asteroide')
        G.add_node('cartaoAdm')
        G.add_node('scanEnfer')
        G.add_node('inspecAmostraEnfer')
        G.add_node('desbloqReator')
        G.add_node('ligaReator')
        G.add_node('esvaziaEscotilhaO2')
        G.add_node('limpaFiltroO2')
        G.add_node('estabilizaDirecaoNavega')
        G.add_node('mapeaRotaNavega')
        G.add_node('fiacaoEletri')
        G.add_node('calibraDistribuEletri')
        G.add_node('reativaEscudo')

        # Adiciona arestas com pesos do mapa
        G.add_edge('caf', 'arma', peso=5)
        G.add_edge('arma', 'o2', peso=3)
        G.add_edge('arma', 'navega', peso=5)
        G.add_edge('arma', 'escudo', peso=8)
        G.add_edge('escudo', 'comun', peso=3)
        G.add_edge('caf', 'adm', peso=7)
        G.add_edge('caf', 'armazena', peso=10)
        G.add_edge('armazena', 'comun', peso=4)
        G.add_edge('armazena', 'eletri', peso=6)
        G.add_edge('caf', 'enfermaria', peso=6)
        G.add_edge('caf', 'motorSup', peso=10)
        G.add_edge('motorSup', 'reator', peso=6)
        G.add_edge('motorSup', 'motorInf', peso=8)
        G.add_edge('motorInf', 'eletri', peso=7)

        # Adiciona arestas com pesos das tasks
        G.add_edge('caf', 'fiacaoCaf', peso=2)
        G.add_edge('caf', 'esvaziaLixoCaf', peso=2)
        G.add_edge('armazena', 'fiacaoArmazena', peso=2)
        G.add_edge('armazena', 'esvaziaEscotilhaArmazena', peso=2)
        G.add_edge('armazena', 'esvaziaLixoArmazena', peso=2)
        G.add_edge('arma', 'asteroide', peso=1)
        G.add_edge('adm', 'cartaoAdm', peso=1)
        G.add_edge('enfermaria', 'scanEnfer', peso=1)
        G.add_edge('enfermaria', 'inspecAmostraEnfer', peso=1)
        G.add_edge('reator', 'desbloqReator', peso=1)
        G.add_edge('reator', 'ligaReator', peso=1)
        G.add_edge('o2', 'esvaziaEscotilhaO2', peso=1)
        G.add_edge('o2', 'limpaFiltroO2', peso=1)
        G.add_edge('navega', 'estabilizaDirecaoNavega', peso=1)
        G.add_edge('navega', 'mapeaRotaNavega', peso=1)
        G.add_edge('eletri', 'fiacaoEletri', peso=1)
        G.add_edge('eletri', 'calibraDistribuEletri', peso=1)
        G.add_edge('escudo', 'reativaEscudo', peso=1)

    return G


def mapear_perguntas_nos(perguntas):
    mapeamento = {
        "Acabar com os Asteroides - Weapons": 'asteroide',
        "Arrumar a Fiação - Electrical": 'fiacaoEletri',
        "Arrumar a Fiação - Storage": 'fiacaoArmazena',
        "Arrumar a Fiação - Cafeteria": 'fiacaoCaf',
        "Calibrar o Distribuidor - Electrical": 'calibraDistribuEletri',
        "Desbloquear Colectores - Reactor": 'desbloqReator',
        "Esvaziar Escotilha - O2": 'esvaziaEscotilhaO2',
        "Esvaziar Escotilha - Storage": 'esvaziaEscotilhaArmazena',
        "Esvaziar o lixo - Cafeteria": 'esvaziaLixoCaf',
        "Esvaziar o lixo - Storage": 'esvaziaLixoArmazena',
        "Estabilizar a Direção - Navigation": 'estabilizaDirecaoNavega',
        "Enviar Scan - Medbay": 'scanEnfer',
        "Ligar Reator - Reactor": 'ligaReator',
        "Limpe o Filtro O2 - O2": 'limpaFiltroO2',
        "Inspecionar Amostra - Medbay": 'inspecAmostraEnfer',
        "Mapear Rota - Navigation": 'mapeaRotaNavega',
        "Passar o Cartão - Admin": 'cartaoAdm',
        "Reativar Escudos - Shields": 'reativaEscudo'
    }
    return mapeamento
