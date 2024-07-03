import mysql.connector
from kivy.app import App
from kivymd.toast import toast
from kivymd.uix.list import BaseListItem
from kivymd.uix.screen import MDScreen

import variaveis_globais
from server import ChatBox


class TelaConversa(MDScreen):
    pass
    def on_pre_enter(self):
        self.ids.listagem.clear_widgets()
        mensagens = ["" for i in range(10)]
        for mensagem in mensagens:
            card = BaseListItem(text=f"{mensagem}")
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
        # pass

    def send_message(self):
        mensagem = self.ids.send.text
        variaveis_globais.mensagem = mensagem

    def send_arquivo(self):
        pass

#
# MDTopAppBar:
#             md_bg_color: 1,1,1,0
#             elevation: 0
#             type: "top"
#             pos_hint: {"top": 1}
#             left_action_items: [["arrow-left", lambda x: root.callback()]]