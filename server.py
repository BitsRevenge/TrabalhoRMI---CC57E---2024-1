import os
import shutil

import Pyro4
import mysql.connector

import variaveis_globais


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
        self.instance_user = dict()
        self.dm_channels = {}  # private channels for DMs { (nick1, nick2): [callback1, callback2] }
        self.channel = []
        self.channel_permissions = {}  # channel permissions { channel: [nicks] }

        # all registered nicks on this server

    def getGrupos(self):
        self.cursor.execute("SELECT nome_grupo FROM tb_servidor_grupo")
        return self.cursor.fetchall()

    def getChats(self):
        self.cursor.execute("SELECT servidor_id_user1, servidor_id_user2 FROM tb_servidor_privado")
        return self.cursor.fetchall()

    def getNicks(self):
        self.cursor.execute("SELECT nome FROM tb_usuario")
        return self.cursor.fetchall()

    def set_pessoa_on(self, nick):
        sql = "UPDATE tb_usuario SET estado = 1 WHERE nome = %s"
        self.cursor.execute(sql, (nick,))
        self.conn.commit()

    def set_pessoa_off(self, nick):
        sql = "UPDATE tb_usuario SET estado = False WHERE nome = %s"
        self.cursor.execute(sql, (nick,))
        self.conn.commit()

    def get_pessoas_on(self):
        query = "SELECT nome FROM tb_usuario WHERE estado = 1"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def set_pessoas_all_off(self):
        sql = "UPDATE tb_usuario SET estado = 0 WHERE estado = 1"
        self.cursor.execute(sql)
        self.conn.commit()

    def join(self, nick, callback):
        # print(callback)
        self.instance_user[nick] = callback
        print(self.instance_user)
        self.set_pessoa_on(nick)

    def leave(self, nick):
        self.set_pessoa_off(nick)

    def pass_adm(self, adm_atual, adm_futuro):

        sql = "SELECT id_user FROM tb_usuario WHERE nome = %s"
        self.cursor.execute(sql, (adm_futuro,))
        id_adm_futuro = self.cursor.fetchall()
        id_adm_futuro = id_adm_futuro[0][0]

        sql = "SELECT id_user FROM tb_usuario WHERE nome = %s"
        self.cursor.execute(sql, (adm_futuro,))
        id_adm_atual = self.cursor.fetchall()
        id_adm_atual = id_adm_atual[0][0]

        sql = "UPDATE tb_servidor_grupo SET grupo_adm_user = %s WHERE grupo_adm_user = %s"
        self.cursor.execute(sql, (id_adm_futuro, id_adm_atual))
        grupo_adm_user = self.cursor.fetchall()
        grupo_adm_user = grupo_adm_user[0][0]

        return ("ADM mudado com sucesso")

    def leave_group(self, nome_grupo, usuario):

        sql = "SELECT grupo_adm_user FROM tb_servidor_grupo WHERE nome_grupo = %s"
        self.cursor.execute(sql, (nome_grupo,))
        grupo_adm_user = self.cursor.fetchall()
        grupo_adm_user = grupo_adm_user[0][0]

        sql = "SELECT id_user FROM tb_usuario WHERE nome = %s"
        self.cursor.execute(sql, (usuario,))
        id_user = self.cursor.fetchall()
        id_user = id_user[0][0]

        if (grupo_adm_user == id_user):
            return ("Passa o ADM pra alguem")

        else:
            for (n, c) in self.channels[nome_grupo]:
                if n == usuario:
                    self.channels[nome_grupo].remove((n, c))

                    # Ver se deleta também a tb_permissão, se não colocar ON_CASCADE
                    sql = "DELETE FROM tb_grupo WHERE servidor_id_user = %s"
                    self.cursor.execute(sql, (id_user,))
                    break

        self.conn.commit()
        return ("Saiu")

    def add_permission(self, user_to_add, nome_grupo):

        if user_to_add in self.channel_permissions[nome_grupo]:
            return
        else:
            self.channel_permissions[nome_grupo].append(user_to_add)

            self.cursor.execute("SELECT id_user FROM tb_usuario WHERE nome = %s", (user_to_add,))
            id_user = self.cursor.fetchall()
            id_user = id_user[0][0]

            self.cursor.execute("SELECT id_grupo FROM tb_servidor_grupo WHERE nome_grupo = %s", (nome_grupo,))
            id_grupo = self.cursor.fetchall()
            id_grupo = id_grupo[0][0]

            query = "INSERT INTO tb_permissao (id_usuario, id_grupo) VALUES (%s, %s);"
            self.cursor.execute(query, (id_user, id_grupo))

            self.conn.commit()


    def enter_group(self, nome_grupo, usuario1):

        pos = None
        try:
            if (usuario1 not in self.channel_permissions[nome_grupo]):
                return print("SEM PERMISSAO")
        except:
            pass

        self.cursor.execute("SELECT id_grupo FROM tb_servidor_grupo WHERE nome_grupo = %s", (nome_grupo,))
        servidor_id_grupo = self.cursor.fetchall()
        servidor_id_grupo = servidor_id_grupo[0][0]

        self.cursor.execute("SELECT id_user FROM tb_usuario WHERE nome = %s", (usuario1,))
        servidor_id_user = self.cursor.fetchall()
        servidor_id_user = servidor_id_user[0][0]

        query = """
                INSERT INTO tb_grupo (servidor_id_grupo, servidor_id_user)
                VALUES (%s, %s);
                """
        self.cursor.execute(query, (servidor_id_grupo, servidor_id_user))
        self.conn.commit()

        for indice, tupla in enumerate(self.instance_user):
            if (usuario1 in tupla):
                pos = indice
                break
        # try:
        self.channels[nome_grupo].append((usuario1, self.instance_user[pos][1]))
        # except:
        #     return "Deu problemas"


    def create_group(self, nome_grupo, usuario_adm, descricao=None):

        self.cursor.execute("SELECT id_user FROM tb_usuario WHERE nome = %s", (usuario_adm,))
        grupo_adm_user = self.cursor.fetchone()
        grupo_adm_user = grupo_adm_user[0]

        query = "INSERT INTO tb_servidor_grupo (nome_grupo, descricao, grupo_adm_user) VALUES (%s, %s, %s);"
        self.cursor.execute(query, (nome_grupo, descricao, grupo_adm_user))

        self.cursor.execute("SELECT id_grupo FROM tb_servidor_grupo WHERE nome_grupo = %s", (nome_grupo,))
        servidor_id_grupo = self.cursor.fetchall()
        servidor_id_grupo = servidor_id_grupo[0][0]

        sql = "INSERT INTO tb_grupo (servidor_id_grupo, servidor_id_user) VALUES (%s, %s)"
        self.cursor.execute(sql, (servidor_id_grupo, grupo_adm_user))

        self.conn.commit()

        self.channel_permissions[nome_grupo] = [usuario_adm]  # Creator has permission
        self.channels[nome_grupo] = []


        for indice, tupla in enumerate(self.instance_user):
            if (usuario_adm in tupla):
                pos = indice
                break

        try:
            self.channels[nome_grupo].append((usuario_adm, self.instance_user[pos][1]))
        except:
            pass

    def send_message_group(self, nome_grupo, usuario1, mensagem):  # criar logs

            try:
                self.instance_user.get(usuario1).message(usuario1, mensagem)  # oneway call
            except Pyro4.errors.ConnectionClosedError:
                pass

    def send_message_chat_privado(self, usuario1, usuario2, mensagem):  # criar logs

        for cback in self.dm_channels[(usuario1, usuario2)]:
            print(cback)
            try:
                cback.message(usuario1, f"DM from {usuario1}: {mensagem}")
            except Pyro4.errors.ConnectionClosedError:
                return f"Failed to send DM to {usuario2}."
        return f"DM sent to {usuario2}."
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
        daemon = Pyro4.Daemon(host="localhost", port=9090)
        ns = Pyro4.locateNS(host='localhost', port=9090)  # Ensure these match your nameserver settings
        print("Nameserver located.")
    except Pyro4.errors.NamingError as e:
        print("Failed to locate the nameserver: ", e)
        raise

    # Register the ChatBox object
    uri = daemon.register(ChatBox)

    # Register the object with the nameserver
    ns.register("example.chatbox.server", uri)

    print("ChatBox server is running.")

    # Start the event loop of the server to wait for calls
    daemon.requestLoop()
