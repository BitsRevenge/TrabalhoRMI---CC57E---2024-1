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

class Chatter(object):

    def __init__(self):
        self.chatbox = Pyro4.core.Proxy('PYRONAME:example.chatbox.server')
        self.abort = 0

    @Pyro4.expose
    @Pyro4.oneway
    def message(self, nick, msg):
        if nick != self.nick:
            print('[{0}] {1}'.format(nick, msg))

    def build(self, nomes, nome_user):
        if nomes:

            pass
        self.nick = nome_user
        people = self.chatbox.join("servidor", self.nick, self)

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

