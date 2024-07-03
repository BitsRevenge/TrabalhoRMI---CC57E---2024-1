import mysql.connector
from kivy.app import App
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.list import OneLineListItem, OneLineAvatarListItem, IconLeftWidget, OneLineIconListItem, \
    OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen
import variaveis_globais
from client import DaemonThread, Chatter
from server import ChatBox
class TelaPessoas(MDScreen):
    conn = mysql.connector.connect(**variaveis_globais.config)
    cursor = conn.cursor()

    def on_pre_enter(self):
        pessoas_cad = self.getNicks()
        pessoas_on = self.get_pessoas_on()
        pessoas_on = [i[0] for i in pessoas_on]
        pessoas = [i[0] for i in pessoas_cad]
        self.ids.listagem.clear_widgets()
        for pessoa in pessoas:
            if pessoa in pessoas_on:
                card = OneLineAvatarIconListItem(IconLeftWidget(
                                                 icon="assets/imagens/button.png"),
                                             text=f"{pessoa}")
            else:
                card = OneLineAvatarIconListItem(text=f"{pessoa}")
            card.bind(on_release=self.on_item_click)
            self.ids.listagem.add_widget(card)

    def getNicks(self):
        self.cursor.execute("SELECT nome FROM tb_usuario")
        return self.cursor.fetchall()

    def set_pessoa_on(self, nick):
        sql = "UPDATE tb_usuario SET estado = 1 WHERE nome = %s"
        self.cursor.execute(sql, (nick,))
        self.conn.commit()

    def get_pessoas_on(self):
        query = "SELECT nome FROM tb_usuario WHERE estado = 1"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def on_item_click(self, instance):
        variaveis_globais.instancia = instance.text
        self.manager.transition.direction = "right"
        self.manager.current = "conversa"

    def tela_login(self):
        self.manager.transition.direction = "right"
        self.manager.current = "login"

    def tela_grupos(self):
        self.manager.transition.direction = "left"
        self.manager.current = "grupos"

    def tela_pessoas(self):
        self.manager.transition.direction = "left"
        self.manager.current = "pessoas"

    pass