## Initializing our bot
We'll pass 3 things to Bot class: 
description - What our bot is,
intents - Intents are discord's permission system, so there are handful of data points that are considered privileged. e.g. guild member presence, so if you've ever seen friend on you friends list and when you click on their profile it says playing .. game for this many hours that's a rich presence and that's a privileged intent and that has more to do with activities than it is going to do with our bot. Another privileged intent is guild member leaving and joining server. Discord has restricted the ability to get that information and the final privileged intent is the message content. SO we require the basic one's that aren't going to require additional confirmation from the user `default()`
debug guilds - It is going to be a list of guild ids in which we want our bot to start.
```python
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

```
