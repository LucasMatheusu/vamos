import tkinter as tk

# Criar a janela principal
janela = tk.Tk()
janela.title("Mensagem Especial")
janela.geometry("400x300")

# Criar um rótulo com a mensagem
mensagem = tk.Label(janela, text="Eu te amo, Carolinda!", font=("Helvetica", 16), fg="red")
mensagem.place(x=80, y=80)  # Definir uma posição inicial para o texto

# Variáveis para controlar a direção do movimento
direcao_x = 2
direcao_y = 2

# Função para mover a mensagem
def mover_mensagem():
    global direcao_x, direcao_y

    # Pegar a posição atual do texto
    x, y = mensagem.winfo_x(), mensagem.winfo_y()

    # Atualizar a posição do texto
    x += direcao_x
    y += direcao_y

    # Checar limites da janela para reverter a direção quando atingir as bordas
    if x <= 0 or x >= janela.winfo_width() - mensagem.winfo_width():
        direcao_x = -direcao_x
    if y <= 0 or y >= janela.winfo_height() - mensagem.winfo_height():
        direcao_y = -direcao_y

    # Definir a nova posição do texto
    mensagem.place(x=x, y=y)

    # Repetir a função após 20 milissegundos
    janela.after(20, mover_mensagem)

# Iniciar o movimento
mover_mensagem()

# Iniciar o loop da interface gráfica
janela.mainloop()
