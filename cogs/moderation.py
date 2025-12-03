from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    
    @commands.command(name="ban")
    @commands.has_permissions(ban_members=True)
    async def ban_member(self, ctx, member : commands.MemberConverter, *, reason : str = "Aucune raison fournie") -> None:
        await member.ban(reason=reason)

        await ctx.send(f"Le membre {member.mention} a été banni, raison => **{reason}**")
        
    @commands.command(name="unban")
    @commands.has_permissions(ban_members=True)
    async def unban_member(self, ctx, member : commands.MemberConverter, *, reason : str = "Aucune raison définie") -> None:
        await member.unban(reason=reason)
        await ctx.send(f"Le membre {member.mention} est de retour sur le serveur !")
         