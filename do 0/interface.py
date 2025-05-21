import tkinter as tk

# Cria a janela principal
janela = tk.Tk()

# Define o título e o tamanho da janela
janela.title("Minha Primeira Interface")
janela.geometry("390x345")  # Define a largura e altura da janela

# Cria um rótulo de texto e o adiciona à janela
texto = tk.Label(janela, text="Olá")  # Usa Label para exibir o texto "Olá"
texto.pack(pady=10)  # Adiciona o rótulo com um espaçamento vertical

# Função chamada quando o botão é clicado
def clique_do_botao():
    texto.config(text="Botão foi clicado!")  # Altera o texto do rótulo

# Cria um botão e associa a função ao clicar
botao = tk.Button(janela, text="Clique aqui", command=clique_do_botao, bg="green", fg="white", font=("Arial", 12))
botao.pack(pady=10)  # Adiciona o botão com espaçamento vertical

# Mantém a janela aberta
janela.mainloop()

