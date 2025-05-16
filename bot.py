# Don't Remove Credit Tg - @Spidey
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class Bot(Client):

    def __init__(self):
        super().__init__(
            "Spidey login",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins=dict(root="Spidey"),
            workers=50,
            sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        print('Bot Started Powered By Spidey Official')

    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')

Bot().run()

# Don't Remove Credit Tg - @Spidey
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
