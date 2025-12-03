from discord.ext import commands

class Messages(commands.Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command(name="del")
    @commands.has_permissions(manage_messages=True)
    async def delete(self, ctx, number : str) -> None:
        """ Supprime un certain nombre de message sans compter le message de la commande

        Args:
            ctx (_type_): jsp
            number (int): nombre de message à supprimer
        """
        if number.lower() == 'all':
           await ctx.channel.purge(limit=None)
        else:
            # Récupère les messages dans une liste
            num : int = int(number)
            await ctx.channel.purge(limit=num + 1)
