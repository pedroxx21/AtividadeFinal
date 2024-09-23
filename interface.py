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
    logotipo = logotipo.subsample(2)  


    tela_login = tk.Frame(app)
    tela_principal = tk.Frame(app)
    tela_cursos = tk.Frame(app)
    tela_usuarios = tk.Frame(app)
    tela_matriculas = tk.Frame(app)
    tela_relatorios = tk.Frame(app)
    tela_configuracoes = tk.Frame(app)
    tela_sobre = tk.Frame(app)

    
    for frame in (tela_login, tela_principal, tela_cursos, tela_usuarios, tela_matriculas, tela_relatorios, tela_configuracoes, tela_sobre):
        frame.grid(row=0, column=0, sticky='nsew')

   
    tk.Label(tela_login, image=logotipo).pack(pady=10)  # Adiciona o logotipo na tela de login
    tk.Label(tela_login, text="Tela de Login", font=("Arial", 16)).pack(pady=20)
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

    
    tk.Label(tela_principal, image=logotipo).pack(pady=10)
    tk.Label(tela_principal, text="Tela Principal").pack(pady=20)
    tk.Button(tela_principal, text="Gerenciar Cursos", command=lambda: mudar_tela(tela_cursos)).pack()
    tk.Button(tela_principal, text="Gerenciar Usuários", command=lambda: mudar_tela(tela_usuarios)).pack()
    tk.Button(tela_principal, text="Gerenciar Matrículas", command=lambda: mudar_tela(tela_matriculas)).pack()
    tk.Button(tela_principal, text="Relatórios", command=lambda: mudar_tela(tela_relatorios)).pack()
    tk.Button(tela_principal, text="Configurações", command=lambda: mudar_tela(tela_configuracoes)).pack()
    tk.Button(tela_principal, text="Sobre", command=lambda: mudar_tela(tela_sobre)).pack()
    tk.Button(tela_principal, text="Logout", command=lambda: logout(app)).pack(pady=20)

    
    tk.Label(tela_cursos, text="Gerenciamento de Cursos").pack(pady=20)

   
    lista_cursos = tk.Listbox(tela_cursos)
    lista_cursos.pack(pady=10)

    def atualizar_lista_cursos():
        cursos = listar_cursos()
        lista_cursos.delete(0, tk.END)
        for curso in cursos:
            lista_cursos.insert(tk.END, f"{curso[0]} - {curso[1]}")

   
    frame_botoes_cursos = tk.Frame(tela_cursos)
    frame_botoes_cursos.pack(pady=10)

    tk.Label(frame_botoes_cursos, text="Nome do Curso:").grid(row=0, column=0)
    entrada_nome_curso = tk.Entry(frame_botoes_cursos)
    entrada_nome_curso.grid(row=0, column=1)

    tk.Label(frame_botoes_cursos, text="Descrição:").grid(row=1, column=0)
    entrada_descricao_curso = tk.Entry(frame_botoes_cursos)
    entrada_descricao_curso.grid(row=1, column=1)

    def adicionar_curso_interface():
        nome_curso = entrada_nome_curso.get()
        descricao_curso = entrada_descricao_curso.get()
        if nome_curso and descricao_curso:
            adicionar_curso(nome_curso, descricao_curso)
            atualizar_lista_cursos()
            messagebox.showinfo("Sucesso", "Curso adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def deletar_curso_interface():
        indice_selecionado = lista_cursos.curselection()
        if indice_selecionado:
            id_curso = lista_cursos.get(indice_selecionado)[0].split(" ")[0]
            deletar_curso(id_curso)
            atualizar_lista_cursos()
            messagebox.showinfo("Sucesso", "Curso deletado com sucesso!")
        else:
            messagebox.showerror("Erro", "Selecione um curso!")

    def atualizar_curso_interface():
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

    tk.Button(frame_botoes_cursos, text="Adicionar Curso", command=adicionar_curso_interface).grid(row=2, column=0, padx=10)
    tk.Button(frame_botoes_cursos, text="Deletar Curso", command=deletar_curso_interface).grid(row=2, column=1, padx=10)
    tk.Button(frame_botoes_cursos, text="Atualizar Curso", command=atualizar_curso_interface).grid(row=2, column=2, padx=10)

    
    tk.Button(tela_cursos, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    
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

    def adicionar_usuario_interface():
        nome_usuario = entrada_nome_usuario.get()
        senha_usuario = entrada_senha_usuario.get()
        if nome_usuario and senha_usuario:
            adicionar_usuario(nome_usuario, senha_usuario)
            atualizar_lista_usuarios()
            messagebox.showinfo("Sucesso", "Usuário adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def deletar_usuario_interface():
        indice_selecionado = lista_usuarios.curselection()
        if indice_selecionado:
            id_usuario = lista_usuarios.get(indice_selecionado)[0].split(" ")[0]
            deletar_usuario(id_usuario)  # Essa chamada se refere à função do banco de dados
            atualizar_lista_usuarios()
            messagebox.showinfo("Sucesso", "Usuário deletado com sucesso!")
        else:
            messagebox.showerror("Erro", "Selecione um usuário!")


    def atualizar_usuario_interface():
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

    tk.Button(frame_botoes_usuarios, text="Adicionar Usuário", command=adicionar_usuario_interface).grid(row=2, column=0, padx=10)
    tk.Button(frame_botoes_usuarios, text="Deletar Usuário", command=deletar_usuario_interface).grid(row=2, column=1, padx=10)
    tk.Button(frame_botoes_usuarios, text="Atualizar Usuário", command=atualizar_usuario_interface).grid(row=2, column=2, padx=10)

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

    def adicionar_matricula_interface():
        id_usuario = entrada_id_usuario.get()
        id_curso = entrada_id_curso.get()
        data_matricula = entrada_data_matricula.get()
        if id_usuario and id_curso and data_matricula:
            adicionar_matricula(id_usuario, id_curso, data_matricula)
            atualizar_lista_matriculas()
            messagebox.showinfo("Sucesso", "Matrícula adicionada com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos!")

    def deletar_matricula_interface():
        indice_selecionado = lista_matriculas.curselection()
        if indice_selecionado:
            id_usuario = lista_matriculas.get(indice_selecionado)[0].split(" ")[0]
            id_curso = lista_matriculas.get(indice_selecionado)[0].split(" ")[2]
            deletar_matricula(id_usuario, id_curso)
            atualizar_lista_matriculas()
            messagebox.showinfo("Sucesso", "Matrícula deletada com sucesso!")
        else:
            messagebox.showerror("Erro", "Selecione uma matrícula!")

    def atualizar_matricula_interface():
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

    tk.Button(frame_botoes_matriculas, text="Adicionar Matrícula", command=adicionar_matricula_interface).grid(row=3, column=0, padx=10)
    tk.Button(frame_botoes_matriculas, text="Deletar Matrícula", command=deletar_matricula_interface).grid(row=3, column=1, padx=10)
    tk.Button(frame_botoes_matriculas, text="Atualizar Matrícula", command=atualizar_matricula_interface).grid(row=3, column=2, padx=10)

    # Botão Voltar
    tk.Button(tela_matriculas, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Atualizar lista de matrículas ao entrar na tela
    atualizar_lista_matriculas()

    # Tela de Relatórios
    tk.Label(tela_relatorios, text="Relatórios", font=("Arial", 16)).pack(pady=20)

# Frame para adicionar relatório
    frame_relatorio = tk.Frame(tela_relatorios)
    frame_relatorio.pack(pady=10)

    tk.Label(frame_relatorio, text="Adicionar Relatório:", font=("Arial", 12)).grid(row=0, column=0)
    entrada_relatorio = tk.Entry(frame_relatorio, width=50)
    entrada_relatorio.grid(row=0, column=1)

    def adicionar_relatorio_interface():
        texto_relatorio = entrada_relatorio.get()
        if texto_relatorio:
            adicionar_relatorio(texto_relatorio)  # Passa o texto como argumento
            atualizar_lista_relatorios()
            messagebox.showinfo("Sucesso", "Relatório adicionado com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha o texto do relatório!")

# Botão para adicionar relatório
    tk.Button(frame_relatorio, text="Adicionar", command=adicionar_relatorio_interface).grid(row=0, column=2, padx=10)

# Frame para listar relatórios
    frame_lista_relatorios = tk.Frame(tela_relatorios)
    frame_lista_relatorios.pack(pady=20)

    tk.Label(frame_lista_relatorios, text="Relatórios Adicionados:", font=("Arial", 12)).pack()

# Listar relatórios
    lista_relatorios = tk.Listbox(frame_lista_relatorios, width=70, height=10)
    lista_relatorios.pack(pady=10)

    def atualizar_lista_relatorios():
        relatorios = listar_relatorios()
        lista_relatorios.delete(0, tk.END)
        for relatorio in relatorios:
            lista_relatorios.insert(tk.END, relatorio[1])  # Supondo que relatorio[1] seja o texto do relatório

# Botão para atualizar a lista
    tk.Button(frame_lista_relatorios, text="Atualizar Lista", command=atualizar_lista_relatorios).pack(pady=5)

# Botão Voltar
    tk.Button(tela_relatorios, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

# Atualizar lista de relatórios ao entrar na tela
    atualizar_lista_relatorios()

    # Tela de Configurações
    tk.Label(tela_configuracoes, text="Configurações do Sistema", font=("Arial", 16)).pack(pady=20)

# Alterar Senha
    frame_senha = tk.Frame(tela_configuracoes)
    frame_senha.pack(pady=10)

    tk.Label(frame_senha, text="Alterar Senha:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)
    entrada_nova_senha = tk.Entry(frame_senha, show="*", width=30)
    entrada_nova_senha.grid(row=0, column=1, padx=10, pady=5)

    def alterar_senha():
        nova_senha = entrada_nova_senha.get()
        if nova_senha:
            # Aqui você pode adicionar a lógica para alterar a senha no banco de dados
            messagebox.showinfo("Sucesso", "Senha alterada com sucesso!")
            entrada_nova_senha.delete(0, tk.END)
        else:
            messagebox.showerror("Erro", "Preencha a nova senha!")

    tk.Button(frame_senha, text="Alterar Senha", command=alterar_senha).grid(row=0, column=2, padx=10, pady=5)

# Alterar Tema (Simples)
    frame_tema = tk.Frame(tela_configuracoes)
    frame_tema.pack(pady=10)

    tk.Label(frame_tema, text="Escolher Tema:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5)

    tema_var = tk.StringVar(value="claro")

    def alterar_tema():
        tema_escolhido = tema_var.get()
        if tema_escolhido == "claro":
            app.configure(bg="white")
        else:
            app.configure(bg="gray")
            messagebox.showinfo("Sucesso", f"Tema alterado para {tema_escolhido.capitalize()}!")

    tk.Radiobutton(frame_tema, text="Claro", variable=tema_var, value="claro").grid(row=0, column=1)
    tk.Radiobutton(frame_tema, text="Escuro", variable=tema_var, value="escuro").grid(row=0, column=2)

    tk.Button(frame_tema, text="Aplicar Tema", command=alterar_tema).grid(row=0, column=3, padx=10, pady=5)

# Redefinir Configurações
    def redefinir_configuracoes():
        resposta = messagebox.askyesno("Redefinir Configurações", "Tem certeza que deseja redefinir todas as configurações?")
        if resposta:
            entrada_nova_senha.delete(0, tk.END)
            tema_var.set("claro")
            app.configure(bg="white")
            messagebox.showinfo("Sucesso", "Configurações redefinidas para o padrão!")

    tk.Button(tela_configuracoes, text="Redefinir Configurações", command=redefinir_configuracoes).pack(pady=20)

# Botão Voltar
    tk.Button(tela_configuracoes, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Tela Sobre
    tk.Label(tela_sobre, text="Sobre o Sistema", font=("Arial", 16)).pack(pady=20)
    tk.Label(tela_sobre, image=logotipo).pack(pady=10)
    tk.Label(tela_sobre, text="Sistema de Gerenciamento de Cursos.", font=("Arial", 12)).pack(pady=10)


    texto_empresa = (
    "A PA Tecnozin é uma empresa que se dedica a transformar a gestão educacional "
    "em escolas e faculdades. Com seu sistema intuitivo, facilita a organização das "
    "informações sobre os alunos e os cursos em que estão matriculados. Isso permite "
    "que as instituições acompanhem o desempenho acadêmico, gerenciem matrículas e "
    "monitorem a frequência de forma muito mais prática. Com uma interface amigável e "
    "recursos personalizáveis, a PA Tecnozin ajuda educadores e administradores a otimizar "
    "suas rotinas, promovendo uma comunicação clara entre alunos e professores. O compromisso "
    "da PA Tecnozin é inovar na educação, oferecendo ferramentas que tornam a gestão mais integrada "
    "e eficiente, sempre com foco no aprendizado e no desenvolvimento dos estudantes."
)

    tk.Label(tela_sobre, text=texto_empresa, wraplength=400, justify="left").pack(pady=10)

    tk.Button(tela_sobre, text="Voltar", command=lambda: mudar_tela(tela_principal)).pack(pady=20)

    # Mostrar a tela de login no início
    mudar_tela(tela_login)