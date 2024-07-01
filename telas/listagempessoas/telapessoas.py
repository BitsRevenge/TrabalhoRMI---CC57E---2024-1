import mysql.connector
from kivy.app import App
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivymd.uix.list import OneLineListItem, OneLineAvatarListItem, IconLeftWidget, OneLineIconListItem, \
    OneLineAvatarIconListItem
from kivymd.uix.screen import MDScreen

from client import DaemonThread, Chatter
from server import ChatBox

class TelaPessoas(MDScreen):
    pass
    def on_pre_enter(self):
        chat_menager = ChatBox()
        pessoas_cad = chat_menager.getNicks()
        pessoas_on = chat_menager.get_pessoas_on()
        pessoas_on = [i[0] for i in pessoas_on]
        pessoas = [i[0] for i in pessoas_cad]
        self.ids.listagem.clear_widgets()
        print(pessoas_on)
        for pessoa in pessoas:
            if pessoa in pessoas_on:
                card = OneLineAvatarIconListItem(IconLeftWidget(
                                                 icon="assets/imagens/button.png"),
                                             text=f"{pessoa}")
            else:
                card = OneLineAvatarIconListItem(text=f"{pessoa}")
            card.bind(on_release=self.on_item_click)
            self.ids.listagem.add_widget(card)

    def on_item_click(self, instance):
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