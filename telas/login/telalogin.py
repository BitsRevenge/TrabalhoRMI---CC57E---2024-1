import mysql.connector
from kivy.app import App
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

from client import Chatter, DaemonThread
from server import ChatBox
from telas.listagempessoas.telapessoas import TelaPessoas
import variaveis_globais

class TelaLogin(MDScreen):
    pass

    def retornar_fields(self):
        input_email = self.ids["email"].text
        input_senha = self.ids["senha"].text
        variaveis_globais.email_user = input_email
        variaveis_globais.senha_user = input_senha

        conn = mysql.connector.connect(**variaveis_globais.config)
        cursor = conn.cursor()

        try:
            query = "SELECT count(*) FROM tb_usuario WHERE email = %s AND senha = %s"
            cursor.execute(query, (input_email, input_senha))
            dados = cursor.fetchall()
        except:
            pass
        else:
            variaveis_globais.nome_user = dados[0][0]

    # def connect(self):
    #
    #     input_email = self.ids["email"].text
    #     input_senha = self.ids["senha"].text
    #
    #     config = {
    #         'user': 'root',
    #         'password': '1234',
    #         'host': '127.0.0.1',
    #         'database': 'db_dadosRMI',
    #     }
    #     conn = mysql.connector.connect(**config)
    #     cursor = conn.cursor()
    #
    #     try:
    #         query = "SELECT count(*) FROM tb_usuario WHERE email = %s AND senha = %s"
    #         cursor.execute(query, (input_email, input_senha))
    #         dados = cursor.fetchall()
    #         if dados[0][0] == 1:
    #             toast("Login!")
    #         else:
    #             toast("Email ou senha inválidos")
    #
    #     except:
    #         toast("Email ou senha inválidos")
        # except:
        #     toast("Email ou senha inválidos")

    pass

#
# MDTopAppBar:
#             md_bg_color: 1,1,1,0
#             elevation: 0
#             type: "top"
#             pos_hint: {"top": 1}
#             left_action_items: [["arrow-left", lambda x: root.callback()]]