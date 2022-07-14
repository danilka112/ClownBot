import discord
from discord.ext import commands

class help_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.help_message = """
'''
Команды:
/help - Я не ебу чё оно делает
/p <Название> - Находит видио по url
/q - Показывает очередь
/skip - Догадайся чё делает
/clear - Останавливает трек и чистит очередь
/leave - Кикает бота из войса
/pause - Ну пауза наверное я не ебу
/resume - Ты даун?
'''
"""
        self.text_channel_text = []

    @commands.Cog.listener()
    async def on_read(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)

    @commands.command(name='help', help='Подсказка')
    async def help(self, ctx):
        await ctx.send(self.help_message)