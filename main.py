import os
from discord import Bot, Intents
from dotenv import load_dotenv


bot = Bot(
    description='Darqbot is the ugliest bot!',
    intents=Intents.default(),
    debug_guilds=[985532814067925002]
)


@bot.event
async def on_ready() -> None:
    print("Darqbot Online!")

load_dotenv()

bot.run(os.getenv("DISCORD_TOKEN"))
