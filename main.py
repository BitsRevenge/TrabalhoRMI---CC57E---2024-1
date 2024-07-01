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
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.screenmanager import MDScreenManager

from server import ChatBox
from telas.escolherArquivo import FileChooserPopup
from telas.esquecisenha.esquecisenha import TelaEsqSenha
from telas.listagemgrupos.telagrupos import TelaGrupos
from telas.listagempessoas.telapessoas import TelaPessoas
from telas.login.telalogin import TelaLogin
from telas.registrar.telaregistrar import TelaRegistrar
from telas.telaconversa.telaconversa import TelaConversa
from telas.telamanager import MainScreenManager


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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        self.sm = MDScreenManager()

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


# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
