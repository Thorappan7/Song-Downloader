import os

class Config(object):
    DATABASE = os.environ.get("DB_URI", "mongodb+srv://poojabot:poojabot@cluster0.abcos.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5297426893").split())
    SUPPORT = os.environ.get("SUPPORT")
    BOT_NAME = os.environ.get("bat","Song Download")
    BOT_USERNAME = os.environ.get("bn",songyt_dl_bot)
