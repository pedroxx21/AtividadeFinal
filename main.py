import tkinter as tk
from interface import criar_interface

# Inicializa o aplicativo
app = tk.Tk()
app.title("Sistema de Gerenciamento")
app.geometry("600x400")

# Cria a interface
criar_interface(app)

# Inicia o loop da aplicação
app.mainloop()

#ok