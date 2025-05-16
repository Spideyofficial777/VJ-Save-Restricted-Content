import os
from os import path, getenv, environ

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28519661"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d47c74c8a596fd3048955b322304109d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5518489725"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://vajoko2131:x3qqdqblhmi0s2fX@cluster0.xrpgiv7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "spideysavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

#LOG CHANNEL for the user logs
LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1002423451263"))

#imgs
START_IMG = (environ.get('START_IMG', 'https://graph.org/file/2518d4eb8c88f8f669f4c.jpg https://graph.org/file/d6d9d9b8d2dc779c49572.jpg https://graph.org/file/4b04eaad1e75e13e6dc08.jpg https://graph.org/file/05066f124a4ac500f8d91.jpg https://graph.org/file/2c64ed483c8fcf2bab7dd.jpg https://i.ibb.co/CPxdkHR/IMG-20240818-192201-633.jpg')).split()
WELCOME_IMAGE = (environ.get('WELCOME_IMAGE', 'https://envs.sh/v3t.jpg')).split()

#for the forceSub 
CHANNEL_IDS = list(map(int, getenv("CHANNEL_IDS", "-1002470391435,-1002433552221").split(",")))

#temp
"""class temp(object):    
    U_NAME = None
    B_NAME = None
    MELCOW = {}"""