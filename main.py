from environnement import Environnement
from bot_core import Bot
from Server import Server

if __name__ == '__main__':

    environnement : Environnement = Environnement()
    server : Server = Server()

    assistant : Bot = Bot(environnement=environnement, server=server)
    assistant.start_bot()