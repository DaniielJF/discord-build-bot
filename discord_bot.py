import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot conectado")

@bot.command()
async def build(ctx, personaje: str):

    ruta = f"builds/{personaje.lower()}.png"

    if os.path.exists(ruta):
        await ctx.send(file=discord.File(ruta))
    else:
        await ctx.send("❌ No tengo ese build.")

TOKEN = os.getenv("DISCORD_TOKEN")

bot.run(TOKEN)

#bot.run("MTQ3OTk5NzQzMjUxMDI4MzkxOQ.Gz_BkQ.Lkpa95INHzVXqXWTYE59-BrZsB_RcbROHGnXTk")