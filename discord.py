import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Event when bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# Simple command to reply with a chatbot-like message
@bot.command(name='chat', help='Chat with the bot!')
async def chat(ctx, *, message):
    response = chatbot_response(message)
    await ctx.send(response)

# A simple chatbot function (replace this with more advanced logic if needed)
def chatbot_response(message):
    if 'hello' in message.lower():
        return 'Hello! How can I assist you today?'
    else:
        return "I'm not sure how to respond to that, but I'm learning!"

bot.run(TOKEN)
