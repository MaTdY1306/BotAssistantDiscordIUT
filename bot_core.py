import discord
from discord.ext import commands
from dotenv import load_dotenv
from environnement import Environnement
from Server import Server
import os

class Bot(commands.Bot):

    def __init__(self, environnement : Environnement, server : Server) -> None:
        """Initialisation de la classe Bot

        Args:
            environnement (Environnement): Environnement du Bot
            server (Server): Serveur du Bot
        """
        # Déclaration des autorisation du Bot
        intents : discord.Intents = discord.Intents.default()
        intents.message_content = True
        intents.members = True
        super().__init__(command_prefix="!", intents=intents)

        # Chargement des variables d'environnement
        load_dotenv(dotenv_path=".env")
        self.token : int = os.getenv("DISCORD_TOKEN")


        # Création d'un environnement et d'un serveur
        self.environnement : Environnement = Environnement()
        self.server : Server = Server()

    async def setup_hook(self) -> None:
        import cogs.moderation as moderation_module
        import cogs.messages as messages_module

        await self.add_cog(moderation_module.Moderation(self))
        await self.add_cog(messages_module.Messages(self))

    async def send_message(self, message : str, idChannel : int) -> None:
        """Envoyer un message dans un channel

        Args:
            message (str): message à envoyer
            idChannel (int): identifiant du channel dans lequel envoyer le message
        """
        channel : discord.channel = self.get_channel(idChannel)
        if channel:
            await channel.send(message)
    
    
    async def on_ready(self) -> None:
        """
        Fonction lancée lors du démarrage du Bot
        
        :param self: Bot
        """
        print("Assistant is ready.\n")
        await self.send_message("Hello", self.server.channel_general)
        await self.send_message(f"Aujourd'hui nous sommes le {self.environnement.now.day} {self.environnement.mois[self.environnement.now.month - 1]} {self.environnement.now.year}", 1445410826432282862)

    def start_bot(self) -> None:
        """
        Fonction permettant de démarrer le Bot
        
        :param self: Bot
        """
        self.run(token=self.token)
        