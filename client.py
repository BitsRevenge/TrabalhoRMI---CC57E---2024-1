import sys
import threading
import Pyro4
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

#
# if sys.version_info < (3, 0):
#     input = raw_input


import mysql.connector

import variaveis_globais


class Chatter(object):

    def __init__(self, nome_user):
        ns = Pyro4.locateNS(host="localhost", port=9090)
        uri = ns.lookup("example.chatbox.server")
        self.chatbox = Pyro4.core.Proxy(uri)
        self.abort = 0

    @Pyro4.expose
    @Pyro4.oneway
    def message(self, nick, msg):
        if nick != self.nick:
            print('[{0}] {1}'.format(nick, msg))

    @Pyro4.expose
    def start(self):
        self.nick = variaveis_globais.nome_user
        callback = self.get_self()
        self.chatbox.join(self.nick, callback)

    def create_group(self, nome_grupo, usuario_adm, descricao=None):
        self.chatbox.create_group(nome_grupo, usuario_adm, descricao)

    def create_chat(self, usuario1):
        self.chatbox.create_chat_privado(usuario1, "1")

    def getNomes(self):
        return self.chatbox.getNicks()

    def getGrupos(self):
        return self.chatbox.getGrupos()

    def send_message(self, mensagem):
        self.chatbox.send_message_chat_privado(self.nick, variaveis_globais.instancia, mensagem)

    def get_self(self):
        return self

    def destruir_instancia(self):
        self.abort = 1


class DaemonThread(threading.Thread):
    def __init__(self, chatter):
        threading.Thread.__init__(self)
        self.chatter = chatter
        self.setDaemon(True)

    def run(self):
        with Pyro4.core.Daemon() as daemon:
            daemon.register(self.chatter)
            daemon.requestLoop(lambda: not self.chatter.abort)

