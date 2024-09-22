import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
from database import (
    verificar_login, adicionar_curso, listar_cursos,
    atualizar_curso, deletar_curso, adicionar_usuario,
    listar_usuarios, atualizar_usuario, deletar_usuario,
    adicionar_matricula, listar_matriculas, atualizar_matricula,
    deletar_matricula, adicionar_relatorio, listar_relatorios
)

def mudar_tela(frame):
    frame.tkraise()

def logout(app):
    app.quit()

def criar_interface(app):
    global logotipo
    logotipo = PhotoImage(file="logo.png")
    logotipo = logotipo.subsample(2)  # Redimensionar pela metade

    # Criar os frames (telas)
    tela_login = tk.Frame(app)
    tela_principal = tk.Frame(app)
    tela_cursos = tk.Frame(app)
    tela_usuarios = tk.Frame(app)
    tela_matriculas = tk.Frame(app)
    tela_relatorios = tk.Frame(app)
    tela_configuracoes = tk.Frame(app)
    tela_sobre = tk.Frame(app)

    # Configurar as telas
    for frame in (tela_login, tela_principal, tela_cursos, tela_usuarios, tela_matriculas, tela_relatorios, tela_configuracoes, tela_sobre):
        frame.grid(row=0, column=0, sticky='nsew')

    # Tela de Login
    tk.Label(tela_login, text="Tela de Login").pack(pady=20)
    tk.Label(tela_login, text="Usuário").pack()
    entrada_usuario = tk.Entry(tela_login)
    entrada_usuario.pack()
    tk.Label(tela_login, text="Senha").pack()
    entrada_senha = tk.Entry(tela_login, show="*")
    entrada_senha.pack()

    def realizar_login():
        usuario = entrada_usuario.get()
        senha = entrada_senha.get()
        if verificar_login(usuario, senha):
            mudar_tela(tela_principal)
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    tk.Button(tela_login, text="Login", command=realizar_login).pack(pady=20)

    # Tela Principal
    tk.Label(tela_principal, text="Tela Principal").pack(pady=20)
    tk.Button(tela_principal, text="Gerenciar Cursos", command=lambda: mudar_tela(tela_cursos)).pack()
    tk.Button(tela_principal, text="Gerenciar Usuários", command=lambda: mudar_tela(tela_usuarios)).pack()
    tk.Button(tela_principal, text="Gerenciar Matrículas", command=lambda: mudar_tela(tela_matriculas)).pack()
    tk.Button(tela_principal, text="Relatórios", command=lambda: mudar_tela(tela_relatorios)).pack()
    tk.Button(tela_principal, text="Configurações", command=lambda: mudar_tela(tela_configuracoes)).pack()
    tk.Button(tela_principal, text="Sobre", command=lambda: mudar_tela(tela_sobre)).pack()
    tk.Button(tela_principal, text="Logout", command=lambda: logout(app)).pack(pady=20)

    # Tela de Cursos
    tk.Label(tela_cursos, text="Gerenciamento de Cursos").pack(pady=20)

    # Listar cursos
    lista_cursos = tk.Listbox(tela_cursos)
    lista_cursos.pack(pady=10)

    def atualizar_lista_cursos():
        cursos = listar_cursos()
        lista_cursos.delete(0, tk.END)
        for curso in cursos:
            lista_cursos.insert(tk.END, f"{curso[0]} - {curso[1]}")

    # Botões para CRUD de cursos
    frame_botoes_cursos = tk.Frame(tela_cursos)
    frame_botoes_cursos.pack(pady=10)

    tk.Label(frame_botoes_cursos, text="Nome do Curso:").grid(row=0, column=0)
    entrada_nome_curso = tk.Entry(frame_botoes_cursos)
    entrada_nome_curso.grid(row=0, column=1)

    tk.Label(frame_botoes_cursos, text="Descrição:").grid(row=1, column=0)
    entrada_descricao_curso = tk.Entry(frame_botoes_cursos)
    entrada_descricao_curso.grid(row=1, column=1)

    def adicionar_curso():
        nome_curso = entrada_nome_curso.get()
        descricao_curso = entrada_descricao_curso.get()
        if nome_curso and descricao_curso:
            adicionar_curso(nome_curso, descricao_curso)
            atualizar_lista_cursos()
            messagebox.showinfo("Sucesso", "Curso adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def deletar_curso():
        indice_selecionado = lista_cursos.curselection()
        if indice_selecionado:
            id_curso = lista_cursos.get(indice_selecionado)[0].split(" ")[0]
            deletar_curso(id_curso)
            atualizar_lista_cursos()
            messagebox.showinfo("Sucesso", "Curso deletado com sucesso!")
        else:
            messagebox.showerror("Erro", "Selecione um curso!")

    def atualizar_curso():
        indice_selecionado = lista_cursos.curselection()
        if indice_selecionado:
            id_curso = lista_cursos.get(indice_selecionado)[0].split(" ")[0]
            nome_curso = entrada_nome_curso.get()
            descricao_curso = entrada_descricao_curso.get()
            if nome_curso and descricao_curso:
                atualizar_curso(id_curso, nome_curso, descricao_curso)
                atualizar_lista_cursos()
                messagebox.showinfo("Sucesso", "Curso atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            messagebox.showerror("Erro", "Selecione um curso!")

    tk.Button(frame_botoes_cursos, text="Adicionar Curso", command=adicionar_curso).grid(row=2, column=0, padx=10)
    tk.Button(frame_botoes_cursos, text="Deletar Curso", command=deletar_curso).grid(row=2, column=1, padx=10)
    tk.Button(frame_botoes_cursos, text="Atualizar Curso", command=atualizar_curso).grid(row=2, column=2, padx=10)

    # Botão Voltar
    tk.Button(tela_cursos, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Atualizar lista de cursos ao entrar na tela
    atualizar_lista_cursos()

    # Tela de Usuários
    tk.Label(tela_usuarios, text="Gerenciamento de Usuários").pack(pady=20)

    # Listar usuários
    lista_usuarios = tk.Listbox(tela_usuarios)
    lista_usuarios.pack(pady=10)

    def atualizar_lista_usuarios():
        usuarios = listar_usuarios()
        lista_usuarios.delete(0, tk.END)
        for usuario in usuarios:
            lista_usuarios.insert(tk.END, f"{usuario[0]} - {usuario[1]}")

    # Botões para CRUD de usuários
    frame_botoes_usuarios = tk.Frame(tela_usuarios)
    frame_botoes_usuarios.pack(pady=10)

    tk.Label(frame_botoes_usuarios, text="Nome do Usuário:").grid(row=0, column=0)
    entrada_nome_usuario = tk.Entry(frame_botoes_usuarios)
    entrada_nome_usuario.grid(row=0, column=1)

    tk.Label(frame_botoes_usuarios, text="Senha:").grid(row=1, column=0)
    entrada_senha_usuario = tk.Entry(frame_botoes_usuarios, show="*")
    entrada_senha_usuario.grid(row=1, column=1)

    def adicionar_usuario():
        nome_usuario = entrada_nome_usuario.get()
        senha_usuario = entrada_senha_usuario.get()
        if nome_usuario and senha_usuario:
            adicionar_usuario(nome_usuario, senha_usuario)
            atualizar_lista_usuarios()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def deletar_usuario():
        indice_selecionado = lista_usuarios.curselection()
        if indice_selecionado:
            id_usuario = lista_usuarios.get(indice_selecionado)[0].split(" ")[0]
            deletar_usuario(id_usuario)
            atualizar_lista_usuarios()
            messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
        else:
            messagebox.showerror("Erro", "Selecione um usuário!")

    def atualizar_usuario():
        indice_selecionado = lista_usuarios.curselection()
        if indice_selecionado:
            id_usuario = lista_usuarios.get(indice_selecionado)[0].split(" ")[0]
            nome_usuario = entrada_nome_usuario.get()
            senha_usuario = entrada_senha_usuario.get()
            if nome_usuario and senha_usuario:
                atualizar_usuario(id_usuario, nome_usuario, senha_usuario)
                atualizar_lista_usuarios()
                messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            messagebox.showerror("Erro", "Selecione um usuário!")

    tk.Button(frame_botoes_usuarios, text="Adicionar Usuário", command=adicionar_usuario).grid(row=2, column=0, padx=10)
    tk.Button(frame_botoes_usuarios, text="Deletar Usuário", command=deletar_usuario).grid(row=2, column=1, padx=10)
    tk.Button(frame_botoes_usuarios, text="Atualizar Usuário", command=atualizar_usuario).grid(row=2, column=2, padx=10)

    # Botão Voltar
    tk.Button(tela_usuarios, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Atualizar lista de usuários ao entrar na tela
    atualizar_lista_usuarios()

    # Tela de Matrículas
    tk.Label(tela_matriculas, text="Gerenciamento de Matrículas").pack(pady=20)

    # Listar matrículas
    lista_matriculas = tk.Listbox(tela_matriculas)
    lista_matriculas.pack(pady=10)

    def atualizar_lista_matriculas():
        matriculas = listar_matriculas()
        lista_matriculas.delete(0, tk.END)
        for matricula in matriculas:
            lista_matriculas.insert(tk.END, f"{matricula[0]} - {matricula[1]} - {matricula[2]}")

    # Botões para CRUD de matrículas
    frame_botoes_matriculas = tk.Frame(tela_matriculas)
    frame_botoes_matriculas.pack(pady=10)

    tk.Label(frame_botoes_matriculas, text="ID do Usuário:").grid(row=0, column=0)
    entrada_id_usuario = tk.Entry(frame_botoes_matriculas)
    entrada_id_usuario.grid(row=0, column=1)

    tk.Label(frame_botoes_matriculas, text="ID do Curso:").grid(row=1, column=0)
    entrada_id_curso = tk.Entry(frame_botoes_matriculas)
    entrada_id_curso.grid(row=1, column=1)

    tk.Label(frame_botoes_matriculas, text="Data de Matrícula:").grid(row=2, column=0)
    entrada_data_matricula = tk.Entry(frame_botoes_matriculas)
    entrada_data_matricula.grid(row=2, column=1)

    def adicionar_matricula():
        id_usuario = entrada_id_usuario.get()
        id_curso = entrada_id_curso.get()
        data_matricula = entrada_data_matricula.get()
        if id_usuario and id_curso and data_matricula:
            adicionar_matricula(id_usuario, id_curso, data_matricula)
            atualizar_lista_matriculas()
            messagebox.showinfo("Sucesso", "Matrícula adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def deletar_matricula():
        indice_selecionado = lista_matriculas.curselection()
        if indice_selecionado:
            id_usuario = lista_matriculas.get(indice_selecionado)[0].split(" ")[0]
            id_curso = lista_matriculas.get(indice_selecionado)[0].split(" ")[2]
            deletar_matricula(id_usuario, id_curso)
            atualizar_lista_matriculas()
            messagebox.showinfo("Sucesso", "Matrícula deletada com sucesso!")
        else:
            messagebox.showerror("Erro", "Selecione uma matrícula!")

    def atualizar_matricula():
        indice_selecionado = lista_matriculas.curselection()
        if indice_selecionado:
            id_usuario = lista_matriculas.get(indice_selecionado)[0].split(" ")[0]
            id_curso = lista_matriculas.get(indice_selecionado)[0].split(" ")[2]
            data_matricula = entrada_data_matricula.get()
            if id_usuario and id_curso and data_matricula:
                atualizar_matricula(id_usuario, id_curso, data_matricula)
                atualizar_lista_matriculas()
                messagebox.showinfo("Sucesso", "Matrícula atualizada com sucesso!")
            else:
                messagebox.showerror("Erro", "Preencha todos os campos!")
        else:
            messagebox.showerror("Erro", "Selecione uma matrícula!")

    tk.Button(frame_botoes_matriculas, text="Adicionar Matrícula", command=adicionar_matricula).grid(row=3, column=0, padx=10)
    tk.Button(frame_botoes_matriculas, text="Deletar Matrícula", command=deletar_matricula).grid(row=3, column=1, padx=10)
    tk.Button(frame_botoes_matriculas, text="Atualizar Matrícula", command=atualizar_matricula).grid(row=3, column=2, padx=10)

    # Botão Voltar
    tk.Button(tela_matriculas, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Atualizar lista de matrículas ao entrar na tela
    atualizar_lista_matriculas()

    # Tela de Relatórios
    tk.Label(tela_relatorios, text="Relatórios").pack(pady=20)

    # Botões para adicionar relatório
    frame_relatorio = tk.Frame(tela_relatorios)
    frame_relatorio.pack(pady=10)

    tk.Label(frame_relatorio, text="Adicionar Relatório:").grid(row=0, column=0)
    entrada_relatorio = tk.Entry(frame_relatorio, width=50)
    entrada_relatorio.grid(row=0, column=1)

    def adicionar_relatorio():
        texto_relatorio = entrada_relatorio.get()
        if texto_relatorio:
            adicionar_relatorio(texto_relatorio)
            messagebox.showinfo("Sucesso", "Relatório adicionado com sucesso!")
            entrada_relatorio.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Preencha o campo do relatório!")

    tk.Button(frame_relatorio, text="Adicionar", command=adicionar_relatorio).grid(row=0, column=2, padx=10)

    # Botão Voltar
    tk.Button(tela_relatorios, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Tela de Configurações
    tk.Label(tela_configuracoes, text="Configurações do Sistema").pack(pady=20)

    # Configurações básicas
    tk.Label(tela_configuracoes, text="Configurações básicas do sistema:").pack()
    tk.Label(tela_configuracoes, text="Exemplo de configuração 1").pack()
    tk.Label(tela_configuracoes, text="Exemplo de configuração 2").pack()

    # Botão Voltar
    tk.Button(tela_configuracoes, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Tela Sobre
    tk.Label(tela_sobre, text="Sobre o Sistema").pack(pady=20)
    tk.Label(tela_sobre, image=logotipo).pack(pady=10)
    tk.Label(tela_sobre, text="Sistema de Gerenciamento de Cursos.").pack(pady=10)
    tk.Button(tela_sobre, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Mostrar a tela de login no início
    mudar_tela(tela_login)
