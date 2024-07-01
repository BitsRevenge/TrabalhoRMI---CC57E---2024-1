import mysql.connector
from kivy.app import App
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

class TelaEsqSenha(MDScreen):
    pass
    def connect(self):
        input_email = self.ids["email"].text
        input_senha_nova = self.ids["senhaNova"].text
        input_senha_nova_conf = self.ids["ConfsenhaNova"].text

        config = {
            'user': 'root',
            'password': SENHA,
            'host': '127.0.0.1',
            'database': 'db_dadosRMI',
        }
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        if input_senha_nova != "" and input_email != "" and input_senha_nova_conf != "":

            try:
                query = "SELECT count(*) FROM tb_usuario WHERE email = %s"
                cursor.execute(query, (input_email,))
                dados = cursor.fetchall()

                if dados[0][0] == 1:
                    sql = "UPDATE tb_usuario SET senha = %s WHERE email = %s"
                    cursor.execute(sql, (input_senha_nova_conf, input_email))
                    conn.commit()
                    toast("Sucesso!")
                else:
                    toast("Email inválido")
            except:
                toast("Email ou senha inválidos")
        else:
            toast("Você precisa preencher todos os campos")
    pass

#
# MDTopAppBar:
#             md_bg_color: 1,1,1,0
#             elevation: 0
#             type: "top"
#             pos_hint: {"top": 1}
#             left_action_items: [["arrow-left", lambda x: root.callback()]]
