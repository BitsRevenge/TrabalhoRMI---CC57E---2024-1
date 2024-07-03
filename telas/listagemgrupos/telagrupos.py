import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, OneLineAvatarListItem, IconLeftWidget
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField

import variaveis_globais
from client import DaemonThread, Chatter
from server import ChatBox
import mysql.connector

class TelaGrupos(MDScreen):

    dialog = None
    conn = mysql.connector.connect(**variaveis_globais.config)
    cursor = conn.cursor()
    instancia = ""
    def on_pre_enter(self):
        show = False
        grupos = self.getGrupos()
        try:
            grupos = [i[0] for i in grupos]
            if len(grupos) == 0:
                show = True
        except:
            show = True

        self.ids.listagem.clear_widgets()
        if show:
            text = "Nenhum grupo criado"
            label = OneLineAvatarListItem(text=text)
            self.ids.listagem.add_widget(label)
        else:
            for grupo in grupos:
                card = OneLineAvatarListItem(text=f"{grupo}")
                card.bind(on_release=self.on_item_click)
                self.ids.listagem.add_widget(card)

    def tela_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login"

    def tela_grupos(self):
        self.manager.transition.direction = "left"
        self.manager.current = "grupos"

    def tela_pessoas(self):
        self.manager.transition.direction = "left"
        self.manager.current = "pessoas"

    def getGrupos(self):
        self.cursor.execute("SELECT nome_grupo FROM tb_servidor_grupo")
        return self.cursor.fetchall()

    def create_group(self):
        if not self.dialog:

            self.dialog = MDDialog(
                title="Insira os Detalhes",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        hint_text="Nome do grupo",
                    ),
                    MDTextField(
                        hint_text="Descrição do grupo",
                    ),
                    orientation="vertical",
                    spacing="12dp",
                    size_hint_y=None,
                    height="120dp",
                ),
                buttons=[
                    MDRaisedButton(
                        text="Cancelar",
                        on_release=self.close_dialog
                    ),
                    MDRaisedButton(
                        text="Criar",
                        on_release=self.save_details
                    ),
                ],
            )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        self.dialog = None
        self.on_pre_enter()
    def save_details(self, *args):
        name_field = self.dialog.content_cls.children[1]
        description_field = self.dialog.content_cls.children[0]
        name = name_field.text
        description = description_field.text
        variaveis_globais.descricao = description
        variaveis_globais.nome_grupo = name

        self.close_dialog()


    def reload(self):
        self.on_pre_enter()
    def on_item_click(self, instance):

        if not self.dialog:
            self.instancia = instance.text
            self.dialog = MDDialog(
                title="Deseja mesmo entrar no grupo?",
                type="custom",
                buttons=[
                    MDRaisedButton(
                        text="Cancelar",
                        on_release=self.close_dialog
                    ),
                    MDRaisedButton(
                        text="Entrar",
                        on_release=self.entrar
                    ),
                ],
            )
        self.dialog.open()

    def entrar(self, *args):
        self.cursor.execute("SELECT id_grupo FROM tb_servidor_grupo WHERE nome_grupo = %s", (self.instancia,))
        servidor_id_grupo = self.cursor.fetchall()
        servidor_id_grupo = servidor_id_grupo[0][0]

        self.cursor.execute("SELECT id_user FROM tb_usuario WHERE nome = %s", (variaveis_globais.nome_user,))
        servidor_id_user = self.cursor.fetchall()
        servidor_id_user = servidor_id_user[0][0]

        query = """
                        INSERT INTO tb_grupo (servidor_id_grupo, servidor_id_user)
                        VALUES (%s, %s);
                        """
        self.cursor.execute(query, (servidor_id_grupo, servidor_id_user))
        self.conn.commit()

    pass