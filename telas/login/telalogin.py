import mysql.connector
from kivy.app import App
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

from client import Chatter, DaemonThread
from server import ChatBox
from telas.listagempessoas.telapessoas import TelaPessoas


class TelaLogin(MDScreen):
    pass
    def criar_instancia_user(self):

        config = {
            'user': 'root',
            'password': SENHA,
            'host': '127.0.0.1',
            'database': 'db_dadosRMI',
        }
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        input_email = self.ids["email"].text
        input_senha = self.ids["senha"].text

        chat_menager = ChatBox()
        pessoas_cad = chat_menager.getNicks()
        pessoas = [i[0] for i in pessoas_cad]
        pessoas_on = chat_menager.get_pessoas_on()
        pessoas_on = [i[0] for i in pessoas_on]
        chatter = Chatter()
        daemonthread = DaemonThread(chatter)
        daemonthread.start()
        query = "SELECT nome FROM tb_usuario WHERE email = %s AND senha = %s"
        cursor.execute(query, (input_email, input_senha))
        dados = cursor.fetchall()
        # try:
        if dados[0][0] in pessoas_on:
            chat_menager.leave(dados[0][0])
            chatter.destruir_instancia()
            chatter.build(pessoas, dados[0][0])
        else:
            chatter.build(pessoas, dados[0][0])
        self.manager.transition.direction = "left"
        self.manager.current = "pessoas"
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
