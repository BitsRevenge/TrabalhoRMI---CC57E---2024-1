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

from client import DaemonThread, Chatter
from server import ChatBox

class TelaGrupos(MDScreen):

    dialog = None

    def on_pre_enter(self):
        show = False
        chat_menager = ChatBox()
        grupos = chat_menager.getGrupos()
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

    def create_group(self):
        if not self.dialog:

            self.dialog = MDDialog(
                title="Insira os Detalhes",
                type="custom",
                content_cls=MDBoxLayout(
                    MDTextField(
                        hint_text="City",
                    ),
                    MDTextField(
                        hint_text="Street",
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

    def save_details(self, *args):
        name_field = self.dialog.content_cls.children[1]
        description_field = self.dialog.content_cls.children[0]
        name = name_field.text
        description = description_field.text

        print(f"Nome: {name}")
        print(f"Descrição: {description}")

        self.close_dialog()

    def on_item_click(self, instance):
        self.manager.transition.direction = "right"
        self.manager.current = "conversa_grupo"

    pass