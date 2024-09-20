import discord
from discord.ext import commands
from stock import show_average


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
tree = bot.tree

@bot.event
async def on_ready():
    await bot.wait_until_ready()
    slash = await bot.tree.sync()
    print(f"目前登入身份 --> {bot.user}")
    print(f"載入 {len(slash)} 個斜線指令")


@tree.command(name = "hello", description = "Hello, world!")
async def hello(interaction: discord.Interaction):
    # 回覆使用者的訊息
    await interaction.response.send_message("Hello, world")


