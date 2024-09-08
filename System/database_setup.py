import sqlite3

def criar_tabela():
    conn = sqlite3.connect("clinica.db")
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS consulta (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_completo TEXT,
                        idade INTEGER,
                        sexo TEXT,
                        data_nasc TEXT,
                        estado_civil TEXT,
                        telefone TEXT,
                        email TEXT,
                        nome_contato TEXT,
                        telefone_contato TEXT,
                        medico TEXT,
                        telefone_medico TEXT,
                        hospital TEXT,
                        pressao_arterial TEXT,
                        frequencia_cardiaca TEXT,
                        temperatura REAL,
                        peso REAL,
                        altura REAL,
                        data_cirurgia TEXT,
                        diabetes INTEGER,
                        hipertensao INTEGER,
                        tabagismo INTEGER,
                        cirurgias INTEGER,
                        antecedentes_alergicos INTEGER,
                        antecedentes_oncologicos INTEGER,
                        ingere_alcool INTEGER,
                        usa_anticoncepcional INTEGER,
                        ciclo_menstrual INTEGER,
                        gestante INTEGER,
                        tratamento_medico INTEGER,
                        marca_passo INTEGER,
                        observacoes TEXT)''')
    
    conn.commit()
    conn.close()