import tkinter as tk
from PIL import ImageTk, Image
import networkx as nx

def mapa():
    # Criar janela
    mapa = tk.Toplevel(janela_principal)
    mapa.resizable(False, False)
    mapa.geometry("960x540")
    mapa.title("Mapa de Tasks")

    # Carregar a imagem de fundo
    imagem_fundo = Image.open("among-us-skeld.png")
    imagem_fundo = imagem_fundo.resize((960, 540), Image.ANTIALIAS)  # Ajustar o tamanho da imagem conforme necessário
    imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

    # Criar um rótulo para exibir a imagem de fundo
    rotulo_fundo = tk.Label(mapa, image=imagem_fundo)
    rotulo_fundo.place(x=0, y=0, relwidth=1, relheight=1)  # Posicionar o rótulo para preencher toda a janela

    mapa.mainloop()

def center_window(window):
    # Função para centralizar uma janela na tela
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def adicionar_missoes():
    # Função que será executada quando o botão "Adicionar Missões" for pressionado
    janela_tasks = tk.Toplevel(janela_principal)
    janela_tasks.title("Tasks")
    janela_tasks.geometry("800x600")
    janela_tasks.resizable(False, False)

    # Centraliza a nova janela
    center_window(janela_tasks)

    # Dicionário para armazenar as variáveis das perguntas
    perguntas_vars = {}

    # Frame para conter as perguntas
    frame_perguntas = tk.Frame(janela_tasks)
    frame_perguntas.pack(anchor="w", padx=20, pady=20)

    # Função para atualizar o dicionário de respostas
    def atualizar_respostas(pergunta):
        perguntas_vars[pergunta].set(not perguntas_vars[pergunta].get())

# Adicionar as perguntas
def adicionar_missoes():
    # Função que será executada quando o botão "Adicionar Missões" for pressionado
    janela_tasks = tk.Toplevel(janela_principal)
    janela_tasks.title("Tasks")
    janela_tasks.geometry("900x700")
    janela_tasks.resizable(False, False)

    # Centraliza a nova janela
    center_window(janela_tasks)

    # Perguntas
    perguntas = [
        "Acabar com os Asteroides - Weapons",
        "Arrumar a Fiação - Electrical",
        "Arrumar a Fiação - Storage",
        "Arrumar a Fiação - Cafeteria",
        "Calibrar o Distribuidor - Electrical",
        "Desbloquear Colectores - Reactor",
        "Esvaziar Escotilha - O2",
        "Esvaziar Escotilha - Storage",
        "Esvaziar o lixo - Cafeteria",
        "Esvaziar o lixo - Storage",
        "Estabilizar a Direção - Navigation",
        "Enviar Scan - Medbay",
        "Ligar Reator - Reactor",
        "Limpe o Filtro O2 - O2",
        "Inspecionar Amostra - Medbay",
        "Mapear Rota - Navigation",
        "Passar o Cartão - Admin",
        "Reativar Escudos - Shields"
    ]
    perguntas_vars = []

    label_tasks = tk.Label(janela_tasks, text="Selecione as tasks (Task - Local)", font=("Arial", 20, "bold"),
                               width=30, justify="center")
    label_tasks.pack(pady=10)

    for pergunta in perguntas:
        pergunta_var = tk.IntVar()
        perguntas_vars.append(pergunta_var)
        chk_pergunta = tk.Checkbutton(janela_tasks, text=pergunta, variable=pergunta_var)
        chk_pergunta.pack(anchor="w", padx=20, pady=5)


    def confirmar():
        respostas = []
        for pergunta, pergunta_var in zip(perguntas, perguntas_vars):
            if pergunta_var.get():
                respostas.append(pergunta)
        janela_tasks.destroy()
        print("Respostas", f"As perguntas selecionadas foram: {respostas}")
        mapa()

    # Botão para confirmar as respostas
    btn_confirmar = tk.Button(janela_tasks, text="Confirmar", command=confirmar)
    btn_confirmar.pack(pady=10)

def sair():
    # Função que será executada quando o botão "Sair" for pressionado
    janela_principal.quit()


# Criação da janela principal
janela_principal = tk.Tk()
janela_principal.title("Otimização de Tasks Among Us")
janela_principal.geometry("800x600")
janela_principal.resizable(False, False)

# Centraliza a janela principal
center_window(janela_principal)

# Criação do frame para centralizar os botões
frame = tk.Frame(janela_principal)
frame.pack(pady=200)

# Criação dos botões
btn_adicionar_missoes = tk.Button(frame, text="Adicionar Tasks", command=adicionar_missoes, width=30, height=2)
btn_adicionar_missoes.pack(pady=10)

btn_sair = tk.Button(frame, text="Sair", command=sair, width=30, height=2)
btn_sair.pack()

# Loop principal da janela
janela_principal.mainloop()

# Cria o grafo
def grafo(num_no):
    G = nx.Graph()

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

    # Imprime as arestas com seus pesos
    for u, v, d in G.edges(data=True):
        print(f"{u} - {v}: {d['weight']}")
