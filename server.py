import os
import shutil

import Pyro4
import mysql.connector

# Chat box administration server.
# Handles logins, logouts, channels and nicknames, and the chatting.
@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class ChatBox(object):
    def __init__(self):
        self.channels = {}  # registered channels { channel --> (nick, client callback) list }
        self.config = {
            'user': 'root',
            'password': '1234',
            'host': '127.0.0.1',
            'database': 'db_dadosRMI',
        }
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()
        self.nicks = self.getNicks()
        self.grupos = self.getGrupos()
        self.chats = self.getChats()
        # all registered nicks on this server

    def getGrupos(self):
        self.cursor.execute("SELECT nome_grupo FROM tb_grupo")
        return self.cursor.fetchall()

    def getChats(self):
        self.cursor.execute("SELECT servidor_id_user1, servidor_id_user2 FROM tb_servidor_privado")
        return self.cursor.fetchall()

    def getNicks(self):
        self.cursor.execute("SELECT nome FROM tb_usuario")
        return self.cursor.fetchall()

    def set_pessoa_on(self, nick):
        sql = "UPDATE tb_usuario SET estado = 1 WHERE nome = %s"
        self.cursor.execute(sql, (nick, ))
        self.conn.commit()

    def set_pessoa_off(self, nick):
        sql = "UPDATE tb_usuario SET estado = False WHERE nome = %s"
        self.cursor.execute(sql, (nick, ))
        self.conn.commit()

    def get_pessoas_on(self):
        query = "SELECT nome FROM tb_usuario WHERE estado = 1"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def set_pessoas_all_off(self):
        sql = "UPDATE tb_usuario SET estado = 0 WHERE estado = 1"
        self.cursor.execute(sql)
        self.conn.commit()

    def join(self, channel, nick, callback):

        self.set_pessoa_on(nick)
        print("%s JOINED %s" % (nick, channel))

    def leave(self, nick):
        self.set_pessoa_off(nick)

    def create_group(self, nome_grupo, usuario_adm, descricao=None):
        pass

    def send_message_group(self, usuario1, mensagem): # criar logs
        pass

    def create_chat_privado(self, usuario1, usuario2):
        pass

    def send_message_chat_privado(self, usuario1, usuario2, mensagem): # criar logs
        pass

    # def upload(self, channel, nick, arq):
    #     os.chdir('..')
    #     nome = ''
    #     for i in arq[::-1]:
    #         if i != '\':
    #             nome = i + nome
    #         else:
    #             break
    #     try:
    #         shutil.copy(arq[8:], os.getcwd() + '\servidor\' + nome)
    #     except:
    #         print('Erro arquivo não encontrado')
    #
    # def download(self, channel, nick, arq):
    #     os.chdir('..')
    #     nome = ''
    #     for i in arq[::-1]:
    #         if i != ' ':
    #             nome = i + nome
    #         else:
    #             break
    #     try:
    #         shutil.copy(os.getcwd()+'\servidor\'+nome, 'C:\Users\hmmli\Downloads\' + nome)
    #     except:
    #         print('Erro arquivo não encontrado')




if __name__ == "__main__":
    # Locate the Pyro nameserver
    try:
        ns = Pyro4.locateNS(host='localhost', port=9090)  # Ensure these match your nameserver settings
        print("Nameserver located.")
    except Pyro4.errors.NamingError as e:
        print("Failed to locate the nameserver: ", e)
        raise

    # Create a Pyro daemon
    daemon = Pyro4.Daemon()

    # Register the ChatBox object
    uri = daemon.register(ChatBox)

    # Register the object with the nameserver
    ns.register("example.chatbox.server", uri)

    print("ChatBox server is running.")

    # Start the event loop of the server to wait for calls
    daemon.requestLoop()
    chat_manager = ChatBox()
    chat_manager.set_pessoas_all_off()
