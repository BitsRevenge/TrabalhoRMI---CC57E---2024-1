import mysql.connector
from kivy.app import App
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

class TelaRegistrar(MDScreen):
    pass
    def connect(self):
        input_nome = self.ids["nome"].text
        input_email = self.ids["email"].text
        input_senha = self.ids["senha"].text

        config = {
            'user': 'root',
            'password': SENHA,
            'host': '127.0.0.1',
            'database': 'db_dadosRMI',
        }
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        if input_nome != "" and input_email != "" and input_senha != "":
            try:

                query = "INSERT INTO tb_usuario (nome, email, senha) VALUES (%s, %s, %s);"
                cursor.execute(query, (input_nome, input_email, input_senha))
                conn.commit()

                query = "SELECT count(*) FROM tb_usuario WHERE email = %s AND senha = %s"
                cursor.execute(query, (input_email, input_senha))
                dados = cursor.fetchall()
                print(dados)
                if dados[0][0] == 1:
                    toast("Registrado com sucesso!")
                else:
                    toast("Nome, email ou senha inválidos")
            except:
                toast("Email ou senha inválidos")
        else:
            toast("Você precisa preencher todos os campos.")

        # pass

#
# MDTopAppBar:
#             md_bg_color: 1,1,1,0
#             elevation: 0
#             type: "top"
#             pos_hint: {"top": 1}
#             left_action_items: [["arrow-left", lambda x: root.callback()]]
