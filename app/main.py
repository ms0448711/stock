from dotenv import load_dotenv
from bot import bot
import os

load_dotenv()


bot.run(os.environ['DISCORD_TOKEN'])