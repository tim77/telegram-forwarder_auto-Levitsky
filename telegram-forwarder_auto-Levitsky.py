#!/usr/bin/env python3

from pyrogram import Client, filters
from pyrogram.types import Message

import config

api_id = config.ID
api_hash = config.HASH

app = Client("USERBOT", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.chat(config.LIST_NAMEs))
async def name(client, message):
    await message.forward(config.FORWARD_NAME)


app.run()
