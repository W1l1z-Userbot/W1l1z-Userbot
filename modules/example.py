#  W1l1z-Userbot - telegram userbot
#  Copyright (C) 2024-present W1l1z Userbot Organization

from pyrogram import Client, filters
from pyrogram.types import Message

from utils.misc import modules_help, prefix


# if your module has packages from PyPi

# from utils.scripts import import_library
# example_1 = import_library("example_1")
# example_2 = import_library("example_2")

# import_library() will automatically install required library
# if it isn't installed


@Client.on_message(filters.command("example_edit", prefix) & filters.me)
async def example_edit(client: Client, message: Message):
    await message.edit("<code>This is an example module</code>")


@Client.on_message(filters.command("example_send", prefix) & filters.me)
async def example_send(client: Client, message: Message):
    await client.send_message(
        message.chat.id, "<b>This is an example module</b>"
    )


# This adds instructions for your module
modules_help["example"] = {
    "example_send": "example send",
    "example_edit": "example edit",
}

# modules_help["example"] = { "example_send [text]": "example send" }
#                  |            |              |        |
#                  |            |              |        └─ command description
#           module_name         command_name   └─ optional command arguments
#        (only snake_case)   (only snake_case too)
