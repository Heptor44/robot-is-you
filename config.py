import discord

activity = "ROBOT IS HELP"
description = "*An entertainment bot for rendering levels and custom scenes based on the indie game Baba Is You.*"
prefixes = ["+", "Robot is ", "robot is ", "ROBOT IS "]
trigger_on_mention = True
webhook_id = 594692503014473729
owner_id = 156021301654454272
embed_color = discord.Color(9077635)
auth_file = "config/auth.json"
log_file = "log.txt"
cogs = [
    "src.cogs.owner",
    "src.cogs.global",
    "src.cogs.meta",
    "src.cogs.errorhandler",
    "src.cogs.reader",
    "src.cogs.utilities",
    "jishaku"
]
