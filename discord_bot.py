import discord
from discord.ext import commands, tasks
import aiohttp
import os
 
intents = discord.Intents.default()
intents.message_content = True
 
bot = commands.Bot(command_prefix="!", intents=intents)
 
KUMA_PUSH_URL = os.getenv("KUMA_PUSH_URL")
 
 
@tasks.loop(seconds=60)
async def heartbeat():
    if not KUMA_PUSH_URL or not bot.is_ready():
        return
    try:
        timeout = aiohttp.ClientTimeout(total=10)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            await session.get(KUMA_PUSH_URL)
    except Exception as e:
        print(f"Heartbeat falló: {e}")
 
 
@bot.event
async def on_ready():
    print("Bot conectado")
    if not heartbeat.is_running():
        heartbeat.start()
 
 
@bot.command()
async def build(ctx, personaje: str):
 
    ruta = f"builds/{personaje.lower()}.png"
 
    if os.path.exists(ruta):
        await ctx.send(file=discord.File(ruta))
    else:
        await ctx.send("❌ No tengo ese build.")
 
 
TOKEN = os.getenv("DISCORD_TOKEN")
 
bot.run(TOKEN)