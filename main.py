import tkinter as tk
from tkinter import messagebox


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
btn_adicionar_missoes = tk.Button(frame, text="Adicionar Missões", command=adicionar_missoes, width=30, height=2)
btn_adicionar_missoes.pack(pady=10)

btn_sair = tk.Button(frame, text="Sair", command=sair, width=30, height=2)
btn_sair.pack()

# Loop principal da janela
janela_principal.mainloop()
