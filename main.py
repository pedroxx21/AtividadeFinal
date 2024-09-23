import tkinter as tk
from interface import criar_interface


app = tk.Tk()
app.title("Sistema de Gerenciamento")
app.geometry("640x640")
criar_interface(app)


app.mainloop()

