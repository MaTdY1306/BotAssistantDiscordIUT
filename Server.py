from dotenv import load_dotenv
import os

class Server:

    def __init__(self):

        load_dotenv(".env")
        self.channel_general : int = int(os.getenv("CHANNEL_ID_GENERAL"))
        self.channel_touche_ton_nez : int = int(os.getenv("CHANNEL_ID_TOUCHE_TON_NEZ"))

    def getChannelGeneral(self) -> int:
        """ Renvoie l'identifiant du channel #general du serveur

        Returns:
            int: identifiant du channel #general
        """
        return self.channel_general