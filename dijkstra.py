import heapq

def dijkstra(grafo, no_inicial, tasks):
    distances = {}  # Dicionário para armazenar as distâncias mínimas
    previous = {}   # Dicionário para armazenar o nó anterior no caminho mais curto
    queue = []      # Fila de prioridade para processar os nós

    # Inicializa as distâncias com infinito para todos os nós, exceto o nó inicial
    for node in grafo:
        distances[node] = float('inf')
    distances[no_inicial] = 0

    # Adiciona o nó inicial na fila de prioridade
    heapq.heappush(queue, (distances[no_inicial], no_inicial))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Verifica se o nó atual é um dos nós alvo
        if current_node in tasks:
            # Constrói o caminho mínimo até o nó atual
            path = []
            while current_node != no_inicial:
                path.append(current_node)
                current_node = previous[current_node]
            path.append(no_inicial)
            path.reverse()
            return path

        # Se a distância atual for maior que a distância armazenada, pula para o próximo nó
        if current_distance > distances[current_node]:
            continue

        # Explora os vizinhos do nó atual
        for neighbor, weight in grafo[current_node].items():
            distance = current_distance + weight

            # Se a distância até o vizinho for menor do que a distância armazenada, atualiza
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Se não foi possível encontrar um caminho para os nós alvo
    return None
