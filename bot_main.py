import discord
from discord.ext import commands
import random
import json
import secrets

BOT_TOKEN = secrets.token
bucket_maps_stock = "./bucket/stock.json"

with open(bucket_maps_stock, 'r') as f:
    map_data = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


def get_random_map(map_list):
    return random.choice(map_list)


# Event: When the bot is ready
@bot.event
async def on_ready():
    print(f'LOGIN :: {bot.user}')


bot.run(BOT_TOKEN)
# TODO ... a lot!
