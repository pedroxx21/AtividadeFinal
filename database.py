import mysql.connector

# Função para conectar ao banco de dados
def conectar():
    conexao = mysql.connector.connect(
        host="localhost",  # Altere se necessário
        user="admin",  # Usuário do MySQL
        password="123",  # Senha do MySQL
        database="sistema_educacional"  # Nome do banco de dados
    )
    return conexao

# Função para verificar login no banco de dados
def verificar_login(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "SELECT * FROM usuarios WHERE nome = %s AND senha = %s"
    cursor.execute(query, (nome, senha))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario

# Função para adicionar curso
def adicionar_curso(nome, descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO cursos (nome, descricao) VALUES (%s, %s)"
    cursor.execute(query, (nome, descricao))
    conexao.commit()
    conexao.close()

# Função para listar cursos
def listar_cursos():
    conexao = conectar()
    cursor = conexao.cursor()
    query = "SELECT * FROM cursos"
    cursor.execute(query)
    cursos = cursor.fetchall()
    conexao.close()
    return cursos

# Função para atualizar curso
def atualizar_curso(id, nome, descricao):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "UPDATE cursos SET nome = %s, descricao = %s WHERE id = %s"
    cursor.execute(query, (nome, descricao, id))
    conexao.commit()
    conexao.close()

# Função para deletar curso
def deletar_curso(id):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "DELETE FROM cursos WHERE id = %s"
    cursor.execute(query, (id,))
    conexao.commit()
    conexao.close()

# Função para adicionar usuário
def adicionar_usuario(nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)"
    cursor.execute(query, (nome, senha))
    conexao.commit()
    conexao.close()

# Função para listar usuários
def listar_usuarios():
    conexao = conectar()
    cursor = conexao.cursor()
    query = "SELECT * FROM usuarios"
    cursor.execute(query)
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

# Função para atualizar usuário
def atualizar_usuario(id, nome, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "UPDATE usuarios SET nome = %s, senha = %s WHERE id = %s"
    cursor.execute(query, (nome, senha, id))
    conexao.commit()
    conexao.close()

# Função para deletar usuário
def deletar_usuario(id):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "DELETE FROM usuarios WHERE id = %s"
    cursor.execute(query, (id,))
    conexao.commit()
    conexao.close()

# Função para adicionar matrícula
def adicionar_matricula(usuario_id, curso_id, data_matricula):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO matriculas (usuario_id, curso_id, data_matricula) VALUES (%s, %s, %s)"
    cursor.execute(query, (usuario_id, curso_id, data_matricula))
    conexao.commit()
    conexao.close()

# Função para listar matrículas
def listar_matriculas():
    conexao = conectar()
    cursor = conexao.cursor()
    query = "SELECT * FROM matriculas"
    cursor.execute(query)
    matriculas = cursor.fetchall()
    conexao.close()
    return matriculas

# Função para atualizar matrícula
def atualizar_matricula(usuario_id, curso_id, data_matricula):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "UPDATE matriculas SET data_matricula = %s WHERE usuario_id = %s AND curso_id = %s"
    cursor.execute(query, (data_matricula, usuario_id, curso_id))
    conexao.commit()
    conexao.close()

# Função para deletar matrícula
def deletar_matricula(usuario_id, curso_id):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "DELETE FROM matriculas WHERE usuario_id = %s AND curso_id = %s"
    cursor.execute(query, (usuario_id, curso_id))
    conexao.commit()
    conexao.close()

# Função para adicionar relatório
def adicionar_relatorio(texto):
    conexao = conectar()
    cursor = conexao.cursor()
    query = "INSERT INTO relatorios (texto) VALUES (%s)"
    cursor.execute(query, (texto,))
    conexao.commit()
    conexao.close()

# Função para listar relatórios
def listar_relatorios():
    conexao = conectar()
    cursor = conexao.cursor()
    query = "SELECT * FROM relatorios"
    cursor.execute(query)
    relatorios = cursor.fetchall()
    conexao.close()
    return relatorios
