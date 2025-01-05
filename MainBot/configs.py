class Config(object):
    TOKEN = ""  # Get bot token from bot father
    DB_URI = "mongodb+srv://*****:******@*******.9wgb5ar.mongodb.net/JoinRequestApprovalRoBot?retryWrites=true&w=majority"  # mongodb uri from mongodb
    BOT_USERNAME = ""  # Bot username
    OWNER_ID = "1608141072"  # Owner ID
    OWNER_USERNAME = "goyalcompany"  # Owner username
    DEV_USERNAME = "PythonDeveloperHub"
    ADMINS = set(["1608141072"])  # Default admins
    ERROR_LOGS = -10000000000  # Error logger chat id
    PUBLISHING_CHATS = set(["-10000000000"])


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
