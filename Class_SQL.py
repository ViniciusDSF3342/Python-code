import sqlite3 as sq
import hashlib as sh

class SQLITE:

    def __init__(self, nomeBanco: str):
        self.nomeBanco = nomeBanco

    def conectarBanco(self):
        database = sq.connect(f'/Users/Viniciusdsf/first-flet-app/Tela de login/assets/databases/users.db')
        cursor = database.cursor()

        return database, cursor
    
    
    def criarTabela(self, nomeTabela: str, Colunas: list, Colunastipo: list):

        if type(Colunas) == list and type(Colunastipo) == list:
            if len(Colunas) == len(Colunastipo):

                database, cursor = self.conectarBanco()
                colunas = []

                for i in range(len(Colunas)):
                    colunas.append(f'{Colunas[i]} {Colunastipo[i]}')

                    ColunaSQL = ','.join(colunas)

                cursor.execute(f'CREATE TABLE IF NOT EXISTS {nomeTabela} ({ColunaSQL})')

                database.commit()
                database.close()

            else:
                print('Não foi possível criar tabela')
        
        else:
            print('Não foi possível criar tabela')          



    def inserirDados(self, nomeTabela:str, Colunas: list, dados: list):

        if type(Colunas) == list and type(dados) == list:
            if len(Colunas) == len(dados):

                database, cursor = self.conectarBanco()
                Dados = []

                for dado in dados:
                    if type(dado) == str:
                        Dados.append(f"'{dado}'")

                    else:
                        Dados.append(str(dado))

                ColunaSQL = ','.join(Colunas)
                DadoSQL = ','.join(Dados)

                cursor.execute(f'INSERT INTO {nomeTabela} ({ColunaSQL}) VALUES ({DadoSQL})')

                database.commit()
                database.close()
            else:
                print('Não foi possível salvar os dados')

        else:
                print('Não foi possível salvar os dados')       


    def editarDados(self, nomeTabela: str, Coluna: str, Valor: str, conditions: str):

        database, cursor = self.conectarBanco()

        if conditions == '':
            cursor.execute(f'UPDATE {nomeTabela} SET {Coluna} = {Valor}')

        else:
            cursor.execute(f'UPDATE {nomeTabela} SET {Coluna} = {Valor} WHERE {conditions}')

        database.commit()
        database.close()

    def apagarDados(self, nomeTabela:str, conditions: str = ''):

        database, cursor = self.conectarBanco()

        if conditions == '':
            cursor.execute(f'DELETE FROM {nomeTabela}')

        else:
            cursor.execute(f'DELETE FROM {nomeTabela} WHERE {conditions}')

        database.commit()
        database.close()

    def verDados(self, nomeTabela: str, Colunas: list ='*', conditions: str =''):

        database, cursor = self.conectarBanco()

        ColunaSQL = ','.join(Colunas)

        if conditions == '':
            cursor.execute(f'SELECT {ColunaSQL} FROM {nomeTabela}')

        else:
            cursor.execute(f'SELECT {ColunaSQL} FROM {nomeTabela} WHERE {conditions}')   

        dados = cursor.fetchall()

        database.commit()
        database.close()

        return dados


    def encriptar_senha(self, senha: str):

        hash = sh.sha512()

        hash.update(bytes(senha, 'UTF-8'))

        password_hashed = hash.hexdigest()

        return password_hashed

# Sqlite = SQLITE('users')
# Sqlite.criarTabela('usuarios', ['nome', 'idade', 'senha'],['TEXT', 'INTEGER', 'TEXT'])
# Sqlite.inserirDados('usuarios', ['nome', 'idade', 'senha'], ['Vinicius', '31', 'abc123'])
# Sqlite.editarDados('usuarios', 'idade', '25', '')
# Sqlite.apagarDados('usuarios', "nome='Vinnyboto'")
# print(Sqlite.verDados('usuarios'))

Sqlite = SQLITE('users')
senha = Sqlite.encriptar_senha('Vinnyboto123')
Sqlite.inserirDados('usuarios',['nome', 'idade', 'senha'], ['Vinicius', 31, senha])
print(Sqlite.verDados('usuarios'))
