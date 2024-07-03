import os
import subprocess

from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
import chardet
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.textfield import MDTextField

import variaveis_globais
from client import Chatter, DaemonThread
from telas.escolherArquivo import FileChooserPopup
from telas.esquecisenha.esquecisenha import TelaEsqSenha
from telas.listagemgrupos.telagrupos import TelaGrupos
from telas.listagempessoas.telapessoas import TelaPessoas
from telas.login.telalogin import TelaLogin
from telas.registrar.telaregistrar import TelaRegistrar
from telas.telaconversa.telaconversa import TelaConversa
from telas.telamanager import MainScreenManager
import mysql.connector

class LiveApp(MDApp, App):

    Window.size=(300, 600)

    DEBUG = 1

    KV_FILES = {
        os.path.join(os.getcwd(), "telas/telamanager.kv"),
        os.path.join(os.getcwd(), "telas/login/telalogin.kv"),
        os.path.join(os.getcwd(), "telas/registrar/telaregistrar.kv"),
        os.path.join(os.getcwd(), "telas/listagempessoas/telapessoas.kv"),
        os.path.join(os.getcwd(), "telas/listagemgrupos/telagrupos.kv"),
        os.path.join(os.getcwd(), "telas/telaconversa/telaconversa.kv"),
    }


    CLASSES = {
        "MainScreenManager": "telas.telamanager",
        "TelaLogin": "telas.login.telalogin",
        "TelaRegistrar": "telas.registrar.telaregistrar",
        "TelaEsqSenha": "telas.esquecisenha.esquecisenha",
        "TelaPessoas": "telas.listagempessoas.telapessoas",
        "TelaGrupos":  "telas.listagemgrupos.telagrupos",
        "TelaConversa":  "telas.telaconversa.telaconversa",
    }


    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    dialog = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.sm = MDScreenManager()
        self.chatter = Chatter(nome_user=variaveis_globais.nome_user)
        self.daemonthread = DaemonThread(self.chatter)

    def build_app(self, **kwargs):
        self.theme_cls.primary_palette= "DeepPurple"
        self.sm.add_widget(TelaLogin())
        self.sm.add_widget(TelaRegistrar())
        self.sm.add_widget(TelaEsqSenha())
        self.sm.add_widget(TelaPessoas())
        self.sm.add_widget(TelaGrupos())
        self.sm.add_widget(TelaConversa())
        return Factory.MainScreenManager()

    def tema_dark(self):
        self.theme_cls.theme_style = "Dark"

    def tema_light(self):
        self.theme_cls.theme_style = "Light"

    def show_file_chooser(self):
        if os.name == 'nt':  # Windows
            os.startfile(os.getcwd())
        elif os.name == 'posix':
            if subprocess.run(["uname", "-s"], capture_output=True).stdout.strip() == b'Darwin':  # macOS
                subprocess.run(["open", "."])
            else:  # Assume Linux
                subprocess.run(["xdg-open", "."])

    def criar_instancia_user(self):

        # try:
        # if dados[0][0] in pessoas_on:
        #     self.chat.leave(variaveis_globais.nome_user)
        #     chatter.destruir_instancia()
        #     chatter.start()
        # else:
        try:
            self.daemonthread.start()
            self.chatter.start()
        except:
            pass

    def getNomes(self):
        return self.chatter.getNomes()

    def getGrupos(self):
        return self.chatter.getGrupos()

    def send_message_chat_privado(self):
        self.chatter.send_message(variaveis_globais.mensagem)

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


    def save_details(self, *args):
        name_field = self.dialog.content_cls.children[1]
        description_field = self.dialog.content_cls.children[0]
        name = name_field.text
        description = description_field.text

        self.criar_grupo(name, variaveis_globais.nome_user, description)
        self.close_dialog()

    def criar_grupo(self, nome_grupo, nome_user, descricao):
        self.chatter.create_group(nome_grupo, nome_user, descricao)


# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
