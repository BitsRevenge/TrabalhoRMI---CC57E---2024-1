import mysql.connector
from kivy.app import App
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen

class TelaConversa(MDScreen):
    pass
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
        pass

    def send_arquivo(self):
        pass

#
# MDTopAppBar:
#             md_bg_color: 1,1,1,0
#             elevation: 0
#             type: "top"
#             pos_hint: {"top": 1}
#             left_action_items: [["arrow-left", lambda x: root.callback()]]